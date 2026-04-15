"""
Simple M/M/1 Queue Simulation
================================
An M/M/1 queue is the simplest queuing model:
  - Arrivals follow a Poisson process (inter-arrival times ~ Exponential(λ))
  - Service times follow an Exponential distribution (rate μ)
  - Single server, FIFO discipline

Key performance metrics (Little's Law and M/M/1 formulas):
  Traffic intensity  : ρ  = λ / μ        (must be < 1 for stability)
  Mean queue length  : Lq = ρ² / (1 - ρ)
  Mean system length : L  = ρ / (1 - ρ)
  Mean waiting time  : Wq = ρ / (μ - λ)
  Mean sojourn time  : W  = 1 / (μ - λ)

This script simulates the queue using an event-driven approach and compares
simulation results with the theoretical formulas.

Concepts covered:
  - Discrete-event simulation
  - Queuing theory (Kendall notation: M/M/1)
  - Validation against analytical solutions
"""

import random
import math


def mm1_simulation(arrival_rate, service_rate, n_customers, seed=None):
    """
    Simulate an M/M/1 queue for *n_customers* arrivals.

    Parameters
    ----------
    arrival_rate  : float – λ, mean arrivals per unit time
    service_rate  : float – μ, mean services per unit time
    n_customers   : int   – number of customers to simulate
    seed          : int or None

    Returns
    -------
    dict with simulation statistics:
      mean_wait        – average time a customer waits in queue
      mean_sojourn     – average total time in system (wait + service)
      mean_queue_len   – time-averaged number of customers in queue
      server_util      – fraction of time the server was busy
    """
    rng = random.Random(seed)

    # Generate inter-arrival and service times
    inter_arrivals = [rng.expovariate(arrival_rate) for _ in range(n_customers)]
    service_times  = [rng.expovariate(service_rate) for _ in range(n_customers)]

    # Event-driven simulation variables
    arrival_time   = 0.0  # arrival time of current customer
    server_free_at = 0.0  # when the server becomes free

    wait_times    = []
    sojourn_times = []
    busy_time     = 0.0

    for i in range(n_customers):
        arrival_time += inter_arrivals[i]

        # Customer waits if server is busy
        wait = max(0.0, server_free_at - arrival_time)
        service_start = arrival_time + wait
        departure_time = service_start + service_times[i]

        wait_times.append(wait)
        sojourn_times.append(departure_time - arrival_time)
        busy_time += service_times[i]

        server_free_at = departure_time

    total_time = arrival_time + max(0.0, server_free_at - arrival_time)
    server_util = busy_time / total_time if total_time > 0 else 0.0
    mean_wait = sum(wait_times) / n_customers
    mean_sojourn = sum(sojourn_times) / n_customers

    # Time-averaged queue length via Little's Law: Lq = λ * Wq
    mean_queue_len = arrival_rate * mean_wait

    return {
        "mean_wait":      mean_wait,
        "mean_sojourn":   mean_sojourn,
        "mean_queue_len": mean_queue_len,
        "server_util":    server_util,
    }


def mm1_theoretical(arrival_rate, service_rate):
    """
    Return the theoretical M/M/1 performance metrics.

    Parameters
    ----------
    arrival_rate : float – λ
    service_rate : float – μ

    Returns
    -------
    dict with theoretical values (None if ρ >= 1, i.e. unstable queue)
    """
    rho = arrival_rate / service_rate
    if rho >= 1.0:
        return {"rho": rho, "stable": False}

    return {
        "rho":            rho,
        "stable":         True,
        "mean_wait":      rho / (service_rate - arrival_rate),
        "mean_sojourn":   1.0 / (service_rate - arrival_rate),
        "mean_queue_len": rho ** 2 / (1 - rho),
        "server_util":    rho,
    }


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    LAMBDA = 4.0   # arrival rate (customers per minute)
    MU     = 6.0   # service rate (customers per minute)
    N      = 10_000
    SEED   = 42

    rho = LAMBDA / MU

    print("M/M/1 Queue Simulation")
    print("=" * 45)
    print(f"  Arrival rate λ  = {LAMBDA} customers/min")
    print(f"  Service rate μ  = {MU} customers/min")
    print(f"  Traffic intensity ρ = λ/μ = {rho:.4f}  ({'stable' if rho < 1 else 'UNSTABLE'})")
    print(f"  Simulating {N:,} customers …\n")

    sim   = mm1_simulation(LAMBDA, MU, N, seed=SEED)
    theory = mm1_theoretical(LAMBDA, MU)

    print(f"  {'Metric':<25} | {'Simulated':>12} | {'Theoretical':>12}")
    print("  " + "-" * 55)
    metrics = [
        ("Mean wait time (Wq)",    "mean_wait"),
        ("Mean sojourn time (W)",  "mean_sojourn"),
        ("Mean queue length (Lq)", "mean_queue_len"),
        ("Server utilisation (ρ)", "server_util"),
    ]
    for label, key in metrics:
        s = sim[key]
        t = theory[key]
        print(f"  {label:<25} | {s:>12.4f} | {t:>12.4f}")

    print("\n  (Simulated values converge to theory as N → ∞)")
