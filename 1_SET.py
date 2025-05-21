class SET:
    def __init__(self, elements):
        self.elements = elements

    def is_member(self, element):
        return element in self.elements

    def powerset(self):
        elements = sorted(list(self.elements))
        power_set = [
            {elements[j] for j in range(len(elements)) if (i & (1 << j))}
            for i in range(1 << len(elements))
        ]
        return sorted(power_set, key=lambda x: (len(x), sorted(x)))

    def is_subset_of(self, set2):
        return self.elements.issubset(set2.elements)

    def union(self, set2):
        return self.elements.union(set2.elements)

    def intersection(self, set2):
        return self.elements.intersection(set2.elements)

    def difference(self, set2):
        return self.elements.difference(set2.elements)

    def symmetric_difference(self, set2):
        return self.elements.symmetric_difference(set2.elements)

    def complement(self, universal_set):
        return universal_set.elements.difference(self.elements)

    def cartesian_product(self, set2):
        return {(x, y) for x in self.elements for y in set2.elements}


def input_set():
    while True:
        try:
            elements = set(map(int, input("Enter set elements (space-separated integers): ").split()))
            print("Set entered: {" + ", ".join(map(str, sorted(elements))) + "}")
            return elements
        except ValueError:
            print("Invalid input! Please enter integers only.")


def display_set(set_data):
    sorted_elements = sorted(set_data)
    print("{" + ", ".join(map(str, sorted_elements)) + "}")


def main():
    print("\n=== SET OPERATIONS ===")
    print("1. Check if element is in set")
    print("2. Generate power set")
    print("3. Check if subset")
    print("4. Union and intersection")
    print("5. Complement (Universal Set - A)")
    print("6. Difference operations (A - B and symmetric difference)")
    print("7. Cartesian product")
    print("8. Exit")

    while True:
        choice = input("\nChoose operation (1-8): ").strip()

        if choice == '1':
            s = SET(input_set())
            while True:
                try:
                    x = int(input("Element to check: "))
                    print(f"Result: {s.is_member(x)}")
                    break
                except ValueError:
                        print("Invalid input! Please enter an integer.")

        elif choice == '2':
            s = SET(input_set())
            print("Power set:")
            for subset in s.powerset():
                display_set(subset)

        elif choice == '3':
            A = SET(input_set())
            B = SET(input_set())
            print("Is A a subset of B:", A.is_subset_of(B))

        elif choice == '4':
            A = SET(input_set())
            B = SET(input_set())
            print("Union:")
            display_set(A.union(B))
            print("Intersection:")
            display_set(A.intersection(B))

        elif choice == '5':
            print("(First define the Universal Set)")
            U = SET(input_set())
            A = SET(input_set())
            print("Complement (Universal Set - A):")
            display_set(A.complement(U))

        elif choice == '6':
            A = SET(input_set())
            B = SET(input_set())
            print("Difference (A - B):")
            display_set(A.difference(B))
            print("Symmetric difference (A Δ B):")
            display_set(A.symmetric_difference(B))

        elif choice == '7':
            A = SET(input_set())
            B = SET(input_set())
            print("Cartesian product:")
            cp = A.cartesian_product(B)
            for pair in sorted(cp):
                print(pair)

        elif choice == '8':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-8.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
