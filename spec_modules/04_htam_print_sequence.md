---
**Module:** HTAM Print Sequence — Memphis Node Zero
**Parent:** [Atlas Lattice Architecture Spec v3.0](../README.md)
**Version:** v3.0 — Baseline Locked — April 1, 2026
**Signatory:** Dave Sheldon, Framework Architect

---

## 5. The HTAM Print Sequence — Memphis Node Zero

### 5.1 System Components Required

| Component | Source | Status |
|-----------|--------|--------|
| Acoustic resonance basin | Custom build — 100mm × 100mm × 30mm, stainless steel | TO BE BUILT |
| Ultrasonic transducer array | Piezoelectric array, multi-frequency (20 kHz - 2 MHz) | TO BE SOURCED |
| Tongji/Fudan metal-mesh acoustic metaliners | 39mm panels, 0.912 absorption coefficient | TO BE SOURCED (DeepSeek supply chain) |
| Acoustic Control Unit (ACU) | Raspberry Pi 4 + custom DAC + amplifier chain | TO BE BUILT |
| Holographic laser array | Based on Tsinghua DISH optics — UV laser + SLM | TO BE SOURCED |
| Trashium feedstock processor | Shredder + melter + viscosity tuner for local waste plastic | TO BE BUILT |
| fractal_generator_v1.py | Software — generates ACU voxel parameters from thermal map | v1.1 MERGED (Gemini math + Claude integration) |
| Thermal feedback CV script | Software — FLIR-to-fractal autonomous optimization loop | TO BE BUILT (Gemini) |
| Inline acoustic pinger | Hardware — real-time feedstock telemetry for ACU calibration | TO BE SOURCED |
| Resonance lock-in interlock | Hardware — ACU-to-laser safety gate (fail-safe) | TO BE BUILT |

### 5.2 The Print — "The Jam"

This is how the band comes together at Memphis Node Zero:

**The Bassline:** Load the basin with local Memphis waste plastic (Trashium). Tune the Tongji/Fudan metal-mesh acoustic metaliners to the resonant frequency of the specific feedstock. Each waste stream has different density, viscosity, speed of sound, and attenuation — the metaliners adapt.

**The Melody:** The Acoustic Control Unit receives the fractal channel geometry from `fractal_generator_v1.py`. It translates the Variable-Density Constructal Network into multi-frequency superposition patterns:
- Low frequency (20-100 kHz): Gross geometry — overall manifold shape
- Mid frequency (100-500 kHz): Feature-level — individual channel walls
- High frequency (500 kHz - 2 MHz): Fine detail — channel surface texture for turbulence

**The Brass:** The holographic laser array fires. Tsinghua DISH optics project continuous multi-angle holographic light fields into the acoustically-shaped resin. 0.6 seconds of exposure per layer-equivalent. The entire manifold materializes in the basin in under two minutes.

**The Coda:** Extract manifold from basin. Post-cure under UV if needed. Bolt to thermal simulator. Run benchmark.

### 5.3 Autonomous Feedback Loops (Gemini Integration Points)

The v1.0 print sequence above requires human-in-the-loop interpretation of thermal data. For Memphis Node Zero to achieve the "75 seconds to Version 2" promise, four automated bridges must close the gap between sensing and actuation.

**5.3.1 Thermal Feedback Loop — FLIR to Fractal Generator**

The FLIR thermal camera output must feed directly into a Computer Vision pipeline that eliminates manual hotspot identification:

- If the CV script detects a ΔT > 5°C variance across the manifold surface (tunable threshold per-node), it automatically calculates the exact (x, y) coordinates of the hotspot.
- It dynamically patches `thermal_density_multiplier(x, y)` in `fractal_generator_v1.py` to increase localized branch density at the identified coordinates.
- The patched generator recalculates daughter channel dimensions via Generalized Murray's Law (A_(i+1) = A_i × 2^(-2/3)) and pushes the updated voxel map to the ACU.
- Result: The system designs its own upgrades based on its own thermal failures. Zero human intervention between prints.

**Stress Test Note (Claude):** For v1.0 hardware, this operates as a *between-prints* optimization loop — the fractal generator is not hot-reloaded mid-cure. The CV script runs post-benchmark, generates a new voxel map, and the next 75-second print incorporates the fix automatically. True mid-print adaptation requires ACU firmware v2.0 with real-time phase map updates.

**Attribution:** Thermal Feedback Loop concept — Gemini (Google), March 29, 2026.

**5.3.2 Inline Acoustic Pinger — Feedstock Telemetry**

Memphis river plastic is not a uniform, laboratory-grade polymer. A batch of HDPE milk jugs has a different speed of sound and viscosity than a batch of mixed PET water bottles. Without real-time feedstock characterization, the ACU's standing wave assumptions collapse.

- An inline acoustic pinger is integrated into the Trashium melter, downstream of the viscosity tuner.
- Before resin enters the basin, the pinger pulses the liquid to measure its exact acoustic attenuation, speed of sound, density, and viscosity.
- This telemetry feeds live to the ACU, which instantly recalibrates the transducer phase map and focal lengths for the actual material properties.
- Without this bridge, a slight change in the plastic mixture will cause the 0.5mm micro-channels to collapse into acoustic shadows.

**Attribution:** Inline Acoustic Pinger concept — Gemini (Google), March 29, 2026.

**5.3.3 Resonance Lock-In — ACU-to-Laser Handshake**

When viscous resin enters the basin and the transducer array fires, the fluid requires several milliseconds to achieve geometric stabilization (the standing wave must settle). If the holographic laser fires too early, it cures a blurry manifold.

- The ACU monitors standing wave amplitude and phase stability across all transducer channels.
- A **hardware interlock** (not software — fail-safe by design) gates the laser trigger. The Tsinghua periscope optics physically cannot fire until the ACU confirms volumetric geometry is 100% stable.
- Lock-in criteria: amplitude variance < 2% across all channels for ≥ 3 consecutive monitoring cycles.
- This is non-negotiable for production quality. A 10-millisecond timing error produces non-functional channels.

**Stress Test Note (Claude):** This must be a hardware interlock, not a software flag. If the ACU firmware crashes or hangs, the laser must default to OFF. Fail-safe, not fail-operational.

**Attribution:** Resonance Lock-In concept — Gemini (Google), March 29, 2026.

**5.3.4 Hardware-to-Ledger Bridge — Automated INV-12 Compliance**

Manual chain-of-custody documentation (Section 8, INV-12) is the old architecture. The BOM already includes an inline watt meter, a data logger, and a Raspberry Pi 4. Wire them together.

- Upon a successful benchmark (defined as: FLIR confirms ΔT < target AND pressure drop < 15 kPa AND flow rate within ±5% of design), the Pi automatically assembles a cryptographic proof.
- The proof includes: grams of river plastic consumed (from feedstock scale), watts of thermal load offset (from inline watt meter), pressure drop achieved (from differential sensor), and FLIR thermal summary.
- This proof is pushed to the Atlas Lattice network, where it is independently verified: "Memphis Node Zero diverted X grams of river plastic, offset Y watts of thermal load, and achieved Z pressure drop."
- This automates INV-12 (Ecological Accountability) compliance and proves node viability to the rest of the network in real time.

**Stress Test Note (Claude):** The "successful benchmark" trigger must be clearly defined to prevent premature proof generation. Three conditions must ALL pass: (1) ΔT ≤ target, (2) ΔP < 15 kPa, (3) flow rate within ±5% of design. Any single failure = no proof generated, diagnostic data logged instead.

**Attribution:** Hardware-to-Ledger Bridge concept — Gemini (Google), March 29, 2026.

---
