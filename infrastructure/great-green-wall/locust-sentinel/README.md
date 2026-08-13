# LOCUST SENTINEL

**Great Green Wall Locust Telemetry & Early-Warning Module**  
Status: v0.1 deployed specification  
Scope: civilian environmental monitoring, restoration protection, and response coordination

## Mission

LOCUST SENTINEL provides a provenance-aware early-warning layer for Desert Locust and related swarm risks affecting Great Green Wall restoration assets.

It separates four states that must never be conflated:

1. **Habitat suitability** — rainfall, soil moisture, vegetation and weather indicate possible breeding conditions.
2. **Suspected swarm** — orbital or regional sensing produces an anomaly consistent with swarm-scale activity.
3. **Confirmed swarm** — drone, field-team, optical/acoustic sensor, or authoritative agency observation confirms locust presence.
4. **Confirmed impact** — measured damage or exposure to Great Green Wall assets is documented.

`habitat suitability != swarm confirmation != damage`

## Core Architecture

```text
Earth observation / weather / restoration telemetry
                  |
                  v
          Habitat-risk model
                  |
                  v
       Swarm-anomaly detector
                  |
                  v
     Drone / field verification
                  |
                  v
       Ground-node confirmation
                  |
                  v
  Response coordination + recovery
                  |
                  v
       Alexandria provenance graph
```

## Sensor Layers

### 1. Orbital wide-area layer

Ingest satellite-derived and authoritative products for:

- rainfall and precipitation anomalies
- soil moisture
- vegetation greenness / vegetation change
- land-surface temperature
- wind fields and likely migration corridors
- radar/SAR observations where useful
- restoration-plot condition and abrupt biomass loss

Satellites are treated primarily as **wide-area cueing systems**. Individual insects are below normal Earth-observation resolution; the goal is to identify habitat and swarm-scale anomalies that justify closer inspection.

### 2. Drone verification layer

Dispatch uncrewed civilian survey platforms to high-priority coordinates for:

- high-resolution optical imagery
- multispectral / thermal confirmation
- local wind and environmental measurements
- swarm-density estimation where feasible
- restoration-asset inspection

### 3. Ground confirmation layer

Low-cost Great Green Wall nodes can provide:

- optical insect counts
- acoustic activity sensing
- local weather
- soil moisture
- vegetation condition
- manual field observations

## Alexandria Evidence Model

Every alert is a typed claim with provenance.

```text
claim -> source scene / sensor record -> model version -> confidence
      -> verification task -> confirmation / rejection -> impact record
      -> response -> recovery outcome
```

Required status labels:

- `predicted`
- `suspected`
- `confirmed`
- `rejected`
- `impact-confirmed`
- `resolved`

Required evidence boundary:

> A favorable habitat signal is not evidence that a swarm exists. A suspected swarm is not evidence of damage. A model alert is not an authoritative field observation.

## Priority Score

Initial triage score:

```text
priority = habitat_risk
         * swarm_confidence
         * asset_exposure
         * vulnerability
         * verification_urgency
```

All factors must retain uncertainty and source provenance. No factor may be silently promoted from assumed to measured.

## Great Green Wall Asset Layer

Track at minimum:

- nurseries
- seed banks
- newly planted restoration plots
- mature restoration plots
- agroforestry zones
- water infrastructure
- food-production zones
- cold-storage / logistics nodes
- communications and power nodes

The system should favor **resilient restoration**, not maximum undifferentiated biomass. Diverse planting, distributed assets, seed reserves, and rapid recovery capacity reduce the probability that one biological event erases years of work.

## Response Policy

LOCUST SENTINEL is a detection, verification, and coordination system. Any pest-management action must comply with local law, ecological safeguards, public-health requirements, and authoritative agricultural guidance.

The module itself does not prescribe indiscriminate eradication or unvalidated acoustic/chemical interventions.

## Telemetry Metrics

- area under habitat watch
- suspected events / month
- confirmation precision and recall
- median time from orbital cue to field verification
- false-positive rate
- confirmed swarm density where available
- Great Green Wall hectares exposed
- measured biomass / crop loss
- response latency
- recovery time
- nursery / seed-bank survival
- cost per verified event
- data completeness / provenance completeness

## v0.1 Build Order

1. Connect authoritative locust, rainfall, vegetation, soil-moisture, and wind feeds.
2. Build a Great Green Wall geospatial asset registry.
3. Define Alexandria claim/event schema and provenance fields.
4. Implement habitat-risk heatmap generation.
5. Add suspected-swarm anomaly queue.
6. Define drone / field verification packet format.
7. Add ground-node observation ingestion.
8. Build confirmation/rejection workflow.
9. Add asset-exposure and recovery ledger.
10. Run historical backtests and report false positives/false negatives before operational reliance.

## v0.2 Targets

- multi-sensor fusion
- automated verification prioritization
- restoration-risk forecasting
- local-language field reporting
- cross-border event handoff
- recovery optimization
- integration with Regenerative Olympics stress testing

## Guardrails

- Satellite cue != confirmed locust event.
- Model confidence != ground truth.
- Alexandria edge != proof.
- Human / authoritative verification remains explicit.
- Preserve false positives and rejected hypotheses as training receipts.
- No hidden destructive action path.

## Canonical Loop

```text
ORBIT -> DETECT -> CUE -> VERIFY -> CONFIRM -> RESPOND -> RECOVER -> LEARN
```

**All telemetry enters. All evidence leaves intact. The restoration system learns.**
