def is_complete_graph(adj_matrix):
    """Check if the adjacency matrix represents a complete graph."""
    n = len(adj_matrix)
    if n == 0:
        print("Empty graph is trivially complete.")
        return True
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != (0 if i == j else 1):
                return False
    return True

def input_adjacency_matrix(n):
    """Input an n x n adjacency matrix with 0/1 entries."""
    matrix = []
    print(f"Enter the {n}x{n} adjacency matrix (one row per line, space-separated):")
    for i in range(n):
        while True:
            row_input = input(f"Row {i+1}: ").strip()
            if not row_input:
                print("Error: Row cannot be empty. Try again.")
                continue
            elements = row_input.split()
            if len(elements) != n:
                print(f"Error: Expected {n} elements, got {len(elements)}. Try again.")
                continue
            try:
                row = [int(x) for x in elements]
                if any(x not in {0, 1} for x in row):
                    print("Error: Matrix entries must be 0 or 1. Try again.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: All elements must be integers. Try again.")
    return matrix

def main():
    print("==== Complete Graph Checker ====")
    while True:
        n_input = input("Enter number of vertices (n ≥ 0): ").strip()
        if not n_input:
            print("Error: Input cannot be empty.")
            continue
        try:
            n = int(n_input)
            if n < 0:
                print("Error: n cannot be negative.")
                continue
            break
        except ValueError:
            print("Error: Please enter an integer.")
    
    adj_matrix = input_adjacency_matrix(n)
    print("\nAdjacency Matrix:")
    for row in adj_matrix:
        print(" ".join(map(str, row)))
    
    if is_complete_graph(adj_matrix):
        print("\nResult: The graph is COMPLETE.")
    else:
        print("\nResult: The graph is NOT complete.")

if __name__ == "__main__":
    main()
