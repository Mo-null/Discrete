from itertools import permutations, product

def generate_permutations(digits, allow_repetition=False, length=None):
    if not allow_repetition:
        digits = list(dict.fromkeys(digits))
    if length is None:
        length = len(digits)
    return list(product(digits, repeat=length)) if allow_repetition else list(permutations(digits, length))

def main():
    print("Permutation Generator")
    digits = input("Enter digits separated by spaces (e.g., 1 2 3): ").split()
    length = int(input("Enter length of permutations: "))
    repetition = input("Allow repetition? (y/n): ").strip().lower() == 'y'
    
    perms = generate_permutations(digits, repetition, length)
    
    print(f"\nTotal permutations: {len(perms)}")
    print("All permutations:")
    for i, perm in enumerate(perms, 1):
        print(f"{i}. {''.join(perm)}")

if __name__ == "__main__":
    main()
