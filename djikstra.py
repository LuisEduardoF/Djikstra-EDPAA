from heap import Heap

class Dijkstra():
    def __init__(self, graph, initial_node):
        self.graph = graph
        self.initial_node = initial_node

    def lineage(self, visited, node):
        lineage = [node]
        while True:
            if visited[node] is None:
                return []
            node = visited[node]
            lineage.append(node)
            
            if node == visited[node]: # Initial Node Case
                break
            
        return lineage

    def output(self, distances, visited, order, output_path):
        # print("ORDER:", order)
        with open(output_path, "w") as f:
            for node in order:
                f.write("SHORTEST PATH TO ")
                
                # Which Node?
                f.write(f"node_{node}: ")
                
                # Lineage
                lineage = self.lineage(visited, node)
                
                lineage_str = " <- ".join([f"node_{n}" for n in lineage])
                
                f.write(lineage_str + " ")
                
                # Distance
                f.write(f"(Distance: {distances[node]:.2f})\n")
                
            
    def dijkstra(self):
        distances = [float('inf')] * len(self.graph)
        distances[self.initial_node] = 0
        
        # print("Distances initialized:", distances)
        visited = [None] * len(self.graph)
        order = []
        
        heap = Heap()
        heap.insert((0, self.initial_node, None))  # (distance, node, previous_node)
        
        while not heap.is_empty():
            current_distance, current_node, previous_node = heap.extract_min()
            
            # print(f"Processing node_{current_node} with current_distance {current_distance}, distances: {int(current_node) == self.initial_node:}")
            if visited[current_node] is not None:
                continue
            
            visited[current_node] = previous_node if previous_node is not None else current_node

            order.append(current_node)
            
            for neighbor, weight in self.graph[current_node].items():
                if visited[neighbor] is None:
                # if neighbor not in visited:
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heap.insert((new_distance, neighbor, current_node))
                
        return distances, visited, order