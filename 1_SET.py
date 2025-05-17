class SET:
    def __init__(self, elements):
        self.elements = elements

    def is_member(self, element):
        return element in self.elements

    def powerset(self):
        elements = sorted(list(self.elements))
        power_set = [
            sorted({elements[j] for j in range(len(elements)) if (i & (1 << j))})
            for i in range(1 << len(elements))
        ]
        return sorted(power_set, key=lambda x: (len(x), x))

    def is_subset_of(self, set2):
        return self.elements.issubset(set2.elements)

    def union_intersection(self, set2):
        return (
            sorted(list(self.elements.union(set2.elements))),
            sorted(list(self.elements.intersection(set2.elements)))
        )

    def difference_operations(self, set2):
        return {
            'difference': sorted(list(self.elements.difference(set2.elements))),
            'symmetric_difference': sorted(list(self.elements.symmetric_difference(set2.elements)))
        }

    def complement(self, set2):
        return sorted(list(self.elements - set2.elements))

    def cartesian_product(self, set2):
        return sorted([(x, y) for x in sorted(self.elements) for y in sorted(set2.elements)])

def input_set():
    while True:
        try:
            elements = set(map(int, input("Enter set elements (space-separated): ").split()))
            print(f"Set: {sorted(elements)}")
            return elements
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def main():
    print("\n=== SET OPERATIONS ===")
    print("1. Check if element is in set")
    print("2. Generate power set")
    print("3. Check if subset")
    print("4. Union and intersection")
    print("5. Set complement (A - B)")
    print("6. Difference operations")
    print("7. Cartesian product")
    print("8. Exit")

    while True:
        choice = input("\nChoose operation (1-8): ").strip()

        if choice == '1':
            s = SET(input_set())
            x = int(input("Element to check: "))
            print(f"Result: {s.is_member(x)}")

        elif choice == '2':
            s = SET(input_set())
            print("Power set:", s.powerset())

        elif choice == '3':
            A = SET(input_set())
            B = SET(input_set())
            print("Is A a subset of B:", A.is_subset_of(B))

        elif choice == '4':
            A = SET(input_set())
            B = SET(input_set())
            union, intersection = A.union_intersection(B)
            print(f"Union: {union}\nIntersection: {intersection}")

        elif choice == '5':
            A = SET(input_set())
            B = SET(input_set())
            print("Complement:", A.complement(B))

        elif choice == '6':
            A = SET(input_set())
            B = SET(input_set())
            results = A.difference_operations(B)
            print("Difference (A - B):", results['difference'])
            print("Symmetric difference:", results['symmetric_difference'])

        elif choice == '7':
            A = SET(input_set())
            B = SET(input_set())
            print("Cartesian product:", A.cartesian_product(B))

        elif choice == '8':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-8.")

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
