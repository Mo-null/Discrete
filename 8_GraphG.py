from collections import defaultdict

def input_directed_graph():
    adj_list = defaultdict(list)
    vertices = set()
    
    print("\nEnter directed edges as 'from to' (e.g., 'A B' for A → B).")
    print("Press Enter on an empty line to finish.\n")
    
    while True:
        edge_input = input("Edge: ").strip()

        if not edge_input:
            if not adj_list:
                print("Error: At least one edge required. Try again.")
                continue
            break

        parts = edge_input.split()
        if len(parts) != 2:
            print("Error: Please enter exactly two vertices separated by space.")
            continue
            
        u, v = parts

        if v in adj_list[u]:
            print(f"Warning: Edge {u}→{v} already exists (ignored)")
            continue
        adj_list[u].append(v)
        vertices.update({u, v})
    
    return adj_list, vertices

def compute_degrees(adj_list, vertices):
    in_degree = {v: 0 for v in vertices}
    out_degree = {v: 0 for v in vertices}
    
    for u, neighbors in adj_list.items():
        out_degree[u] = len(neighbors)
        
        for v in neighbors:
            in_degree[v] += 1
            
    return in_degree, out_degree

def display_results(in_degree, out_degree):
    max_len = max(max((len(str(v)) for v in in_degree), default=0), len("Vertex"))

    print(f"\n{'Vertex':<{max_len}} | {'In-Degree':>9} | {'Out-Degree':>10}")
    print("-" * (max_len + 23))
    
    for v in sorted(in_degree):
        print(f"{v:<{max_len}} | {in_degree[v]:>9} | {out_degree[v]:>10}")

def main():
    print("=== Directed Graph Degree Calculator ===")
    adj_list, vertices = input_directed_graph()
    in_degree, out_degree = compute_degrees(adj_list, vertices)
    display_results(in_degree, out_degree)

if __name__ == "__main__":
    main()
