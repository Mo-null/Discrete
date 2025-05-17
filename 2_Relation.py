class RELATION:
    def __init__(self, matrix):
        if not all(len(row) == len(matrix) for row in matrix):
            raise ValueError("Matrix must be square")
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
    print("Enter square relation matrix (one row per line, 0s and 1s):")
    rows = []
    while True:
        row_input = input(f"Row {len(rows)+1}: ").strip()
        if not row_input and len(rows) > 0:
            break
        try:
            row = list(map(int, row_input.split()))
            if not all(x in (0,1) for x in row):
                print("Error: Only 0s and 1s allowed")
                continue
            rows.append(row)
        except ValueError:
            print("Error: Use space-separated integers")

    try:
        rel = RELATION(rows)
        print("\nClassification:", rel.classify())
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
