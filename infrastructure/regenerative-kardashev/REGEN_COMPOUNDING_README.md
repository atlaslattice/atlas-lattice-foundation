# REGEN_COMPOUNDING — Regenerative Kardashev / Absurd Abundance

Status: toy systems model / hypothesis generator, not an empirical forecast.

## Core state variables

- `P_t`: productive capacity (TW)
- `ell_t`: liberated usable fraction of system throughput
- `eta`: conversion of reinvested surplus into added productive capacity
- `R_J(H)`: lifetime joule return over horizon H

## Core equations

Uncapped reinvestment:

`P_{t+1} = P_t * (1 + eta * ell_t)`

Rising leak closure:

`ell_{t+1} = min(ell_t + Delta_ell, ell_max)`

Horizon-aware regenerative return:

`R_J(H) = integral_0^H DeltaP(t) dt / E_reinvested`

## Baseline run

- P0 = 129 TW
- ell0 = 6.85%
- eta = 25%
- capped comparator ceiling = 2.2x P0
- absurd-abundance leak-closure gain = +0.05 percentage points/year
- ell_max = 50%
- horizon = 1,000 years

## Important correction

At eta=1, ell=6.85%, 100% reinvestment and 250 years, the uncapped equation yields about 2.0 zettawatts, not 2 exawatts.

## Interpretation boundary

The vertical long-horizon curve is not a physical prediction. It is a diagnostic showing that an uncapped exponential model eventually requires explicit physical constraints (matter, radiative flux, accessible volume, conversion speed, information limits, etc.).

## Files

- `regen_compounding.py` — model implementation
- `regen_compounding_results.csv` — checkpoint outputs
- `regen_compounding_trajectories.svg` — log-scale trajectory visualization
