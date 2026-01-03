from heap import Heap

class Dijkstra():
    def __init__(self, graph, initial_node):
        self.graph = graph
        self.initial_node = initial_node

    def dijkstra(self):
        distances = {node: float('inf') for node in self.graph}
        print("Distances initialized:", distances)
        visited = {}
        heap = Heap()
        heap.insert((0, self.initial_node, None))  # (distance, node, previous_node)
        
        while not heap.is_empty():
            current_distance, current_node, previous_node = heap.extract_min()
            
            # print(f"Processing node_{current_node} with current_distance {current_distance}, distances: {int(current_node) == self.initial_node:}")
            if current_node in visited:
                continue

            visited[current_node] = visited[previous_node] + [current_node] if previous_node is not None else [current_node]
        
            
            print(f"SHORTEST PATH TO node_{current_node}:", end=" ")
            for node in visited[current_node][::-1]:
                if node != self.initial_node:
                    print(f"node_{node} <-", end=" ")
                else:
                    print(f"node_{node}", end=" ")
            print(f"(Distance: {current_distance:.2f})")

            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = current_distance + weight
                    if new_distance < distances[int(neighbor)]:
                        distances[int(neighbor)] = new_distance
                        heap.insert((new_distance, neighbor, current_node))
                
        return distances, visited