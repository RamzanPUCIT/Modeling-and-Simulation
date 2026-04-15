"""
Growth Models: Linear, Exponential, and Logistic
==================================================
Three fundamental growth models used in system dynamics and population modelling:

1. Linear Growth
   N(t) = N0 + r * t
   - Population grows by a fixed amount each time step.
   - r = absolute growth rate (units per time).

2. Exponential Growth
   N(t) = N0 * e^(r * t)
   - Population grows proportionally to its current size.
   - r = relative (per-capita) growth rate.
   - Unrealistic long-term (no resource limits).

3. Logistic Growth (Verhulst model)
   N(t) = K / (1 + ((K - N0) / N0) * e^(-r * t))
   - Growth slows as population approaches carrying capacity K.
   - Widely used in ecology, epidemiology, and marketing.

Concepts covered:
  - Ordinary differential equations (analytic solutions)
  - System dynamics feedback loops
  - Carrying capacity and saturation effects
"""

import math


def linear_growth(N0, r, t):
    """
    Compute population at time *t* under linear growth.

    N(t) = N0 + r * t

    Parameters
    ----------
    N0 : float – initial population
    r  : float – absolute growth rate per unit time
    t  : float – time

    Returns
    -------
    float
    """
    return N0 + r * t


def exponential_growth(N0, r, t):
    """
    Compute population at time *t* under exponential growth.

    N(t) = N0 * exp(r * t)

    Parameters
    ----------
    N0 : float – initial population
    r  : float – per-capita growth rate
    t  : float – time

    Returns
    -------
    float
    """
    return N0 * math.exp(r * t)


def logistic_growth(N0, r, K, t):
    """
    Compute population at time *t* under logistic growth.

    N(t) = K / (1 + ((K - N0) / N0) * exp(-r * t))

    Parameters
    ----------
    N0 : float – initial population  (0 < N0 < K)
    r  : float – intrinsic growth rate
    K  : float – carrying capacity
    t  : float – time

    Returns
    -------
    float
    """
    if N0 <= 0:
        raise ValueError("Initial population N0 must be positive.")
    if K <= 0:
        raise ValueError("Carrying capacity K must be positive.")
    return K / (1 + ((K - N0) / N0) * math.exp(-r * t))


def print_growth_table(N0, r_lin, r_exp, r_log, K, time_points):
    """
    Print a comparison table of the three models at each time point.

    Parameters
    ----------
    N0        : float – initial population for all three models
    r_lin     : float – linear growth rate
    r_exp     : float – exponential growth rate
    r_log     : float – logistic growth rate
    K         : float – carrying capacity (for logistic)
    time_points : iterable of float
    """
    print(
        f"\n  {'Time':>6} | {'Linear':>12} | {'Exponential':>12} | {'Logistic':>12}"
    )
    print("  " + "-" * 52)
    for t in time_points:
        lin = linear_growth(N0, r_lin, t)
        exp = exponential_growth(N0, r_exp, t)
        log = logistic_growth(N0, r_log, K, t)
        print(f"  {t:>6.1f} | {lin:>12.2f} | {exp:>12.2f} | {log:>12.2f}")


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    N0    = 10.0    # initial population
    R_LIN = 5.0     # linear growth rate (units/time)
    R_EXP = 0.3     # exponential growth rate (per unit time)
    R_LOG = 0.5     # logistic growth rate (per unit time)
    K     = 200.0   # carrying capacity

    print("Growth Models: Linear, Exponential, and Logistic")
    print("=" * 55)
    print(f"  Initial population N0 = {N0}")
    print(f"  Linear rate           = {R_LIN} (units/time)")
    print(f"  Exponential rate r    = {R_EXP} (per unit time)")
    print(f"  Logistic rate r       = {R_LOG}, K = {K}")

    time_steps = list(range(0, 25, 2))   # t = 0, 2, 4, …, 24
    print_growth_table(N0, R_LIN, R_EXP, R_LOG, K, time_steps)

    # Summary at t = 20
    t_final = 20
    print(f"\n  Summary at t = {t_final}:")
    print(f"    Linear      : {linear_growth(N0, R_LIN, t_final):.2f}")
    print(f"    Exponential : {exponential_growth(N0, R_EXP, t_final):.2f}")
    print(f"    Logistic    : {logistic_growth(N0, R_LOG, K, t_final):.2f}  (cap = {K})")
    print(
        "\n  Observation: Logistic growth is bounded by K, while exponential\n"
        "  growth increases without limit."
    )
