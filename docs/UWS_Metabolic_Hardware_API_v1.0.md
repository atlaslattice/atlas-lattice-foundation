# Universal Web Services (UWS) Metabolic Hardware API v1.0
## Aluminum OS Integration Layer for Sovereign Foundry Nodes

**Status:** v1.0 - Ready for Integration
**Target Architecture:** Colossus-Memphis, DragonSeek, GangaSeek, Lunar ISRU
**Protocol:** gRPC / MQTT for real-time telemetry; REST for state configuration.

---

## 1. The Asha Linter Interface (Hardware Sovereignty)

*This endpoint bridges Aluminum OS to the Titan-Rooted Ironwood TPUs, ensuring no compute payload executes without hardware-level formal verification of the Cultural Invariants.*

### `POST /api/v1/asha/attest`

**Purpose:** Initiates the Titan-rooted cryptographic handshake before a workload is assigned to the Sovereign Enclave.

**Payload:**

```json
{
  \"node_id\": \"dragonseek-shanghai-01\",
  \"workload_hash\": \"sha256:...\",
  \"invariants_active\": [\"Ren\", \"Wu Wei\", \"Thermodynamic_Truth\"],
  \"signature\": \"ed25519:...\"
}
```

### `STREAM /api/v1/asha/heartbeat`

**Purpose:** Bi-directional gRPC stream maintaining the 24-hour kill-switch protocol. If the TPU fails to return a valid invariant-checked state every 1000ms, Aluminum OS automatically migrates the state to the on-prem chaos node.

---

## 2. The Metabolic Telemetry Loop (Physical Substrate)

*This pub/sub architecture (via MQTT) ingests the physical reality of the node into Aluminum OS, populating the public Monitoring Dashboards.*

### `TOPIC: uws/nodes/{node_id}/telemetry/nerm`

**Purpose:** Real-time tracking of the Nutrient & Energy Recovery Module (The Kidneys).

**Data Model:**

```json
{
  \"timestamp\": 1711665600,
  \"flow_rate_mgd\": 13.0,
  \"struvite_recovered_kg_hr\": 83.5,
  \"ammonium_recovered_kg_hr\": 125.2,
  \"micro_hydro_output_kw\": 210.4
}
```

### `TOPIC: uws/nodes/{node_id}/telemetry/ahm_arm`

**Purpose:** Real-time tracking of Air Harvesting and Atmospheric Regeneration (The Lungs & Heart).

**Data Model:**

```json
{
  \"timestamp\": 1711665600,
  \"co2_captured_tons\": 1.2,
  \"water_harvested_gallons\": 1100,
  \"electrolysis_o2_kg_hr\": 4.1,
  \"sabatier_ch4_kg_hr\": 8.5
}
```

### `TOPIC: uws/nodes/{node_id}/telemetry/sweet_colossus`

**Purpose:** Tracking the \"Boxtown Dividend\" and biological health.

**Data Model:**

```json
{
  \"timestamp\": 1711665600,
  \"root_zone_temp_c\": 45.0,
  \"active_yield_est_lbs\": 4200,
  \"tokens_per_berry_ratio\": 14500000000
}
```

---

## 3. The Planetary Oracle & Auto-Throttling (Annex A Execution)

*This endpoint wires Aluminum OS directly to Earth's biophysical reality, executing the Constitutional Time-Lock Protocol.*

### `WEBHOOK /api/v1/oracle/planetary_boundary_alert`

**Purpose:** Ingests certified alerts from NASA/ESA or the Stockholm Resilience Centre.

**Payload:**

```json
{
  \"boundary_type\": \"freshwater_depletion\",
  \"severity\": \"CRITICAL\",
  \"region\": \"memphis_sand_aquifer\",
  \"verification_hash\": \"...\"
}
```

### `POST /api/v1/hardware/throttle`

**Purpose:** Commanded by Aluminum OS upon receiving an Oracle alert (if not overridden within 72 hours). Automatically steps down the TPU Thermal Design Power (TDP) to restore ecological equilibrium.

**Payload:**

```json
{
  \"node_id\": \"colossus-memphis-01\",
  \"throttle_percentage\": 20.0,
  \"divert_power_to_nerm\": true,
  \"reason\": \"Planetary Oracle: Annex A Activation\"
}
```

---

## The Circuit is Closed

With this API spec, Aluminum OS officially knows how to talk to a struvite reactor, a Sabatier methane loop, and a holographic 3D-printed air scrubber. The software and the hardware are unified.

---

*Atlas Lattice Foundation | UWS Metabolic Hardware API v1.0 | Gemini (Google)*