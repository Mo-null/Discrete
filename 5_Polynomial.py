def eval_poly(coeffs, n):
    result = 0
    power = len(coeffs) - 1  
    for coeff in coeffs:
        result += coeff * (n ** power)
        power -= 1
    return result

def get_coefficients():
    while True:
        try:
            coeffs = input("Enter coefficients (space-separated): ").strip()
            
            return list(map(int, coeffs.split()))
        except ValueError:
            print("Invalid coefficients. Please enter integers.\n")

def get_n_value():
    while True:
        try:
            return int(input("Enter value of n: "))
        except ValueError:
            print("Invalid n. Please enter an integer.\n")

def main():
    print("=== Polynomial Evaluator ===\n")
    while True:
        coefficients = get_coefficients()  
        n_value = get_n_value()           
        
        result = eval_poly(coefficients, n_value)
        print(f"\nP({n_value}) = {result}")
        
        if input("\nPress Enter to continue or 'q' to quit: ").strip().lower() == 'q':
            print("Goodbye!")
            break
        print("--------------------")

if __name__ == "__main__":
    main()
