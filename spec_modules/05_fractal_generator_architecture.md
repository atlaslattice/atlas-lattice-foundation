---
**Module:** Fractal Generator — Software Architecture
**Parent:** [Atlas Lattice Architecture Spec v3.0](../README.md)
**Version:** v3.0 — Baseline Locked — April 1, 2026
**Signatory:** Dave Sheldon, Framework Architect

---

## 6. The Fractal Generator — Software Architecture

### 6.1 Overview

`fractal_generator_v1.py` is the logic engine that takes a thermal map (Ironwood or any heat source) and generates the 3D voxel parameters for the Acoustic Control Unit.

**Author:** Gemini (Google), March 29, 2026
**Language:** Python 3.x + NumPy
**Status:** v1.1 — READY FOR ACU SIMULATION (full vector math merged, 43 segments compiled, DeepSeek acoustic validation pending)

### 6.2 Architecture

```
Thermal Map Input → Density Multiplier → Murray's Law Scaling → Recursive Bifurcation → ACU Voxel Output
     ↑                                                                                        ↓
FLIR CV Feedback ← Benchmark Data ← Thermal Test ← Manifold Print ← Resonance Lock-In ← ACU Phase Map
     ↑                                                                                        ↑
     └──────────── Hardware-to-Ledger (INV-12 proof) ──────────────── Acoustic Pinger ────────┘
```

Key classes and methods:

- `HTAM_Fractal_Generator` — Main generator class
  - `thermal_density_multiplier(x, y)` — Maps position on die to branching density based on proximity to 1,000W logic core center
  - `generalized_murrays_law(parent_area, parent_length)` — Applies 2^(-2/3) area scaling and 2^(-1/3) length scaling for non-circular cross-sections
  - `calculate_bifurcation_angles(parent_vector)` — ±37.47° optimal Murray deviation via 2D rotation matrices (v1.1, Gemini)
  - `get_cross_section_shape(channel_area)` — Rounded-square geometry: height = 0.8 × width, corner radius = 0.25 × width (v1.1, Gemini)
  - `generate_constructal_network(start_pos, current_vector, depth, area, length)` — Full recursive bifurcation with exact vector translations and variable depth controlled by thermal density map (v1.1)

### 6.3 Open Questions for DeepSeek Validation

1. **Minimum channel width:** Is 0.5mm achievable with acoustic standing wave confinement, or will the laser cure a puddle at that scale?
2. **Overhang angles:** What are the acoustic overhang limits for rectangular cross-sections in a HDPE/PET Trashium resin?
3. **Multi-frequency interference:** At what channel density do the superimposed acoustic fields start to destructively interfere, creating geometry errors?
4. **Basin wall reflections:** How do acoustic reflections off the stainless steel basin walls affect standing wave fidelity at the manifold edges?

---
