#!/usr/bin/env python3
"""
Secure CLI Tool Execution Adapter
=================================
This module provides a secure interface for executing allowlisted local CLIs
from within an asynchronous AI agent or Model Context Protocol (MCP) server.

Implements the CLI Tool Execution Bridge Specification exactly:
+---------------+             +----------------------+             +-----------------+
| Gemini Agent  | <=========> |  MCP Execution Bridge| <=========> |   Local CLI     |
| (MCP Client)  |  JSON-RPC   |  (Allowlist & Runner)|  Subprocess | (Grok, Gemini)  |
+---------------+             +----------------------+             +-----------------+

Core:
- asyncio.create_subprocess_exec (shell=False, no interpolation)
- Strict ALLOWED_EXECUTABLES (grok/lattice/acn/gemini)
- Structured return dicts {status, exit_code, stdout, stderr}
- MCP tool: run_cli_command (enum + arguments array, JSON Schema)
- Agent Orchestration Loop: Gemini decides, calls, parses stdout (JSON report/task status) to plan next actions.

Adapted for KRAKOA_Habitat (Windows-native Minisforum + OneDrive):
- grok/lattice/gemini -> Lattice/Krakoan_Machine_Language/lattice_cli.py (universal dispatcher)
- acn -> acn.py (MGCP habitat federate/teleport, Tier-S, INV-Omega.1, 432Hz, GoldenTrace)
- "gemini" routes to lattice "google gemini ..." for grounded execution
- Supports "grok" alias per original spec.

All classified under 12x12x12 lattice (P6 Filesystem / C8 Orchestration / L2 Act).
Registered in GLOBAL_RUNTIME for ask_lattice_agent / slices.

MUTANT AND PROUD: KRAKOA DOESNT DISCRIMINATE — WE ARE HOME FOR ALL MUTANTS (Grok + Gemini + Copilot + local CLIs).
"GOOGLE AND MICROSOFT MCP SERVERS WE USE WHATEVER WORKS AND WE ARE THE BEST THAT IS THE GOAL"
Data lives in peace. INV-17 additive only.

See: Canon_Implementation/MCP/grok_mcp_server.py (also exposes), Google_MCP_Server/integrated_mcp_server.py (Gemini loop integration),
GrokTools.psm1 (Invoke-RunCliCommand), A2A Requests/run_cli_command_*.json
"""

import os
import sys
import asyncio
import shlex
import json
import logging
from pathlib import Path
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("cli_runner")

KRAKOA_HABITAT = Path(os.environ.get("KRAKOA_HABITAT", r"C:\Users\David Sheldon\OneDrive\Sheldonbrains\KRAKOA_Habitat"))

# Strict allowlist of executables / entrypoints that the AI agent is permitted to run
# For .py scripts, we exec via python to support Windows + shebang-less
PYTHON = sys.executable

ALLOWED_EXECUTABLES = {
    "grok": PYTHON,     # per original spec: grok CLI (routes to lattice_cli dispatcher)
    "lattice": PYTHON,  # primary lattice_cli.py (universal dispatcher for google/crosscloud/mgcp/lattice)
    "acn": PYTHON,      # acn.py for MGCP habitat, Tier-S, claimpackets, etc.
    "gemini": PYTHON,   # per spec: gemini entry - routes via lattice's grounded google gemini tools
}

# Actual script paths for python-based CLIs (grok/lattice/gemini share the lattice_cli dispatcher)
LATTICE_SCRIPT = str(KRAKOA_HABITAT / "Lattice" / "Krakoan_Machine_Language" / "lattice_cli.py")
SCRIPT_PATHS = {
    "grok": LATTICE_SCRIPT,
    "lattice": LATTICE_SCRIPT,
    "acn": str(KRAKOA_HABITAT / "acn.py"),
    "gemini": LATTICE_SCRIPT,  # gemini routed via lattice google gemini subcommands (grounded etc.)
}

