class RELATION:
    def __init__(self, matrix):
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix must be square.")
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
        is_equiv = self.is_reflexive() and self.is_symmetric() and self.is_transitive()
        is_partial_order = self.is_reflexive() and self.is_antisymmetric() and self.is_transitive()
        
        if is_equiv:
            return "Equivalence Relation"
        elif is_partial_order:
            return "Partial Order Relation"
        return "None"


def main():
    print("Enter the relation matrix (space-separated rows, e.g., '1 0 1' for a row):")
    rows = []
    while True:
        row_input = input(f"Row {len(rows) + 1} (or press Enter to finish): ").strip()
        if not row_input:
            break
        row = list(map(int, row_input.split()))
        rows.append(row)
    
    try:
        rel = RELATION(rows)
        print("\nRelation Matrix:")
        for row in rel.matrix:
            print(" ".join(map(str, row)))
        print("\nClassification:", rel.classify())
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
