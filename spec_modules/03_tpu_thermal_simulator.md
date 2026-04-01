---
**Module:** TPU Thermal Simulator
**Parent:** [Atlas Lattice Architecture Spec v3.0](../README.md)
**Version:** v3.0 — Baseline Locked — April 1, 2026
**Signatory:** Dave Sheldon, Framework Architect

---

## 4. The TPU Thermal Simulator

We do not need an actual Ironwood TPU. We need its **thermal footprint**.

### 4.1 Design Concept

A **TPU Thermal Simulator** replicates the exact thermal load of a single Ironwood chip using commodity heating components. This sidesteps Google datacenter security protocols and multi-million-dollar TSMC wafer procurement entirely.

### 4.2 Bill of Materials

| Component | Specification | Quantity | Purpose |
|-----------|---------------|----------|---------|
| Copper heating block | 50mm × 50mm × 10mm, C101 OFHC copper | 1 | Thermal mass matching Ironwood die |
| Cartridge heaters | 1200W total capacity (4 × 300W, 6.35mm dia) | 4 | Replicate 1,000W logic core TDP |
| PID temperature controller | 0-1200W, K-type thermocouple input | 1 | Maintain stable thermal load |
| K-type thermocouples | Surface-mount, 0.5mm bead | 8 | 4 on heater block, 4 on manifold surface |
| Thermal paste | Arctic Silver 5 or equivalent | 1 tube | Interface between copper block and Trashium manifold |
| Compression plate | Aluminum, 60mm × 60mm × 5mm, 4× M4 standoffs | 1 | Clamp manifold to copper block |
| Coolant pump | 12V DC, 2-4 L/min, 2m head | 1 | Circulate coolant through manifold |
| Coolant reservoir | 1L capacity with fill port | 1 | Coolant supply |
| Silicone tubing | 6mm ID, 1m lengths | 2 | Inlet/outlet connections |
| Barb fittings | 6mm barb × M6 thread | 4 | Manifold and pump connections |
| FLIR thermal camera (or equivalent) | Minimum 160×120 resolution | 1 | Non-contact surface thermal mapping |
| Data logger | Multi-channel thermocouple input, USB | 1 | Record thermal performance data |
| Power supply | 48V DC, 30A (or bench supply) | 1 | Power for heaters |
| Power meter | Inline watt meter | 1 | Verify exact thermal load |

**Estimated BOM Cost:** $500-800 (all commodity parts, no custom fabrication)

### 4.3 Test Protocol

1. **Baseline:** Mount factory aluminum heatsink on thermal simulator. Run at 1,000W for 30 minutes. Record steady-state temperatures across all 8 thermocouples. Log thermal camera imagery.
2. **HTAM Test:** Replace aluminum heatsink with Trashium fractal manifold (first print). Same thermal load, same duration, same measurements.
3. **Iteration:** If hot spots appear, adjust fractal density parameters in ACU algorithm. Reprint (75 seconds). Retest. Document each version.
4. **Victory Condition:** Trashium manifold achieves equal or lower steady-state temperature than aluminum baseline under identical thermal load.

---
