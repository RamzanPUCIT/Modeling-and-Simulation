"""
Demand-Supply Equilibrium
==========================
This script models a simple linear market where demand decreases with price
and supply increases with price.  The equilibrium price and quantity are found
by solving the two linear equations simultaneously.

Economic model:
  Demand : Qd = a - b * P   (downward-sloping demand curve)
  Supply : Qs = c + d * P   (upward-sloping supply curve)

Equilibrium condition:  Qd = Qs
  ⟹  a - b*P = c + d*P
  ⟹  P* = (a - c) / (b + d)
  ⟹  Q* = a - b * P*

Concepts covered:
  - Linear equations and simultaneous solution
  - Basic economic supply-demand model
  - Numerical simulation of market equilibrium
"""


def equilibrium_price_and_quantity(a, b, c, d):
    """
    Compute equilibrium price P* and quantity Q*.

    Parameters
    ----------
    a : float – demand intercept  (Qd = a - b*P)
    b : float – demand slope      (must be > 0)
    c : float – supply intercept  (Qs = c + d*P)
    d : float – supply slope      (must be > 0)

    Returns
    -------
    P_star : float – equilibrium price
    Q_star : float – equilibrium quantity
    """
    if (b + d) == 0:
        raise ValueError("b + d must be non-zero to find equilibrium.")

    P_star = (a - c) / (b + d)
    Q_star = a - b * P_star
    return P_star, Q_star


def demand(a, b, price):
    """Return quantity demanded at a given price."""
    return a - b * price


def supply(c, d, price):
    """Return quantity supplied at a given price."""
    return c + d * price


def simulate_market(a, b, c, d, price_range):
    """
    Simulate the market over a range of prices and print demand vs. supply.

    Parameters
    ----------
    a, b     : demand parameters
    c, d     : supply parameters
    price_range : iterable of price values to evaluate
    """
    print(f"\n  {'Price':>8} | {'Demand':>8} | {'Supply':>8} | {'Surplus/Deficit':>16}")
    print("  " + "-" * 52)
    for P in price_range:
        Qd = demand(a, b, P)
        Qs = supply(c, d, P)
        balance = Qs - Qd
        label = f"{balance:+.2f}"
        print(f"  {P:>8.2f} | {Qd:>8.2f} | {Qs:>8.2f} | {label:>16}")


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Model parameters
    a = 100   # demand intercept
    b = 2     # demand slope
    c = 10    # supply intercept
    d = 3     # supply slope

    P_star, Q_star = equilibrium_price_and_quantity(a, b, c, d)

    print("Demand-Supply Equilibrium Model")
    print("=" * 45)
    print(f"  Demand function : Qd = {a} - {b}*P")
    print(f"  Supply function : Qs = {c} + {d}*P")
    print(f"\n  Equilibrium Price    : P* = {P_star:.4f}")
    print(f"  Equilibrium Quantity : Q* = {Q_star:.4f}")

    # Show market conditions at several price levels
    prices = [i for i in range(0, 25, 5)]
    simulate_market(a, b, c, d, prices)
    print(f"\n  → At P = {P_star:.2f}, surplus/deficit ≈ 0  (equilibrium).")
