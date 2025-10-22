# Trapezoidal rule for f(x) = x^2 from x=0 to x=2 with 4 trapezoids
def f(x):
    return x**2  # Our function

a, b = 0, 2  # Interval [0, 2]
n = 4  # Number of trapezoids
dx = (b - a) / n  # Width of each trapezoid

# Calculate x-values and corresponding y-values
x = [a + i * dx for i in range(n + 1)]  # x0, x1, ..., x4
y = [f(x_i) for x_i in x]  # f(x0), f(x1), ..., f(x4)

# Trapezoidal rule: (dx/2) * (y0 + 2*y1 + 2*y2 + 2*y3 + y4)
area = (dx / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])

print(f"Approximated area: {area:.4f}")
# Compare with exact integral (1/3)x^3 from 0 to 2 = 8/3 ≈ 2.6667
print(f"Exact area: {8/3:.4f}")