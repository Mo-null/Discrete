from itertools import product

def find_solutions(n, C):
    solutions = []
    for combo in product(range(C + 1), repeat=n):
        if sum(combo) == C:
            solutions.append(combo)
    return solutions

def main():
    try:
        n = int(input("Enter the number of variables (n ≥ 1): "))
        C = int(input("Enter the constant (C ≤ 10): "))
    except ValueError:
        print("Error: n and C must be integers")
        return

    if n < 1:
        print("Error: n must be ≥ 1")
        return
    if C > 10:
        print("Error: C must be ≤ 10")
        return

    solutions = find_solutions(n, C)
    print(f"\nTotal solutions: {len(solutions)}")
    for i, solution in enumerate(solutions, 1):
        equation = " + ".join(f"x{j+1}={val}" for j, val in enumerate(solution))
        print(f"{i}. {equation} = {C}")

if __name__ == "__main__":
    main()
