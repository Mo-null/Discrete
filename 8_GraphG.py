def compute_degrees(adj_list):
    """Compute in-degree and out-degree for each vertex in a directed graph"""
    vertices = set(adj_list.keys()).union(*adj_list.values())
    in_degree = {v: 0 for v in vertices}
    out_degree = {v: len(adj_list.get(v, [])) for v in vertices}
    
    for v in adj_list:
        for neighbor in adj_list[v]:
            in_degree[neighbor] += 1
            
    return in_degree, out_degree

def input_directed_graph():
    """Input directed graph edges with validation"""
    adj_list = {}
    print("Enter edges as 'from to' (e.g., 'A B'). Empty line to finish:")
    
    while True:
        line = input("> ").strip()
        if not line:
            if not adj_list:
                print("Error: No edges entered. Try again.")
                continue
            break
            
        parts = line.split()
        if len(parts) != 2:
            print("Error: Exactly two vertices required. Try again.")
            continue
            
        u, v = parts
        if u == v:
            print("Error: Self-loops not allowed. Try again.")
            continue
            
        adj_list.setdefault(u, []).append(v)
    
    return adj_list

def main():
    print("=== Directed Graph Degree Calculator ===")
    adj_list = input_directed_graph()
    in_degree, out_degree = compute_degrees(adj_list)
    
    print("\nVertex | In-Degree | Out-Degree")
    print("-------------------------------")
    for v in sorted(in_degree.keys()):  # Safe to use direct dict access now
        print(f"{v:6} | {in_degree[v]:9} | {out_degree[v]:10}")

if __name__ == "__main__":
    main()
