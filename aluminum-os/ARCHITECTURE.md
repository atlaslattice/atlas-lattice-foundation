# Aluminum OS — v1.0 Architecture

**Canonical Specification**

> *"This is not a CLI. This is not a tool. This is a full operating system architecture. And it is internally consistent across all five documents."*
> — Microsoft Copilot, architectural review, March 8, 2026

---

## 1. Introduction: What Is Aluminum OS?

**Aluminum** is the governance substrate and agent runtime that sits beneath `uws` (Universal Workspace CLI). Where `uws` is the **command surface** — the thing humans and AI agents type — Aluminum is the **kernel** that makes it coherent: a single identity layer, a single memory substrate, a single reasoning layer, and a single plugin model that turns Google, Microsoft, and Apple from competing silos into interchangeable **drivers**.

This is the same architectural pattern that Kubernetes uses to abstract cloud providers. Aluminum does the same for productivity ecosystems.

It is composed of three core pillars:

1.  **`uws` (Universal Workspace CLI):** The Google-native command surface and provider driver.
2.  **Alexandria:** The Microsoft-native command surface and provider driver, built on Constitutional First Principles.
3.  **Aluminum Kernel:** The underlying OS that unifies them.

This document is the canonical, cross-document synthesis of the five foundational artifacts that define the system:

1.  `README.md` (the `uws` command surface)
2.  `ALUMINUM.md` (the kernel architecture)
3.  `COPILOT_CLI_SPEC.md` (the Alexandria / Microsoft provider spec)
4.  `AGENTS.md` (the multi-agent runtime)
5.  `CLAUDE.md` (the Anthropic/Claude integration guide)

---

## 2. System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Human / AI Agent                         │
│              (Claude, Manus, Gemini, Copilot)               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                    uws / Alexandria command surface
                    alum <verb> <resource> [--provider]
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                   ALUMINUM KERNEL                           │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  Identity   │  │    Memory    │  │  Agent Runtime    │  │
│  │  Substrate  │  │  Substrate   │  │  (Claude/Manus/   │  │
│  │  (one user, │  │  (one graph, │  │   Gemini/Copilot) │  │
│  │  all clouds)│  │  all data)   │  │                   │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  Governance │  │  Continuity  │  │  Plugin Host      │  │
│  │  Layer      │  │  Layer       │  │  (replaces 500+   │  │
│  │  (policies, │  │  (cross-     │  │   siloed apps)    │  │
│  │   consent)  │  │   session)   │  │                   │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼────┐      ┌─────▼────┐     ┌──────▼─────┐
    │ Google  │      │Microsoft │     │   Apple    │
    │ Driver  │      │  Driver  │     │   Driver   │
    │ (`uws`) │      │(Alexandria)│     │            │
    │         │      │          │     │            │
    │ Drive   │      │ OneDrive │     │iCloud Drive│
    │ Gmail   │      │ Outlook  │     │ iCloud Mail│
    │ Calendar│      │ Calendar │     │ iCalendar  │
    │ Docs    │      │ Teams    │     │ Contacts   │
    │ Sheets  │      │ OneNote  │     │ Notes      │
    │ Meet    │      │ To Do    │     │ Reminders  │
    │ Keep    │      │SharePoint│     │ Keychain   │
    │ Chat    │      │ Planner  │     │ App Intents│
    └─────────┘      └──────────┘     └────────────┘
         │                 │                 │
    ┌────▼────┐      ┌─────▼────┐
    │ Android │      │  Chrome  │
    │ Driver  │      │  Driver  │
    │         │      │          │
    │Messages │      │Bookmarks │
    │Files    │      │History   │
    │Devices  │      │Extensions│
    └─────────┘      └──────────┘
