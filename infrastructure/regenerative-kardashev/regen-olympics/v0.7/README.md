# REGEN OLYMPICS v0.7 — All Models Enter / All Models Leave / Dream Team

Status: **toy systems tournament / hypothesis generator, not an empirical Earth forecast**.

## Protocol

1. Every existing model enters intact.
2. Every model faces identical shocks and receives receipts.
3. No model is deleted or overwritten; every model leaves with its own scorecard.
4. Specialist traits are mapped across the full field.
5. Only after the field is complete is a new Dream Team synthesized.
6. Dream Team is a new model; it does not erase or replace its contributors.

## Core accounting

- `P_t = P0 + K_t`
- `S_t = d_t P_t`
- `L_t = s S_t`
- `I_t = (1-s) S_t`
- `d_{t+1} = max(0, d_t - Phi(L_t))`
- `K_{t+1} = max(0, K_t(1+rho-depreciation) + eta I_t)`

## Run

- Distinct entering models: **52**
- Best entrant: **v0.6 Gen100-15**
- Best entrant `R_J(250)`: **65,469.16**
- Best entrant modeled final capacity: **2,553,857 TW (~2.554 EW)**
- Dream Team winner: **Dream-198**
- Dream Team `R_J(250)`: **119,542.99**
- Dream Team modeled final capacity: **5,326,298 TW (~5.326 EW)**
- Dream Team remaining modeled drain: **7.076e-10**
- Dream Team median worst disruption: **0.678%**
- Dream Team collapse rate: **0%**

The Dream Team nearly doubled modeled final productive capacity and improved horizon-defined regenerative return by about 83% versus the strongest entrant. Its worst-disruption metric was modestly higher than the strongest entrant (0.678% vs. 0.502%). Normalized scores are field-relative; use absolute metrics for cross-field comparisons.

## Atlas Lattice boundary

`Atlas Lattice Architecture Proxy` entered as an **assumed architecture proxy**, not measured empirical performance. Future receipts integration should derive its parameters from measured module data.

## Raw artifact locations

Google Drive v0.7 folder:
https://drive.google.com/drive/folders/1OMpmq_dBzI4-qeTttAHRrCS98gC0Sm_A

Notion archive:
https://app.notion.com/p/3ba0c1de73d98122a63bd28712ef4d7e

Raw scoreboards / Dream candidates are retained in Drive; SHA-256 receipts are in `SHA256SUMS.txt` so the archived raw files can be verified byte-for-byte.
