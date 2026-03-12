# Aluminum OS

Constitutional governance substrate and agent runtime for the Universal Workspace CLI (`uws`).

## Files

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — v1.0 canonical specification (cross-document synthesis)
- [`KERNEL.md`](KERNEL.md) — Core kernel architecture specification  
- [`COPILOT-CLI-SPEC.md`](COPILOT-CLI-SPEC.md) — Alexandria / Microsoft provider spec + Constitutional First Principles

## Quick Start

```bash
# Core command grammar
alum <verb> <resource> [--provider google|microsoft|apple|android|chrome] [flags]

# Examples
alum mail send --to "alice@example.com" --subject "Hello"
alum drive list --provider microsoft
alum calendar create --ai "team sync tomorrow at 10am"
alum search "Q1 budget" --provider all
alum ai "summarize my unread emails"
```

## Source Repo

`splitmerge420/uws` (uws-universal branch) — Aluminum OS + Universal Workspace CLI
