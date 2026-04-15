"""
Monte Carlo Estimation of π
=============================
The Monte Carlo method uses random sampling to estimate mathematical quantities.
To estimate π we use the unit circle inscribed in a 2×2 square:

  - Sample random points (x, y) uniformly in [-1, 1] × [-1, 1].
  - A point is *inside* the circle if  x² + y² ≤ 1.
  - The ratio of points inside the circle to total points approximates π/4:
        π ≈ 4 × (points inside circle) / (total points)

As the number of samples increases, the estimate converges to the true value
of π (≈ 3.14159…) by the Law of Large Numbers.

Concepts covered:
  - Monte Carlo integration
  - Law of Large Numbers
  - Estimation error and convergence
"""

import math
import random


def estimate_pi(n_samples, seed=None):
    """
    Estimate π using the Monte Carlo circle method.

    Parameters
    ----------
    n_samples : int   – number of random points to generate
    seed      : int or None – random seed for reproducibility

    Returns
    -------
    pi_estimate : float
    n_inside    : int  – number of points that fell inside the circle
    """
    rng = random.Random(seed)
    n_inside = 0

    for _ in range(n_samples):
        x = rng.uniform(-1.0, 1.0)
        y = rng.uniform(-1.0, 1.0)
        if x * x + y * y <= 1.0:   # inside unit circle
            n_inside += 1

    pi_estimate = 4.0 * n_inside / n_samples
    return pi_estimate, n_inside


def convergence_table(sample_sizes, seed=None):
    """Print a table showing how the π estimate improves with more samples."""
    print(f"\n  {'Samples':>12} | {'π estimate':>12} | {'Error':>12}")
    print("  " + "-" * 42)
    for n in sample_sizes:
        pi_est, _ = estimate_pi(n, seed=seed)
        error = abs(pi_est - math.pi)
        print(f"  {n:>12,} | {pi_est:>12.6f} | {error:>12.6f}")


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    SEED = 2024

    print("Monte Carlo Estimation of π")
    print("=" * 45)
    print(f"  True value of π = {math.pi:.8f}")

    # Single estimate with a large number of samples
    n = 1_000_000
    pi_est, inside = estimate_pi(n, seed=SEED)
    error = abs(pi_est - math.pi)
    print(f"\n  Using {n:,} random points:")
    print(f"    Points inside circle : {inside:,}")
    print(f"    π estimate           : {pi_est:.6f}")
    print(f"    Absolute error       : {error:.6f}")

    # Convergence demonstration
    print("\n  Convergence table (seed fixed for reproducibility):")
    sizes = [100, 1_000, 10_000, 100_000, 1_000_000]
    convergence_table(sizes, seed=SEED)

    print(
        "\n  Observation: error decreases roughly as 1/√n (Monte Carlo convergence rate)."
    )
