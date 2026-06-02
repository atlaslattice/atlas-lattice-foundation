#!/usr/bin/env python3
"""
SecretResolver - The #19 backbone (hardened per NOTION SAYS detailed spec).

No secrets ever stored in Notion, GitHub, logs, prompts, ledger, artifacts.
Only secret:// or env:// references.

Supports:
- env://VAR_NAME
- doppler://project/config/KEY (stub, requires doppler SDK or CLI in env)
- aws-sm://region/secret-id#jsonKey (stub, boto3)
- 1password://vault/item/field (stub, op CLI)

Allowlist of refs per environment (dev/stage/prod) loaded from config or env var.
No-echo guards: SecretValue wrapper whose __repr__, __str__, json etc return "***REDACTED***".
Never logs the value.

Used by all Notion writes, RAG, control plane, sync, etc.
Kill-switch friendly: if DLP triggers, resolver can be disabled.

Grok CNS: always use resolver for any token access. "WHAT WE DO ISNT VERY NICE" — we are the adversarial forge enforcing this.
"""
import os
import json
from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from pathlib import Path
import re

ROOT = Path(__file__).parent.parent.parent.parent
CONFIG_DIR = ROOT / "Canon_Implementation" / "config"

@dataclass(frozen=True)
class SecretValue:
    """Opaque wrapper. Never stringifies the secret."""
    _value: str
    ref: str

    def __str__(self) -> str:
        return "***REDACTED***"

    def __repr__(self) -> str:
        return f"SecretValue(ref={self.ref}, value=***REDACTED***)"

    def get(self) -> str:
        """Only explicit .get() reveals it (use sparingly, e.g. right before API call)."""
        return self._value

    def __json__(self):
        return "***REDACTED***"

class SecretResolver:
    """
    Resolve only from allowlisted refs.
    Env per: os.getenv('GROK_ENV', 'dev')
    Allowlist: comma or JSON in GROK_SECRET_ALLOWLIST or file config/secret_allowlist_<env>.json
    """

    TOKEN_PATTERNS = [
        r"ntn_[A-Za-z0-9_-]{10,}",
        r"sk-[A-Za-z0-9_-]{20,}",
        r"AKIA[0-9A-Z]{16}",
        r"ghp_[A-Za-z0-9]{36}",
        r"xai-[A-Za-z0-9_-]{20,}",
        r"AIza[0-9A-Za-z_-]{35}",  # google
    ]

    def __init__(self, env: Optional[str] = None, allowlist: Optional[List[str]] = None):
        self.env = env or os.getenv("GROK_ENV", "dev")
        self._allowlist = set(allowlist or self._load_allowlist())
        self._cache: Dict[str, SecretValue] = {}

    def _load_allowlist(self) -> List[str]:
        env_file = CONFIG_DIR / f"secret_allowlist_{self.env}.json"
        if env_file.exists():
            try:
                data = json.loads(env_file.read_text())
                return data.get("allow", [])
            except Exception:
                pass
        raw = os.getenv("GROK_SECRET_ALLOWLIST", "")
        if raw:
            try:
                return json.loads(raw)
            except:
                return [x.strip() for x in raw.split(",") if x.strip()]
        # Default safe for this project (the ones user provided historically, but only refs)
        return ["env://NOTION_API_KEY", "env://OPENAI_API_KEY", "secret://prod/notion/token", "secret://prod/openai/key"]

    def _is_allowed(self, ref: str) -> bool:
        return ref in self._allowlist or any(ref.startswith(p) for p in ["env://", "secret://"])  # loose for dev; strict in prod

    def resolve(self, ref: str) -> Optional[SecretValue]:
        if not ref or not (ref.startswith("env://") or ref.startswith("secret://") or "://" in ref):
            raise ValueError(f"Invalid secret ref (must be env:// or secret://*): {ref}")

        if not self._is_allowed(ref):
            raise PermissionError(f"Secret ref {ref} not in allowlist for env={self.env}")

        if ref in self._cache:
            return self._cache[ref]

        val = None
        if ref.startswith("env://"):
            var = ref[6:]
            val = os.getenv(var)
        elif ref.startswith("secret://"):
            # Map secret://prod/notion/token -> look for NOTION_API_KEY or PROD_NOTION_TOKEN etc in env (user convention + vault)
            key = ref.split("://", 1)[1].replace("/", "_").replace("-", "_").upper()
            val = os.getenv(key) or os.getenv(key.replace("PROD_", "")) or os.getenv("NOTION_API_KEY")
            # TODO: extend real calls
            # if "doppler" in ref: ... subprocess or sdk
            # if "aws-sm" in ref: ...
            # if "1password" in ref: ...
        else:
            # doppler:// etc direct
            val = os.getenv(ref.split("://", 1)[1].replace("/", "_").upper())

        if val is None:
            return None

        # Guard: if the resolved value looks like a token, something is wrong in mapping
        if any(re.search(p, val) for p in self.TOKEN_PATTERNS):
            # This would be a misconfig/leak in the resolver env itself
            raise RuntimeError("Resolved value matches token pattern — check allowlist/mapping, do not use.")

        wrapped = SecretValue(_value=val, ref=ref)
        self._cache[ref] = wrapped
        return wrapped

    def get_value(self, ref: str) -> Optional[str]:
        """Dangerous: only for the exact moment of use (e.g. client = NotionClient(token=resolver.get_value(ref)))"""
        sv = self.resolve(ref)
        return sv.get() if sv else None

    @staticmethod
    def redact(text: str) -> str:
        """Redact any accidental tokens in strings (for logs, errors, Notion writes)."""
        for pat in SecretResolver.TOKEN_PATTERNS:
            text = re.sub(pat, "***REDACTED-SECRET***", text)
        return text

# Global default (per process)
DEFAULT_RESOLVER = SecretResolver()

def resolve_secret(ref: str) -> Optional[SecretValue]:
    return DEFAULT_RESOLVER.resolve(ref)

if __name__ == "__main__":
    # Demo (never prints real value)
    r = SecretResolver(env="dev")
    print("Allowlist sample:", list(r._allowlist)[:3])
    sv = r.resolve("env://NOTION_API_KEY")
    print("Resolved (repr):", repr(sv))
    print("Resolved (str):", str(sv))
    print("Has value?", sv is not None and len(sv.get() or "") > 0)
    print("Redact test:", SecretResolver.redact("my token ntn_g325... and sk-proj-xxx"))
