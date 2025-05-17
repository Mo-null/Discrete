from itertools import product

def find_solutions(n, C):
    solutions = []
    for combo in product(range(C + 1), repeat=n):
        if sum(combo) == C:
            solutions.append(combo)
    return solutions

def main():
    n = int(input("Enter the number of variables (n): "))
    C = int(input("Enter the constant (C <= 10): "))
    
    if C > 10:
        print("Error: C must be ≤ 10")
        return
    
    solutions = find_solutions(n, C)
    
    print(f"\nTotal solutions: {len(solutions)}")
    print("All solutions:")
    for i, solution in enumerate(solutions, 1):
        print(f"{i}. {solution}")

if __name__ == "__main__":
    main()
