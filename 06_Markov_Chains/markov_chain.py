"""
Basic Markov Chain State Transition
=====================================
A Markov chain is a stochastic process where the next state depends only on the
current state (the Markov property / "memoryless" property).

It is described by:
  - A set of states  S = {s0, s1, …, sn}
  - A transition matrix  T  where  T[i][j] = P(next state = j | current state = i)
    (each row sums to 1)

Steady-state distribution π:
  After many transitions the system converges to a stationary distribution π
  where  π = π · T  (left eigenvector for eigenvalue 1).

Example: Weather model
  States: Sunny (0), Cloudy (1), Rainy (2)
  Transition probabilities are given in the matrix below.

Concepts covered:
  - Markov chains and transition matrices
  - Monte Carlo simulation of chain trajectories
  - Empirical vs. theoretical steady-state distributions
"""

import random


# ── Weather Markov Chain ───────────────────────────────────────────────────────
STATES = ["Sunny", "Cloudy", "Rainy"]

# T[i][j] = probability of moving from state i to state j
TRANSITION_MATRIX = [
    #  Sunny  Cloudy  Rainy
    [0.6,   0.3,    0.1],   # from Sunny
    [0.2,   0.4,    0.4],   # from Cloudy
    [0.1,   0.3,    0.6],   # from Rainy
]


def next_state(current_state_idx, transition_matrix, rng):
    """
    Sample the next state given the current state index.

    Parameters
    ----------
    current_state_idx  : int  – index of the current state
    transition_matrix  : list of lists of float – row-stochastic matrix
    rng                : random.Random instance

    Returns
    -------
    int – index of the next state
    """
    row = transition_matrix[current_state_idx]
    r = rng.random()
    cumulative = 0.0
    for j, prob in enumerate(row):
        cumulative += prob
        if r < cumulative:
            return j
    return len(row) - 1   # fallback for floating-point edge cases


def simulate_chain(initial_state_idx, n_steps, transition_matrix, seed=None):
    """
    Simulate a Markov chain for *n_steps* transitions.

    Parameters
    ----------
    initial_state_idx : int  – starting state index
    n_steps           : int  – number of transitions to simulate
    transition_matrix : list of lists of float
    seed              : int or None

    Returns
    -------
    list of int  – sequence of state indices (length n_steps + 1)
    """
    rng = random.Random(seed)
    trajectory = [initial_state_idx]
    for _ in range(n_steps):
        trajectory.append(next_state(trajectory[-1], transition_matrix, rng))
    return trajectory


def empirical_distribution(trajectory, n_states):
    """Return the fraction of time spent in each state."""
    counts = [0] * n_states
    for s in trajectory:
        counts[s] += 1
    total = len(trajectory)
    return [c / total for c in counts]


def validate_transition_matrix(matrix):
    """Check that each row sums to ~1."""
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        if abs(row_sum - 1.0) > 1e-9:
            raise ValueError(f"Row {i} sums to {row_sum:.6f}, expected 1.0")


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    validate_transition_matrix(TRANSITION_MATRIX)

    N_STEPS = 50_000
    SEED    = 7
    START   = 0   # start in Sunny state

    print("Basic Markov Chain – Weather Model")
    print("=" * 45)
    print("  States :", STATES)
    print("\n  Transition matrix (row = from, col = to):")
    header = "           " + "  ".join(f"{s:>8}" for s in STATES)
    print(header)
    for i, (state, row) in enumerate(zip(STATES, TRANSITION_MATRIX)):
        row_str = "  ".join(f"{p:>8.2f}" for p in row)
        print(f"  {state:<10} {row_str}")

    trajectory = simulate_chain(START, N_STEPS, TRANSITION_MATRIX, seed=SEED)

    # Print first 15 steps of the trajectory
    print(f"\n  First 15 states (starting from '{STATES[START]}'):")
    print("  " + " → ".join(STATES[s] for s in trajectory[:15]))

    # Empirical steady-state distribution
    emp_dist = empirical_distribution(trajectory, len(STATES))
    print(f"\n  Empirical steady-state distribution (after {N_STEPS:,} steps):")
    for state, freq in zip(STATES, emp_dist):
        bar = "█" * int(freq * 40)
        print(f"  {state:<10} {freq:.4f}  {bar}")

    print(
        "\n  (The empirical distribution approximates the theoretical steady-state π "
        "as N → ∞.)"
    )
