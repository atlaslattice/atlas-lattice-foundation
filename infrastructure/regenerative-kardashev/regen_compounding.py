from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Config:
    P0_TW: float = 129.0
    liberated0: float = 0.0685
    eta: float = 0.25
    capped_multiple: float = 2.2
    liberated_growth_per_year: float = 0.0005
    liberated_max: float = 0.50

def conventional(cfg: Config, years: int) -> List[float]:
    """No cap; fixed liberated fraction. Same conversion efficiency every year."""
    P = cfg.P0_TW
    out = [P]
    for _ in range(years):
        P *= (1.0 + cfg.eta * cfg.liberated0)
        out.append(P)
    return out

def regenerative_capped(cfg: Config, years: int) -> List[float]:
    """100% surplus reinvestment with logistic diminishing returns."""
    P = cfg.P0_TW
    cap = cfg.P0_TW * cfg.capped_multiple
    out = [P]
    for _ in range(years):
        growth = cfg.eta * cfg.liberated0 * P * (1.0 - P / cap)
        P += growth
        out.append(P)
    return out

def absurd_abundance(cfg: Config, years: int) -> Dict[str, List[float]]:
    """
    100% surplus reinvestment; no productive-capacity ceiling.
    The liberated-surplus fraction rises as drains are progressively closed.
    The fraction itself remains bounded to [0, liberated_max] for accounting sanity.
    """
    P = cfg.P0_TW
    powers = [P]
    liberated = [cfg.liberated0]
    for t in range(years):
        l = min(cfg.liberated0 + cfg.liberated_growth_per_year * t,
                cfg.liberated_max)
        P *= (1.0 + cfg.eta * l)
        powers.append(P)
        liberated.append(min(cfg.liberated0 + cfg.liberated_growth_per_year * (t+1),
                              cfg.liberated_max))
    return {"power_TW": powers, "liberated_fraction": liberated}

def annualized_power_return(cfg: Config) -> float:
    """
    Dimensionless one-step power return:
    ΔP / P_reinvested = eta.
    """
    return cfg.eta

def joule_return_over_horizon(cfg: Config, horizon_years: float) -> float:
    """
    Simplified dimensionless energy return if one increment of productive
    capacity persists for `horizon_years` with no decay:
        R_J(H) ≈ eta * H
    This is a payback-style metric, not a full lifecycle model.
    """
    return cfg.eta * horizon_years
