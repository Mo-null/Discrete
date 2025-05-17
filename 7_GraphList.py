def is_complete_graph(adj_list):
    vertices = list(adj_list.keys())
    n = len(vertices)
    
    for vertex in adj_list:
        if len(adj_list[vertex]) != n - 1 or vertex in adj_list[vertex]:
            return False
        
        for neighbor in adj_list[vertex]:
            if vertex not in adj_list[neighbor]:
                return False
                
    return True

def input_graph():
    adj_list = {}
    print("Enter adjacency list (one vertex per line, format: 'A B C' or '1 2 3')")
    print("Enter an empty line to finish")
    
    while True:
        line = input("> ").strip()
        if not line:
            break
            
        parts = line.split()
        vertex = parts[0]
        neighbors = parts[1:]
        
        if len(neighbors) != len(set(neighbors)):
            print(f"Error: Duplicate neighbors for vertex {vertex}")
            continue
            
        adj_list[vertex] = neighbors
    
    return adj_list

def main():
    print("==== Complete Graph Checker ====")
    adj_list = input_graph()
    
    print("\nAdjacency List:")
    for vertex, neighbors in adj_list.items():
        print(f"{vertex}: {' '.join(neighbors)}")
    
    if is_complete_graph(adj_list):
        print("\n The graph is COMPLETE")
    else:
        print("\n The graph is NOT complete")

if __name__ == "__main__":
    main()
