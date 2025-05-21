from collections import defaultdict

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

    adj_list = defaultdict(list)
    print(f"\nEnter edges as pairs of vertices (0 to {num_vertices-1}). Press Enter to finish:")
    print("Example: '0 1' means an edge between vertex 0 and 1.")

    while True:
        edge_input = input("Edge: ").strip()
        if not edge_input:
            break
        try:
            u, v = map(int, edge_input.split())
            if u == v:
                print("Error: Self-loops (e.g., '0 0') violate the definition of a complete graph.")
            elif u < 0 or v < 0 or u >= num_vertices or v >= num_vertices:
                print(f"Error: Vertex indices must be between 0 and {num_vertices-1}.")
            elif v in adj_list[u]:
                print("Error: Duplicate edges are not allowed.")
            else:
                adj_list[u].append(v)
                adj_list[v].append(u)
        except ValueError:
            print("Error: Enter edges as two integers separated by a space (e.g., '0 1').")

    return adj_list, num_vertices

def is_complete_graph(adj_list, num_vertices):
    for u in range(num_vertices):
        if len(adj_list[u]) != num_vertices - 1 or u in adj_list[u]:
            return False
    return True

def print_adj_list(adj_list, num_vertices):
    print("\nAdjacency List:")
    for u in range(num_vertices):
        neighbors = sorted(adj_list[u])
        print(f"{u}: {neighbors}")

def main():
    print("=== Complete Graph Checker (Adjacency List) ===")
    adj_list, num_vertices = input_graph()
    print_adj_list(adj_list, num_vertices)
    if is_complete_graph(adj_list, num_vertices):
        print("\nThe graph is COMPLETE (all possible edges exist).")
    else:
        print("\nThe graph is NOT complete (missing edges).")

if __name__ == "__main__":
    main()
