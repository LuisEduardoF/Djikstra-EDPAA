from heap import Heap

def read_file(file_path):
    graph = {}
    initial_node = None
    
    with open(file_path, 'r') as file:
        for line in file:
            if initial_node is None:
                initial_node = int(line.strip().split('_')[1])
                continue
            parts = line.strip().split(',')
            node = int(parts[0].split('_')[1])
            edges = {}
            for i, weight in enumerate(parts[1:]):
                neighbor = i
                if neighbor >= node:
                    neighbor += 1
                try:
                    if float(weight) > 0 and float(weight) != float('inf'):
                        edges[int(neighbor)] = float(weight)
                except ValueError:
                    continue
            graph[node] = edges
            
    return graph, initial_node