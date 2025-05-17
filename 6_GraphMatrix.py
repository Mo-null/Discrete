def is_complete_graph(adj_matrix):
    n = len(adj_matrix)
    if n < 2:
        return True
    for i in range(n):
        for j in range(n):
            if i == j:
                if adj_matrix[i][j] != 0:
                    return False
            else:
                if adj_matrix[i][j] != 1:
                    return False
    return True

def input_adjacency_matrix(n):
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
