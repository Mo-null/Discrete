from itertools import product

def find_solutions(n, C):
    solutions = []
    for combo in product(range(C + 1), repeat=n):
        if sum(combo) == C:
            solutions.append(combo)
    return solutions

def main():
    while True:
        try:
            n = int(input("Enter the number of variables (n ≥ 1): "))
            if n < 1:
                print("Please enter a number ≥ 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            C = int(input("Enter the constant (0 ≤ C ≤ 10): "))
            if C < 0 or C > 10:
                print("Please enter a number between 0 and 10 (inclusive).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    solutions = find_solutions(n, C)
    print(f"\nTotal solutions: {len(solutions)}")
    for i, solution in enumerate(solutions, 1):
        equation = " + ".join(f"x{j+1}={val}" for j, val in enumerate(solution))
        print(f"{i}. {equation} = {C}")

if __name__ == "__main__":
    main()
