def eval_poly(coeffs, n, power=None):
    if power is None:
        power = len(coeffs) - 1  
    if not coeffs:
        return 0
    return coeffs[0] * (n ** power) + eval_poly(coeffs[1:], n, power - 1)

try:
    coefficients = list(map(int, input("Enter coefficients (highest degree first, space-separated): ").split()))
    n_value = int(input("Enter value of n: "))
    result = eval_poly(coefficients, n_value)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter integers only.")
