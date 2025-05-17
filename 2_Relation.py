class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def is_reflexive(self):
        for i in range(self.size):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == 1:
                    for k in range(self.size):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    def classify(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return "Equivalence Relation"
        elif self.is_reflexive() and self.is_antisymmetric() and self.is_transitive():
            return "Partial Order Relation"
        return "None"


def main():
    print("=== Relation Matrix Analyzer ===")
    
    while True:
        try:
            n = int(input("Enter matrix size (n for nxn): ").strip())
            if n <= 0:
                print("Error: Size must be ≥1")
                continue
            break
        except ValueError:
            print("Error: Enter an integer")

    print(f"\nEnter {n} rows, each with {n} space-separated 0s and 1s:")
    rows = []
    for i in range(n):
        while True:
            row_input = input(f"Row {i+1}: ").strip()
            try:
                row = list(map(int, row_input.split()))
                if len(row) != n:
                    print(f"Error: Exactly {n} values required")
                    continue
                if not all(x in (0, 1) for x in row):
                    print("Error: Only 0s and 1s allowed")
                    continue
                rows.append(row)
                break
            except ValueError:
                print("Error: Use integers separated by spaces")

    rel = RELATION(rows)
    print("\n=== Analysis ===")
    print(f"Reflexive: {rel.is_reflexive()}")
    print(f"Symmetric: {rel.is_symmetric()}")
    print(f"Antisymmetric: {rel.is_antisymmetric()}")
    print(f"Transitive: {rel.is_transitive()}")
    print(f"\nClassification: {rel.classify()}")


if __name__ == "__main__":
    main()
