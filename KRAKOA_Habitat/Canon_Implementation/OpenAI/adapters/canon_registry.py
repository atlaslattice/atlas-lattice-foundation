#!/usr/bin/env python3
"""
CanonRegistry - Canon vs Candidate governance model (#4 + #20).

Protected pages/databases have:
- list of allowed editors/approvers (human-root is ultimate)
- promotion rules (what makes something canon: lint pass, bullshit pass, human approve, ledger entry, no DLP, evidence packs for RAG claims)

Enforce:
- Candidate artifacts generated freely (sim, local writes, temp pages).
- Canon writes require check + human-root flag (PublicReleaseClass already has human_root_approved).

Can be backed by Notion DB (recommended for live) or local JSON config (for bootstrap).

Used by semantic-diff-review, control plane promotion, RAG accept-to-claim, docs compiler, etc.

Wired into engine for #20.
"""
import json
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional, Set
from pathlib import Path
import datetime

ROOT = Path(__file__).parent.parent.parent.parent
REGISTRY_FILE = ROOT / "Canon_Implementation" / "config" / "canon_registry.json"

@dataclass
class ProtectedAsset:
    page_or_db_id: str
    url: str = ""
    allowed_approvers: List[str] = field(default_factory=list)  # emails or "human-root"
    promotion_rules: Dict[str, Any] = field(default_factory=lambda: {
        "require_human_root": True,
        "require_bullshit_pass": True,
        "require_ledger": True,
        "require_no_dlp_p0": True,
        "min_evidence_packs_for_rag": 1
    })
    status: str = "protected"  # protected / candidate_ok

@dataclass
class CanonRegistry:
    assets: Dict[str, ProtectedAsset] = field(default_factory=dict)  # key by id or url
    _dirty: bool = False

    def __post_init__(self):
        if REGISTRY_FILE.exists():
            try:
                data = json.loads(REGISTRY_FILE.read_text())
                for k, v in data.get("assets", {}).items():
                    self.assets[k] = ProtectedAsset(**v)
            except Exception:
                pass

    def is_protected(self, page_id: str, url: str = "") -> bool:
        return page_id in self.assets or url in {a.url for a in self.assets.values()}

    def get_asset(self, page_id: str, url: str = "") -> Optional[ProtectedAsset]:
        if page_id in self.assets:
            return self.assets[page_id]
        for a in self.assets.values():
            if a.url == url or page_id in a.url:
                return a
        return None

    def require_approval(self, page_id: str, url: str = "", checks: Optional[Dict[str, bool]] = None) -> (bool, str):
        asset = self.get_asset(page_id, url)
        if not asset:
            return True, "not protected (candidate ok)"
        checks = checks or {}
        rules = asset.promotion_rules
        if rules.get("require_human_root") and not checks.get("human_root_approved", False):
            return False, "human-root approval required for canon"
        if rules.get("require_bullshit_pass") and not checks.get("bullshit_passed", False):
            return False, "bullshit olympics pass required"
        if rules.get("require_ledger") and not checks.get("ledger_emitted", False):
            return False, "action ledger entry required"
        if rules.get("require_no_dlp_p0") and checks.get("dlp_p0_found", False):
            return False, "DLP P0 findings block canon"
        return True, "promotion checks passed"

    def add_protected(self, page_id: str, url: str = "", approvers: Optional[List[str]] = None, rules: Optional[Dict] = None):
        self.assets[page_id] = ProtectedAsset(
            page_or_db_id=page_id,
            url=url,
            allowed_approvers=approvers or ["human-root"],
            promotion_rules=rules or {}
        )
        self._dirty = True
        self.save()

    def save(self):
        if not self._dirty:
            return
        REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
        data = {"assets": {k: asdict(v) for k,v in self.assets.items()}, "updated": datetime.datetime.utcnow().isoformat()}
        REGISTRY_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
        self._dirty = False

# Global
DEFAULT_CANON_REGISTRY = CanonRegistry()

if __name__ == "__main__":
    reg = CanonRegistry()
    print("Protected count:", len(reg.assets))
    # Example bootstrap (user will populate real protected pages like North Star, specs)
    if not reg.is_protected("example-canon-page"):
        reg.add_protected("example-canon-page", url="https://notion.so/...", approvers=["human-root", "dave@..."])
    ok, msg = reg.require_approval("example-canon-page", checks={"human_root_approved": True, "bullshit_passed": True, "ledger_emitted": True, "dlp_p0_found": False})
    print("Promotion check:", ok, msg)
    reg.save()
    print("Registry saved to", REGISTRY_FILE)