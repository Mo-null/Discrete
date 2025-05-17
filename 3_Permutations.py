from itertools import permutations, product

def generate_permutations(elements, allow_repetition=False, length=None):
    if not allow_repetition:
        elements = list(dict.fromkeys(elements))
    if length is None:
        length = len(elements)
    if not allow_repetition and length > len(elements):
        raise ValueError("Length cannot exceed number of unique elements when repetition=False")
    return list(product(elements, repeat=length)) if allow_repetition else list(permutations(elements, length))

def display_permutations(perms):
    print(f"\nTotal permutations: {len(perms)}")
    for i, perm in enumerate(perms, 1):
        print(f"{i}. {''.join(perm)}")

def main():
    print("Permutation Generator")
    try:
        elements = input("Enter elements separated by spaces: ").split()
        if not elements:
            raise ValueError("No elements entered")
        
        length = int(input("Enter length of permutations: "))
        repetition = input("Allow repetition? (y/n): ").strip().lower() == 'y'

        perms = generate_permutations(elements, repetition, length)
        display_permutations(perms)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
