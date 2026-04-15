import math
import random
from collections import deque

# =========================================================
# AI-852 / Computational Modelling
# Mid Prep - Combined Practical Code
# Covers major pre-mid concepts in one file
# =========================================================


# =========================================================
# 1. STATIC LINEAR MODEL: line from two points
# =========================================================
def line_from_two_points(x1, y1, x2, y2):
    """
    Returns slope m and intercept c for line y = mx + c
    """
    if x2 == x1:
        raise ValueError("Vertical line: slope is undefined.")
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return m, c


# =========================================================
# 2. DEMAND-SUPPLY EQUILIBRIUM (static model)
# Example:
# Qd = a - bP
# Qs = c + dP
# At equilibrium: Qd = Qs
# =========================================================
def demand_supply_equilibrium(a, b, c, d):
    """
    Solves:
    Qd = a - bP
    Qs = c + dP
    equilibrium when Qd = Qs
    """
    price = (a - c) / (b + d)
    quantity = a - b * price
    return price, quantity


# =========================================================
# 3. XOR CHECK
# XOR cannot be separated by a single straight line
# =========================================================
def xor_dataset():
    """
    Classic XOR dataset
    """
    X = [(0, 0), (0, 1), (1, 0), (1, 1)]
    y = [0, 1, 1, 0]
    return X, y


# =========================================================
# 4. LINEAR CONGRUENTIAL GENERATOR (LCG)
# X(i+1) = (a*X(i) + c) mod m
# R(i) = X(i)/m
# =========================================================
def lcg(seed, a, c, m, n):
    values = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        values.append(x / m)
    return values


# =========================================================
# 5. MONTE CARLO METHOD: estimate pi
# =========================================================
def monte_carlo_pi(num_points=10000):
    inside = 0
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / num_points


# =========================================================
# 6. MARKOV CHAIN
# next_state = current_state * P
# =========================================================
def markov_step(state_vector, transition_matrix):
    n = len(state_vector)
    next_state = [0.0] * n
    for j in range(n):
        for i in range(n):
            next_state[j] += state_vector[i] * transition_matrix[i][j]
    return next_state


def markov_n_steps(initial_state, transition_matrix, steps):
    state = initial_state[:]
    history = [state[:]]
    for _ in range(steps):
        state = markov_step(state, transition_matrix)
        history.append(state[:])
    return history


# =========================================================
# 7. SIMPLE M/M/1 QUEUE SIMULATION
# Arrival ~ exponential(lambda)
# Service ~ exponential(mu)
# =========================================================
def exp_random(rate):
    """
    Generates exponential random variable using inverse transform
    """
    u = random.random()
    return -math.log(1 - u) / rate


def simulate_mm1_queue(arrival_rate=5, service_rate=7, num_customers=20):
    """
    Basic M/M/1 queue simulation
    """
    arrival_times = []
    service_times = []
    service_start_times = []
    departure_times = []
    waiting_times = []
    system_times = []

    current_time = 0.0
    last_departure = 0.0

    for _ in range(num_customers):
        inter_arrival = exp_random(arrival_rate)
        current_time += inter_arrival
        arrival_time = current_time
        service_time = exp_random(service_rate)

        service_start = max(arrival_time, last_departure)
        departure = service_start + service_time
        waiting = service_start - arrival_time
        system_time = departure - arrival_time

        arrival_times.append(arrival_time)
        service_times.append(service_time)
        service_start_times.append(service_start)
        departure_times.append(departure)
        waiting_times.append(waiting)
        system_times.append(system_time)

        last_departure = departure

    avg_wait = sum(waiting_times) / num_customers
    avg_system = sum(system_times) / num_customers
    utilization = sum(service_times) / departure_times[-1] if departure_times[-1] > 0 else 0

    return {
        "arrival_times": arrival_times,
        "service_times": service_times,
        "service_start_times": service_start_times,
        "departure_times": departure_times,
        "waiting_times": waiting_times,
        "system_times": system_times,
        "average_waiting_time": avg_wait,
        "average_system_time": avg_system,
        "utilization": utilization,
    }


# =========================================================
# 8. CONTINUOUS TIME / SYSTEM DYNAMICS
# Linear Growth: x = a + kt
# Exponential Growth: x = a*e^(kt)
# Logistic-style discrete approximation
# =========================================================
def linear_growth(a, k, t_values):
    return [a + k * t for t in t_values]


