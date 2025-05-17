from itertools import permutations, product

def generate_permutations(elements, allow_repetition=False, length=None):
    if not allow_repetition:
        elements = list(dict.fromkeys(elements))
    if length is None:
        length = len(elements)
    if not allow_repetition and length > len(elements):
        raise ValueError("Length cannot exceed number of unique elements when repetition=False")
    return list(product(elements, repeat=length)) if allow_repetition else list(permutations(elements, length))

def display_permutations(perms, repetition_mode):
    mode = "WITH" if repetition_mode else "WITHOUT"
    print(f"\nGenerating permutations {mode} repetition")
    print(f"Total permutations: {len(perms)}")
    print("All permutations:")
    for i, perm in enumerate(perms, 1):
        print(f"{i}. {perm}")  # Now showing as tuples

def main():
    print("Permutation Generator")
    print("Note: Enter 'y' for permutations WITH repetition (items can repeat)")
    print("      Enter 'n' for permutations WITHOUT repetition (all items unique)\n")
    
    try:
        elements = input("Enter elements separated by spaces: ").split()
        if not elements:
            raise ValueError("No elements entered")
        
        length = int(input("Enter length of permutations: "))
        repetition = input("Allow repetition? (y/n): ").strip().lower() == 'y'

        perms = generate_permutations(elements, repetition, length)
        display_permutations(perms, repetition)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
