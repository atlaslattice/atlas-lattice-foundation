"""REGEN OLYMPICS v0.7 — ALL MODELS ENTER / ALL MODELS LEAVE / DREAM TEAM

Toy systems tournament / hypothesis generator. Not an empirical Earth forecast.

Protocol:
1. Every existing model enters intact.
2. Every model faces identical shocks and receives receipts.
3. No model is deleted or overwritten; every model leaves with its own scorecard.
4. Specialist traits are mapped across the full field.
5. Only after the field is complete is a new Dream Team synthesized.
6. Dream Team is a new model; it does not erase or replace its contributors.

Core accounting:
P_t = P0 + K_t
S_t = d_t P_t
L_t = s S_t
I_t = (1-s) S_t
d_{t+1} = max(0, d_t - Phi(L_t))
K_{t+1} = max(0, K_t(1+rho-depreciation) + eta I_t)
"""
