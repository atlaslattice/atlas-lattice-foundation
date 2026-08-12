"""REGEN OLYMPICS v0.6 — Generational Dream Team Evolution

Toy systems tournament / hypothesis generator. Not an empirical forecast.

Architecture:
- 512 worlds per generation
- 100 generations
- identical multi-stress screening
- specialist champions + modular Dream Team synthesis
- elite retention, crossover, mutation, and Dream Team injection
- Hall of Fame across generations

Core accounting:
P_t = P0 + K_t
S_t = d_t P_t
L_t = s S_t
I_t = (1-s) S_t
d_{t+1} = max(0, d_t - Phi(L_t))
K_{t+1} = max(0, K_t(1+rho-depreciation) + eta I_t)

All recovered surplus is reinvested.
"""
