"""
Line from Two Points
=====================
Given two points on a 2D plane, this script computes the slope, y-intercept,
and equation of the straight line passing through them.

Concepts covered:
  - Slope formula: m = (y2 - y1) / (x2 - x1)
  - Intercept formula: b = y1 - m * x1
  - Line equation: y = m*x + b
"""


def line_from_two_points(x1, y1, x2, y2):
    """Return (slope, intercept) of the line through (x1,y1) and (x2,y2).

    Parameters
    ----------
    x1, y1 : float  – coordinates of the first point
    x2, y2 : float  – coordinates of the second point

    Returns
    -------
    slope     : float
    intercept : float
    """
    if x1 == x2:
        raise ValueError("x1 and x2 must be different (vertical line has no slope).")

    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept


def evaluate_line(slope, intercept, x):
    """Return y = slope * x + intercept."""
    return slope * x + intercept


def print_equation(slope, intercept):
    """Pretty-print the line equation."""
    sign = "+" if intercept >= 0 else "-"
    print(f"  y = {slope:.4f}x {sign} {abs(intercept):.4f}")


# ── Main demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Example: points (1, 2) and (4, 8)
    p1 = (1, 2)
    p2 = (4, 8)

    m, b = line_from_two_points(*p1, *p2)

    print("Line from Two Points")
    print("=" * 40)
    print(f"  Point 1 : {p1}")
    print(f"  Point 2 : {p2}")
    print(f"  Slope   : {m:.4f}")
    print(f"  Intercept: {b:.4f}")
    print("  Equation:")
    print_equation(m, b)

    # Verify that both original points satisfy the equation
    print("\nVerification:")
    for x, y in [p1, p2]:
        y_pred = evaluate_line(m, b, x)
        print(f"  x={x}  →  y_predicted={y_pred:.4f}  (actual={y})")
