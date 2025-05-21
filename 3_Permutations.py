from itertools import permutations, product

def generate_permutations(elements, allow_repetition=False, length=None):
    if not allow_repetition:
        elements = list(dict.fromkeys(elements))
    return list(product(elements, repeat=length)) if allow_repetition else list(permutations(elements, length))

def display_permutations(perms, repetition_mode):
    mode = "WITH" if repetition_mode else "WITHOUT"
    print(f"\nGenerating permutations {mode} repetition")
    print(f"Total permutations: {len(perms)}")
    print("All permutations:")
    for i, perm in enumerate(perms, 1):
        int_tuple = tuple(int(x) for x in perm) 
        print(f"{i}. {int_tuple}")

def main():
    print("=== Digit Permutation Generator ===")
    
    while True:
        elements = input("Enter digits (space-separated): ").split()
        if not elements:
            print("Error: No digits entered")
            continue
        if all(d.isdigit() and len(d) == 1 for d in elements):
            break
        print("Error: Only single digits (0-9) allowed")
    
    while True:
        try:
            length = int(input("Enter length of permutations: "))
            if length > 0: break
            print("Length must be positive")
        except ValueError:
            print("Please enter an integer")

    while True:
        repetition = input("Allow repetition? (y/n): ").lower()
        if repetition in ('y', 'n'):
            repetition = (repetition == 'y')
            break
        print("Please enter 'y' or 'n'")
    
    try:
        perms = generate_permutations(elements, repetition, length)
        display_permutations(perms, repetition)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