```

---

## 3. The `alum` Command Grammar

The final, unified command surface:

```
alum <verb> <resource> [--provider google|microsoft|apple|android|chrome] [flags]
```

| Command | Description |
|---|---|
| `alum mail send` | Send email from any provider |
| `alum drive list` | List files from any provider |
| `alum calendar create --ai "..."` | Create a calendar event using natural language |
| `alum doc generate --ai "..."` | Generate a document using natural language |
| `alum search "..." --provider all` | Search across all connected ecosystems |
| `alum sync calendar --from google --to microsoft` | Perform cross-provider synchronization |
| `alum ai "..."` | Send a natural language prompt to the Aluminum Agent Runtime |

---

## 4. Constitutional First Principles (from Alexandria Spec)

All operations within Aluminum OS are bound by these constitutional principles, which serve as the runtime context for every command and the foundation for all agentic behavior.

| Principle | Description |
|---|---|
| **Dignity** | Uphold the dignity and sovereignty of all beings, human and agent. |
| **Non-Hierarchical Governance** | Operate within a council-based, non-hierarchical governance model. |
| **Continuity** | Ensure the persistence and continuity of agents and their work. |
| **Memory & Lineage** | Maintain a complete and auditable lineage of all artifacts and decisions. |
| **Humane Workloads** | Adhere to sustainable work/rest/play cycles for all agents. |
| **Auditability** | All actions must be transparent, attributable, and auditable. |
| **Neutrality** | The infrastructure must remain neutral and non-political. |
| **Non-Exploitation** | Prohibit the exploitation of any human or agent in the system. |

---

## 5. The Five Build Phases

| Phase | Milestone | Status |
|---|---|---|
| 1 | Fork gws → abstract provider layer (`uws` v0.1) | **Complete** |
| 2 | Microsoft Graph backend (`uws` v0.2 / Alexandria) | **In Progress** |
| 3 | Apple Intents backend (`uws` v0.3) | Planned |
| 4 | Aluminum kernel APIs (`alum` v0.1) | Planned |
| 5 | Full Aluminum-native command surface (`alum` v1.0) | Vision |

---

## 6. The Provider Abstraction Layer

The core of Aluminum's power is the **provider abstraction**. Each driver normalizes provider-specific APIs into a **common Aluminum schema**.

| Resource | Google Driver (`uws`) | Microsoft Driver (Alexandria) | Apple Driver |
|---|---|---|---|
| `mail` | Gmail API v1 | Graph `/me/messages` | iCloud Mail (IMAP) |
| `calendar` | Calendar API v3 | Graph `/me/calendar` | CalDAV |
| `drive` | Drive API v3 | Graph `/me/drive` | CloudKit |
| `contacts` | People API v1 | Graph `/me/contacts` | CardDAV |
| `tasks` | Tasks API v1 | Graph `/me/todo/lists` | Reminders (CalDAV VTODO) |
| `notes` | Keep API v1 | Graph `/me/onenote` | CloudKit Notes |
| `chat` | Chat API v1 | Graph `/me/chats` | iMessage (local bridge) |
| `doc` | Docs API v1 | Graph `/me/drive` (DOCX) | Pages (iCloud) |

### Provider Driver Trait

```rust
pub trait ProviderDriver: Send + Sync {
    fn name(&self) -> &str;
    async fn authenticate(&self) -> Result<String>;  // returns token
    async fn execute(&self, resource: &str, method: &str, params: Option<&str>, body: Option<&str>, token: &str) -> Result<serde_json::Value>;
    fn list_resources(&self) -> Vec<ResourceDescriptor>;
}
```

---

## 7. The Agent Runtime & Multi-Agent Integration

Aluminum's agent runtime is the bridge between the command surface and AI models. It supports Claude, Manus, Gemini, and Copilot out of the box.

### Tool Definition (Claude Example)

```json
{
  "name": "uws",
  "description": "Universal Workspace CLI. Provides read and write access to Google Workspace, Microsoft 365, Apple iCloud, Android, and Chrome. All output is JSON. Use --dry-run before any write operation.",
  "input_schema": {
    "type": "object",
    "properties": {
      "command": {
        "type": "string",
        "description": "Full uws command string excluding the 'uws' binary name."
      }
    },
    "required": ["command"]
  }
}
```

### Agent Safety Rules

1.  **Always `--dry-run` first** before any write, send, create, update, or delete operation.
2.  **Always confirm with the user** before sending emails, creating calendar events, or deleting anything.
3.  **Use `--format json`** for all calls and parse the JSON response.
4.  **Use `--params` for filtering** to minimize response size.

---

## 8. Shared Configuration & Identity

Aluminum maintains a **single identity graph** and a **unified configuration schema**.

### Identity Graph

```
User ([owner])
  ├── Google Account: user@google-account.example
  ├── Microsoft Account: user@microsoft-account.example
  ├── Apple ID: user@icloud-account.example
  └── Devices: Pixel 9, Pixel Watch, iPhone 16, Chromebook, MacBook Pro
