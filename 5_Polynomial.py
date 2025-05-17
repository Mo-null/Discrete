def eval_poly(coeffs, x, power=None):
    if power is None:
        power = len(coeffs) - 1  # Highest degree first
    if not coeffs:
        return 0
    return coeffs[0] * (x ** power) + eval_poly(coeffs[1:], x, power - 1)

# Example: 4x² + 2x + 9 at x=5 → 119
print(eval_poly([4, 2, 9], 5))  # Output: 119
