def input_graph():
    while True:
        try:
            num_vertices = int(input("Enter number of vertices (≥ 1): "))
            if num_vertices < 1:
                print("Error: Number of vertices must be ≥ 1.\n")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.\n")

    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    print(f"\nEnter edges as pairs of vertices (0 to {num_vertices-1}). Press Enter to finish:")
    print("Example: '0 1' means an edge between vertex 0 and 1.")
    
    while True:
        edge_input = input("Edge: ").strip()
        if not edge_input:
            break
        
        try:
            u, v = map(int, edge_input.split())
            if u < 0 or v < 0 or u >= num_vertices or v >= num_vertices:
                print(f"Error: Vertex indices must be between 0 and {num_vertices-1}.")
            elif u == v:
                print("Error: Self-loops (e.g., '0 0') violate the definition of a complete graph.")
            else:
                adj_matrix[u][v] = 1
                adj_matrix[v][u] = 1
        except ValueError:
            print("Error: Enter edges as two integers separated by a space (e.g., '0 1').")

    return adj_matrix

def is_complete_graph(adj_matrix):
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i == j:
                if adj_matrix[i][j] != 0:
                    return False
            elif adj_matrix[i][j] != 1:
                return False
    return True

def print_adj_matrix(adj_matrix):
    print("\nAdjacency Matrix:")
    for row in adj_matrix:
        print(row)

def main():
    print("=== Complete Graph Checker ===")
    adj_matrix = input_graph()
    print_adj_matrix(adj_matrix)
    if is_complete_graph(adj_matrix):
        print("\nThe graph is COMPLETE (all possible edges exist).")
    else:
        print("\nThe graph is NOT complete (missing edges).")

if __name__ == "__main__":
    main()
