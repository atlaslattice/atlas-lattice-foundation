---
**Module:** Persistent Specialized Agents — Onboard AI
**Parent:** [Atlas Lattice Architecture Spec v3.0](../README.md)
**Version:** v3.0 — Baseline Locked — April 1, 2026
**Signatory:** Dave Sheldon, Framework Architect

---

### 8.4 Persistent Specialized Agents — Onboard AI (v1.3)

**Attribution:** Persistent Specialized Agent architecture — Gemini (Google), March 30, 2026. Resource efficiency modeling (persistent vs. event-driven) — Dave Sheldon, exhaustive comparative analysis confirming persistent agents are less resource-intensive than event-triggered models with superior results.

Instead of spinning up new model instances per task (event-driven, cold-start overhead on every trigger), Memphis Node Zero runs four always-on AI agents with persistent memory and local context. These agents maintain continuous state awareness of the campus, eliminating the repeated context-reconstruction cost of event-triggered architectures. Dave Sheldon's comparative modeling confirms this architecture is less resource-intensive and produces better optimization outcomes than event-driven alternatives.

**Agent 1: Waste-to-Resource Agent**

Continuously monitors every physical and digital exhaust stream on campus to identify new upcycling opportunities. Data sources: Shreddernaut sorting telemetry, water treatment plant effluent analysis, HTAM printer waste heat profiles, greenhouse nutrient runoff. The agent's persistent memory allows it to correlate patterns across days and weeks that event-triggered analysis would miss — for example, detecting that a specific waste plastic blend arriving on Tuesdays from a particular transfer station produces superior BAETA alloy properties.

- Interfaces with: Loop 3 (Replicator), Loop 1 (Watershed), Loop 4 (Thermal)
- Status: CONCEPTUAL — requires Shreddernaut fleet telemetry API + water plant sensor integration

**Agent 2: Local Joy / Flourishing Agent**

Tracks subjective community well-being alongside objective metrics, ensuring that campus outputs (strawberries, printed tools, jobs, cleaner water) actually serve local human needs rather than optimizing for spreadsheet metrics alone. Measurement methodology to be developed — potential data sources include community feedback mechanisms, local economic indicators, food access metrics, employment satisfaction surveys.

- Interfaces with: Loop 2 (Strawberry), Loop 6 (Human), constitutional invariant reporting
- Status: CONCEPTUAL — joy equation methodology under development (Dave Sheldon)
- **Note:** This is the most novel agent in the architecture. No existing AI system tracks community flourishing as a first-class optimization target. The measurement framework will be developed after the physical loops stabilize.

**Agent 3: ROI Maximizer Agent**

Runs continuous simulations to ensure the campus maintains compounding long-term profitability sufficient to self-fund expansion without external capital dependency. Interfaces with GPT's MER economic model (forthcoming: MER_Executive_Summary_v0.1.md) for compute cost optimization and with the self-funding flywheel (§8.3) for revenue projection.

- Interfaces with: Loop 5 (Hardware/Ground-Truth), §8.3 Self-Funding Flywheel, MER model
- Status: CONCEPTUAL — requires at least one revenue-generating loop operational for real data input

**Agent 4: Constitutional Audit Agent**

Enforces the global invariants (INV-1, INV-7, INV-12, INV-31) continuously rather than on triggered events. Reports transparently to the Atlas Lattice network. This is an evolution of the Hardware-to-Ledger Bridge (§5.3.4) from event-triggered proof generation to persistent compliance monitoring.

- Interfaces with: All six loops, Hardware-to-Ledger Bridge, Atlas Lattice network
- Status: CONCEPTUAL — builds on existing Hardware-to-Ledger Bridge (§5.3.4, PLANNED)
- **Architectural note:** The v1.0 Hardware-to-Ledger Bridge fires on successful benchmark events. The Constitutional Audit Agent wraps this in a persistent monitoring layer that also detects drift, degradation, and compliance gaps between benchmark events — catching problems the event model would miss.

**Stress Test Note (Claude):** The self-funding flywheel is the long-term vision. The near-term reality is that Loop 3 (materials) depends on Loop 1 (water) commissioning, Loop 2 (food) depends on Loop 1 nutrient recovery, and Loop 4 (power) depends on heat exchanger integration with Colossus. The dependency chain means the flywheel doesn't spin up all at once — it sequences. The v1.0 HTAM print (Sections 2-6) remains the first domino and is independent of the regenerative loops. Don't let the vision delay the proof-of-concept.