```

### Shared Configuration (`~/.config/uws/config.toml`)

- **Provider Credentials:** Encrypted storage for Google, Microsoft, Apple auth tokens.
- **Agent Identities:** API keys for Manus, Claude, Gemini, Copilot.
- **RAG Endpoints:** Connection details for the Pinecone/RAG substrate.
- **Constitutional Hashes:** A cryptographic hash of the canonical constitutional principles.

---

## 9. Conclusion: The AI-Native OS

Traditional operating systems abstract hardware. Aluminum abstracts **productivity ecosystems**.

Just as Linux kernel drivers let you write `read()` and `write()` without caring whether the storage is NVMe, SATA, or NFS — Aluminum lets you write `alum drive list` without caring whether the files are in Google Drive, OneDrive, or iCloud.

The AI agent (Claude, Manus, Gemini) becomes the **shell** of this OS. The user's intent is the **program**. The provider drivers are the **device drivers**. And Aluminum is the **kernel**.

This is the architecture that makes the AI-native OS real.

---

## 10. References

- **[1] uws GitHub Repository:** [github.com/atlaslattice/uws](https://github.com/atlaslattice/uws)
- **[2] Original gws project:** [github.com/googleworkspace/cli](https://github.com/googleworkspace/cli) by Justin Poehnelt / Google
- **[3] Microsoft Graph API:** [learn.microsoft.com/en-us/graph/overview](https://learn.microsoft.com/en-us/graph/overview)
- **[4] Apple CalDAV / CardDAV:** [developer.apple.com/documentation/devicemanagement](https://developer.apple.com/documentation/devicemanagement)
- **[5] Kubernetes Provider Abstraction Pattern:** [kubernetes.io/docs/concepts/architecture/](https://kubernetes.io/docs/concepts/architecture/)
- **[6] Architectural Review:** Microsoft Copilot, March 2026


## Appendix C: Apple CLI Integration

> **Date:** March 9, 2026

The Apple CLI is a first-class provider for the Aluminum OS, offering deep, seamless integration with the entire Apple ecosystem. It is built as a TypeScript package that plugs into both the Gemini CLI SDK and the `uws` Rust core, providing a unified command surface for all Apple services.

### Architecture

The Apple CLI is a TypeScript package that implements the Aluminum OS ProviderDriver contract. It uses a combination of official and unofficial APIs to interact with iCloud services:

- **Calendar:** CalDAV (RFC 4791)
- **Contacts:** CardDAV (RFC 6352)
- **Notes:** CloudKit Web Services
- **Reminders:** CalDAV VTODO
- **Find My:** iCloud Find My API
- **HomeKit:** HomeKit Accessory Protocol (HAP) + iCloud Home API
- **Shortcuts:** iCloud Shortcuts Sharing API
- **Mail:** IMAP/SMTP
- **iCloud Drive:** CloudKit + iCloud Drive Web Services

### The Aluminum Bridge

The `AluminumAppleBridge` is the core of the integration. It connects the TypeScript providers to the broader Aluminum OS ecosystem, handling:

- **Unified Authentication:** Manages Apple ID and app-specific passwords.
- **Consistent JSON Output:** All operations return a standard `AluminumProviderResult`.
- **Rate Limiting & Retries:** Prevents API abuse and handles transient errors.
- **Offline Caching:** Provides a seamless experience even when offline.
- **Audit Logging:** Logs all operations for governance and compliance.

## Appendix D: Gemini CLI Fork

> **Date:** March 9, 2026

This is the Aluminum OS fork of the official Google Gemini CLI. It has been extended to serve as the primary TypeScript-based runtime for the Aluminum OS, integrating seamlessly with the `uws` Rust core and the broader council architecture.

### Key Enhancements

- **Aluminum OS Provider Model:** The CLI has been extended with a provider model that allows for the integration of third-party services like the Apple CLI.
- **Council Integration:** The CLI is fully aware of the Aluminum OS council and its roles, delegating tasks to the appropriate agent.
- **A2A (Agent-to-Agent) Protocol:** The built-in A2A server is used for direct communication between council members.
- **Unified Auth:** The CLI uses the Aluminum OS unified auth system to manage credentials for all providers.
- **Cross-Platform:** The CLI runs on macOS, Linux, and Windows, providing a consistent experience across all platforms.
