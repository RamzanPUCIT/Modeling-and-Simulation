"""
XOR Dataset Demonstration
==========================
The XOR (exclusive-or) dataset is a classic example that shows why a single
straight line (linear model) cannot separate all classes – motivating the need
for non-linear models and multi-layer networks.

Truth table for XOR:
  Input A | Input B | Output (A XOR B)
  --------|---------|----------------
    0     |   0     |       0
    0     |   1     |       1
    1     |   0     |       1
    1     |   1     |       0

Concepts covered:
  - Creating a simple labelled dataset by hand
  - Understanding linear separability
  - Checking XOR with Python's bitwise operator (^)
"""


def build_xor_dataset():
    """Return the four XOR input-output pairs as a list of (A, B, label)."""
    dataset = []
    for a in [0, 1]:
        for b in [0, 1]:
            label = a ^ b          # Python bitwise XOR operator
            dataset.append((a, b, label))
    return dataset


def print_truth_table(dataset):
    """Display the XOR truth table in a formatted way."""
    print(f"  {'Input A':>8} | {'Input B':>8} | {'A XOR B':>8}")
    print("  " + "-" * 33)
    for a, b, label in dataset:
        print(f"  {a:>8} | {b:>8} | {label:>8}")


def is_linearly_separable(dataset):
    """
    Attempt a brute-force check: try every axis-aligned decision boundary.
    For the XOR problem this always returns False, illustrating that XOR
    cannot be separated by a single line.
    """
    # A proper check would involve linear programming; here we demonstrate
    # the concept by showing that class-0 and class-1 points overlap in
    # both x and y projections.
    class0 = [(a, b) for a, b, label in dataset if label == 0]
    class1 = [(a, b) for a, b, label in dataset if label == 1]

    # XOR class-0 points: (0,0) and (1,1) – they appear at both low and high x/y
    # XOR class-1 points: (0,1) and (1,0) – they also span both axes
    # No single line can separate them → not linearly separable
    x0 = {a for a, _ in class0}
    x1 = {a for a, _ in class1}
    return x0.isdisjoint(x1)   # False for XOR


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    dataset = build_xor_dataset()

    print("XOR Dataset Demonstration")
    print("=" * 40)
    print_truth_table(dataset)

    separable = is_linearly_separable(dataset)
    print(f"\n  Linearly separable? → {separable}")
    print(
        "\n  Explanation: XOR outputs 1 when inputs DIFFER and 0 when they MATCH.\n"
        "  No single straight line can divide the two classes, which is why\n"
        "  non-linear models (e.g., neural networks) are needed for XOR.\n"
    )