def exponential_growth(a, k, t_values):
    return [a * math.exp(k * t) for t in t_values]


def logistic_growth_discrete(x0, r, K, steps):
    """
    Simple discrete logistic growth:
    x_next = x + r*x*(1 - x/K)
    """
    x = x0
    values = [x]
    for _ in range(steps):
        x = x + r * x * (1 - x / K)
        values.append(x)
    return values


# =========================================================
# 9. MAIN DEMO
# =========================================================
def main():
    print("=" * 60)
    print("MID PREP - MODELING AND SIMULATION COMBINED CODE")
    print("=" * 60)

    # -----------------------------------------------------
    # 1. Line from two points
    # -----------------------------------------------------
    print("\n1. LINE FROM TWO POINTS")
    x1, y1 = 2, 5
    x2, y2 = 3, 9
    m, c = line_from_two_points(x1, y1, x2, y2)
    print(f"Points: ({x1}, {y1}), ({x2}, {y2})")
    print(f"Line: y = {m:.2f}x + {c:.2f}")

    # -----------------------------------------------------
    # 2. Demand-supply equilibrium
    # Example:
    # Qd = 100 - 2P
    # Qs = 20 + 3P
    # -----------------------------------------------------
    print("\n2. DEMAND-SUPPLY EQUILIBRIUM")
    a, b, c_val, d = 100, 2, 20, 3
    eq_price, eq_quantity = demand_supply_equilibrium(a, b, c_val, d)
    print(f"Qd = {a} - {b}P")
    print(f"Qs = {c_val} + {d}P")
    print(f"Equilibrium Price = {eq_price:.2f}")
    print(f"Equilibrium Quantity = {eq_quantity:.2f}")

    # -----------------------------------------------------
    # 3. XOR dataset
    # -----------------------------------------------------
    print("\n3. XOR DATASET")
    X, y = xor_dataset()
    for xi, yi in zip(X, y):
        print(f"Input={xi}, Output={yi}")
    print("Note: XOR is not linearly separable.")

    # -----------------------------------------------------
    # 4. LCG random numbers
    # -----------------------------------------------------
    print("\n4. LCG RANDOM NUMBERS")
    lcg_values = lcg(seed=7, a=5, c=3, m=16, n=10)
    print("Generated values:")
    print([round(v, 4) for v in lcg_values])

    # -----------------------------------------------------
    # 5. Monte Carlo pi
    # -----------------------------------------------------
    print("\n5. MONTE CARLO PI ESTIMATION")
    pi_est = monte_carlo_pi(10000)
    print(f"Estimated pi = {pi_est:.5f}")

    # -----------------------------------------------------
    # 6. Markov chain
    # -----------------------------------------------------
    print("\n6. MARKOV CHAIN")
    transition_matrix = [
        [0.65, 0.28, 0.07],
        [0.15, 0.67, 0.18],
        [0.12, 0.36, 0.52],
    ]
    initial_state = [0.21, 0.68, 0.11]
    history = markov_n_steps(initial_state, transition_matrix, 5)
    for step, state in enumerate(history):
        rounded = [round(v, 4) for v in state]
        print(f"Step {step}: {rounded}")

    # -----------------------------------------------------
    # 7. Queue simulation
    # -----------------------------------------------------
    print("\n7. M/M/1 QUEUE SIMULATION")
    queue_result = simulate_mm1_queue(arrival_rate=5, service_rate=7, num_customers=20)
    print(f"Average Waiting Time = {queue_result['average_waiting_time']:.4f}")
    print(f"Average System Time  = {queue_result['average_system_time']:.4f}")
    print(f"Utilization          = {queue_result['utilization']:.4f}")

    # -----------------------------------------------------
    # 8. System dynamics
    # -----------------------------------------------------
    print("\n8. SYSTEM DYNAMICS")
    t_values = list(range(0, 6))
    lin_vals = linear_growth(a=10, k=3, t_values=t_values)
    exp_vals = exponential_growth(a=10, k=0.2, t_values=t_values)
    log_vals = logistic_growth_discrete(x0=5, r=0.4, K=100, steps=10)

    print("Linear growth values:")
    print([round(v, 4) for v in lin_vals])

    print("Exponential growth values:")
    print([round(v, 4) for v in exp_vals])

    print("Logistic growth values:")
    print([round(v, 4) for v in log_vals])

    print("\nDone. This single file covers major pre-mid practical ideas.")


if __name__ == "__main__":
    main()