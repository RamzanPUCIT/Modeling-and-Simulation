# Modeling and Simulation — Course Repository

A graduate-level Python repository for the **Modeling and Simulation** course.  
Each module introduces a core concept through clean, well-commented starter code designed to be beginner-friendly and suitable for an academic portfolio.

---

## 📚 Course Topics & Repository Structure

```
Modeling-and-Simulation/
├── 01_Basics/                   – Foundational mathematical tools
│   ├── line_from_two_points.py  – Slope, intercept, and line equation
│   └── xor_dataset.py           – XOR truth table & linear separability
│
├── 02_Linear_Models/            – Linear economic and algebraic models
│   └── demand_supply_equilibrium.py – Market equilibrium price & quantity
│
├── 03_Random_Numbers/           – Pseudo-random number generation
│   └── linear_congruential_generator.py – LCG algorithm (from scratch)
│
├── 04_Monte_Carlo/              – Probabilistic simulation methods
│   └── monte_carlo_pi.py        – Estimate π with random sampling
│
├── 05_Queuing_Theory/           – Waiting-line models
│   └── mm1_queue.py             – Discrete-event M/M/1 queue simulation
│
├── 06_Markov_Chains/            – Stochastic state-transition processes
│   └── markov_chain.py          – Weather model with steady-state analysis
│
└── 07_System_Dynamics/          – Continuous growth and feedback models
    └── growth_models.py         – Linear, exponential & logistic growth
```

---

## 🎯 Learning Goals

| # | Module | Key Concepts |
|---|--------|-------------|
| 1 | **Basics** | Coordinate geometry, datasets, linear separability |
| 2 | **Linear Models** | Supply-demand curves, simultaneous linear equations |
| 3 | **Random Numbers** | LCG recurrence, modular arithmetic, period, seed sensitivity |
| 4 | **Monte Carlo** | Random sampling, Law of Large Numbers, convergence rate |
| 5 | **Queuing Theory** | M/M/1 model, Poisson arrivals, Little's Law, server utilisation |
| 6 | **Markov Chains** | Transition matrices, steady-state distribution, memoryless property |
| 7 | **System Dynamics** | ODE solutions, carrying capacity, feedback loops |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher  
- Install dependencies (only the standard library is required; optional packages listed in `requirements.txt`):

```bash
pip install -r requirements.txt
```

### Running the Examples

Each script can be run directly:

```bash
# Basics
python 01_Basics/line_from_two_points.py
python 01_Basics/xor_dataset.py

# Linear Models
python 02_Linear_Models/demand_supply_equilibrium.py

# Random Numbers
python 03_Random_Numbers/linear_congruential_generator.py

# Monte Carlo
python 04_Monte_Carlo/monte_carlo_pi.py

# Queuing Theory
python 05_Queuing_Theory/mm1_queue.py

# Markov Chains
python 06_Markov_Chains/markov_chain.py

# System Dynamics
python 07_System_Dynamics/growth_models.py
```

---

## 🗂️ Module Descriptions

### 01 – Basics
Foundational tools needed throughout the course.

- **`line_from_two_points.py`** — Given two 2-D points, computes slope, y-intercept, and the line equation `y = mx + b`, then verifies by back-substitution.
- **`xor_dataset.py`** — Builds the canonical XOR truth table and demonstrates that XOR is *not* linearly separable, motivating the need for non-linear models.

### 02 – Linear Models
Algebraic and economic models expressed as linear equations.

- **`demand_supply_equilibrium.py`** — Models a linear market (`Qd = a − b·P`, `Qs = c + d·P`), solves for the equilibrium price and quantity, and simulates surplus/deficit across a price range.

### 03 – Random Numbers
How computers generate "random" numbers without true randomness.

- **`linear_congruential_generator.py`** — Implements the LCG formula `X_{n+1} = (a·X_n + c) mod m` from scratch, normalises to \[0, 1), and analyses basic statistics.

### 04 – Monte Carlo
Using randomness to approximate deterministic quantities.

- **`monte_carlo_pi.py`** — Estimates π by sampling random points in a square and counting those that fall inside the inscribed circle.  A convergence table shows how accuracy improves with sample size.

### 05 – Queuing Theory
Mathematical modelling of waiting lines.

- **`mm1_queue.py`** — Event-driven simulation of the M/M/1 queue (single server, Poisson arrivals, exponential service times).  Compares simulated metrics (mean wait, sojourn, queue length, utilisation) with theoretical M/M/1 formulas.

### 06 – Markov Chains
Stochastic processes with the memoryless property.

- **`markov_chain.py`** — Implements a 3-state weather Markov chain (Sunny / Cloudy / Rainy), simulates thousands of transitions, and empirically estimates the steady-state distribution.

### 07 – System Dynamics
Continuous-time models of growth, decay, and feedback.

- **`growth_models.py`** — Analytical solutions for linear growth (`N = N₀ + r·t`), exponential growth (`N = N₀·eʳᵗ`), and logistic growth (Verhulst model with carrying capacity K).

---

## 📦 Dependencies

All examples use only the **Python standard library** (`math`, `random`).  
Optional packages for plotting or extended analysis are listed in `requirements.txt`.

---

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in this repository.
