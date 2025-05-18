def is_complete_graph(adj_list):
    """Check if adjacency list represents a complete undirected graph without self-loops"""
    vertices = list(adj_list.keys())
    n = len(vertices)
    
    if n == 0:
        return True
        
    for vertex in vertices:
        if len(adj_list[vertex]) != n - 1 or vertex in adj_list[vertex]:
            return False
        for neighbor in adj_list[vertex]:
            if vertex not in adj_list.get(neighbor, []):
                return False
    return True

def input_graph():
    """Input adjacency list with essential validation"""
    adj_list = {}
    print("Enter vertices first (one per line), then edges (format: 'Vertex Neighbor1 Neighbor2...')")
    
    print("Enter all vertex names (type 'done' to finish):")
    while True:
        vertex = input("Vertex> ").strip()
        if vertex.lower() == 'done':
            if not adj_list:
                print("(Please enter at least one vertex)")
                continue
            break
        adj_list[vertex] = []

    print("\nEnter neighbors for each vertex (empty line to skip):")
    for vertex in adj_list:
        while True:  
            neighbors = input(f"{vertex}> ").strip().split()
            if not neighbors:
                break
            if vertex in neighbors:
                print(f"Error: Self-loop for {vertex}")
                continue
            if len(neighbors) != len(set(neighbors)):
                print(f"Error: Duplicate neighbors for vertex {vertex}")
                continue
            if not all(n in adj_list for n in neighbors):
                print(f"Error: Unknown vertex in neighbors")
                continue
            adj_list[vertex] = neighbors
            break  
    return adj_list

def main():
    print("==== Complete Graph Checker ====")
    adj_list = input_graph()
    
    print("\nAdjacency List:")
    for vertex, neighbors in adj_list.items():
        print(f"{vertex}: {' '.join(neighbors)}")
    
    print("\nThe graph is", "COMPLETE" if is_complete_graph(adj_list) else "NOT complete")

if __name__ == "__main__":
    main()