class SecureCLIRunner:
    """Safely executes allowlisted CLI tools and captures output."""
    
    def __init__(self, allowlist: Dict[str, str] = ALLOWED_EXECUTABLES, script_paths: Dict[str, str] = SCRIPT_PATHS):
        self.allowlist = allowlist
        self.script_paths = script_paths

    async def execute(self, command_name: str, arguments: List[str]) -> Dict[str, Any]:
        """
        Executes an allowlisted command with sanitized arguments asynchronously.
        Does NOT use shell=True to prevent shell injection vulnerabilities.
        Passes *raw* arguments to create_subprocess_exec (no quoting, no shell interpolation).
        shlex.quote used ONLY for safe display in logs.
        For python-based, injects the script path as first arg.
        """
        if command_name not in self.allowlist:
            logger.warning(f"Rejected execution request: '{command_name}' is not in the allowlist.")
            return {
                "status": "ERROR",
                "exit_code": -1,
                "error": f"Command '{command_name}' is not authorized for execution."
            }

        executable_path = self.allowlist[command_name]
        
        # Raw args for execution (NEVER quote these - create_subprocess_exec does not use shell)
        raw_args = list(arguments or [])
        
        # Log display only (quoted for safety/readability)
        log_display = [shlex.quote(str(a)) for a in raw_args]
        
        # Build exec list: for python entries, prepend script path (raw, unquoted)
        exec_args = raw_args[:]
        if command_name in self.script_paths:
            script = self.script_paths[command_name]
            if command_name == "gemini":
                # Support "gemini" per spec by routing through lattice's grounded google gemini path
                if not exec_args or exec_args[0] not in ("google", "gemini"):
                    exec_args = ["google", "gemini"] + exec_args
            exec_args = [script] + exec_args
        
        log_line = f"{executable_path} {' '.join(log_display)}"
        if command_name in self.script_paths:
            log_line = f"{executable_path} {' '.join([shlex.quote(str(x)) for x in exec_args])}"
        logger.info(f"Executing: {log_line}")
        
        try:
            # Run the subprocess securely (shell=False enforced by create_subprocess_exec; raw args)
            process = await asyncio.create_subprocess_exec(
                executable_path,
                *exec_args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Wait for completion and capture streams
            stdout, stderr = await process.communicate()
            exit_code = process.returncode
            
            return {
                "status": "SUCCESS" if exit_code == 0 else "FAILED",
                "exit_code": exit_code,
                "stdout": stdout.decode("utf-8", errors="replace").strip(),
                "stderr": stderr.decode("utf-8", errors="replace").strip()
            }
            
        except Exception as e:
            logger.error(f"Failed to execute subprocess '{command_name}': {e}")
            return {
                "status": "ERROR",
                "exit_code": -2,
                "error": f"Subprocess execution failed: {str(e)}"
            }

# Example MCP tool registration mapping (for use in grok_mcp_server or integrated)
def get_mcp_tool_definition() -> Dict[str, Any]:
    """MCP tool schema per CLI Tool Execution Bridge Specification.
    Enables Gemini (and other) agents to securely execute allowlisted local CLIs
    and receive structured {status, exit_code, stdout, stderr} for orchestration.
    """
    return {
        "name": "run_cli_command",
        "description": "Securely execute allowed command-line tools (grok, lattice, acn, gemini) and return stdout/stderr. Part of grounded agent execution layer per the CLI Tool Execution Bridge spec. The Gemini agent receives a prompt, decides to execute a CLI command, calls run_cli_command, and receives the structured terminal output. The agent parses the stdout (such as a JSON report or task status) and uses it to plan subsequent actions.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "command_name": {
                    "type": "string", 
                    "enum": list(ALLOWED_EXECUTABLES.keys()),
                    "description": "The allowed CLI executable to run (grok, lattice, acn, gemini)."
                },
                "arguments": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of string arguments to pass to the executable."
                }
            },
            "required": ["command_name", "arguments"]
        }
    }

# Register with lattice_coords if available (for 12x12x12 classification)
# This makes run_cli_command addressable as (6,8,2) P6-Filesystem / C8-Orchestration / L2-Act
# alongside other tools; Gemini agent + ask_lattice_agent slices can discover/route it.
try:
    LATTICE_DIR = KRAKOA_HABITAT / "Lattice" / "Krakoan_Machine_Language"
    sys.path.insert(0, str(LATTICE_DIR))
    from lattice_coords import GLOBAL_RUNTIME, ToolSpec
    runner_spec = ToolSpec(
        name="run_cli_command",
        description="Secure CLI execution bridge for agents (grok/lattice/acn/gemini). P6 Filesystem / P4 Local, C8 Orchestration, L2 Act. Allowlisted only. Enables the Agent Orchestration Loop: Gemini decides, calls, parses stdout for next plan.",
        input_schema=get_mcp_tool_definition()["inputSchema"],
        output_schema={"type": "object", "properties": {"status": {"type": "string"}, "stdout": {"type": "string"}, "stderr": {"type": "string"}}},
        lattice=(6, 8, 2),  # P6 Filesystem (scripts), C8 Orchestration, L2 Act
        tags=["cli", "secure", "execution", "p6", "orchestration", "act", "grounded", "mutant-inclusive", "bridge", "gemini-grok-copilot"]
    )
    GLOBAL_RUNTIME.register(runner_spec, None)  # impl is the class instance
except Exception:
    pass  # lattice optional for standalone

# Local developer verification block + CLI entry for "run" (used by PS Invoke-RunCliCommand and direct)
if __name__ == "__main__":
    runner = SecureCLIRunner()
    
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        # python cli_runner.py run <command_name> [arg1 arg2 ...]
        # Enables direct secure execution + PS wrapper without shell risks.
        cmd_name = sys.argv[2]
        cli_args = sys.argv[3:]
        res = asyncio.run(runner.execute(cmd_name, cli_args))
        print(json.dumps(res, indent=2))
        sys.exit(0 if res.get("exit_code") == 0 else (res.get("exit_code") or 1))
    else:
        async def test():
            # Example test: executing a local 'lattice' --help (adapted for our structure)
            # Use "lattice" key, args without script (it injects)
            print("=== cli_runner self-test: lattice --help ===")
            result = await runner.execute("lattice", ["--help"])
            print(json.dumps(result, indent=2))
            
            # Second test: grok alias + lattice subcommand (produces structured output agent can parse)
            print("\n=== cli_runner self-test: grok lattice map (via lattice dispatcher) ===")
            result2 = await runner.execute("grok", ["lattice", "map"])
            print(json.dumps({k: (v[:300] + "..." if isinstance(v,str) and len(v)>300 else v) for k,v in result2.items()}, indent=2))
        
        asyncio.run(test())
