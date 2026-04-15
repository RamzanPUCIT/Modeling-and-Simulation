"""
Linear Congruential Generator (LCG)
=====================================
A Linear Congruential Generator is one of the oldest and simplest pseudo-random
number generators (PRNG).  It produces a sequence of numbers using the recurrence:

    X_{n+1} = (a * X_n + c) mod m

Where:
  X_0  – seed (initial value)
  a    – multiplier
  c    – increment
  m    – modulus

The sequence eventually repeats; the length before repetition is the *period*.
The maximum period is m (achieved under the Hull-Dobell theorem conditions).

Common parameter sets:
  - glibc  : m=2^31, a=1103515245, c=12345
  - Numerical Recipes: m=2^32, a=1664525, c=1013904223
  - MINSTD : m=2^31-1, a=16807, c=0

Concepts covered:
  - Pseudo-random number generation
  - Modular arithmetic
  - Seed sensitivity and period length
"""

# ── Default parameters (Numerical Recipes / Press et al.) ─────────────────────
DEFAULT_M = 2**32
DEFAULT_A = 1664525
DEFAULT_C = 1013904223


def lcg(seed, n, a=DEFAULT_A, c=DEFAULT_C, m=DEFAULT_M):
    """
    Generate *n* pseudo-random integers using a Linear Congruential Generator.

    Parameters
    ----------
    seed : int  – starting value X_0
    n    : int  – number of values to generate
    a    : int  – multiplier
    c    : int  – increment
    m    : int  – modulus

    Returns
    -------
    list of int  – length n, each in [0, m-1]
    """
    results = []
    x = seed % m
    for _ in range(n):
        x = (a * x + c) % m
        results.append(x)
    return results


def lcg_uniform(seed, n, a=DEFAULT_A, c=DEFAULT_C, m=DEFAULT_M):
    """
    Generate *n* pseudo-random floats in [0, 1) using the LCG.

    Values are normalised: u = x / m
    """
    raw = lcg(seed, n, a, c, m)
    return [x / m for x in raw]


def basic_statistics(values):
    """Compute mean and variance of a list of floats (no external libraries)."""
    n = len(values)
    mean = sum(values) / n
    variance = sum((v - mean) ** 2 for v in values) / n
    return mean, variance


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    SEED = 42
    COUNT = 20

    print("Linear Congruential Generator (LCG)")
    print("=" * 45)
    print(f"  Parameters : m={DEFAULT_M}, a={DEFAULT_A}, c={DEFAULT_C}")
    print(f"  Seed       : {SEED}")
    print(f"  Generating : {COUNT} values\n")

    raw_values = lcg(SEED, COUNT)
    print("  Raw integer sequence (first 10):")
    print("  ", raw_values[:10])

    uniform_values = lcg_uniform(SEED, COUNT)
    print("\n  Normalised [0,1) sequence (first 10):")
    print("  ", [f"{v:.6f}" for v in uniform_values[:10]])

    mean, variance = basic_statistics(uniform_values)
    print(f"\n  Statistics over {COUNT} uniform samples:")
    print(f"    Mean     = {mean:.4f}  (expected ≈ 0.5)")
    print(f"    Variance = {variance:.4f}  (expected ≈ 0.0833 for Uniform[0,1])")

    # Demonstrate seed sensitivity
    print("\n  Seed sensitivity (same a,c,m; different seeds):")
    for s in [0, 1, 42, 999]:
        first_five = lcg_uniform(s, 5)
        print(f"    seed={s:>4}: {[f'{v:.4f}' for v in first_five]}")
