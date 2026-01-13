from heap import Heap

class Dijkstra():
    def __init__(self, graph, initial_node):
        # TAD composto por um grafo e um node inicial
        self.graph = graph
        self.initial_node = initial_node

    # Funcao auxiliar para fazer o tracking da lineage de um node para o node inicial
    # input: visited array, target node
    # output: lineage array
    def lineage(self, visited, node):
        lineage = [node]
        while True:
            if visited[node] is None:
                return []
            node = visited[node]
            lineage.append(node)
            
            if node == visited[node]: # 
                break
            
        return lineage

    # Gera o output no formato estabelecido (lineage + distance)
    # input: distances array, visited array, order array
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
                
    # Implementação do algoritmo de Dijkstra
    # output: distances array (|V|), visited array (|V|), order array (|V|)     
    def dijkstra(self):
        
        distances = [float('inf')] * len(self.graph) # Inicializa todas as distancias como infinito (array de tamanho |V|)
        # distances = {node: float('inf') for node in self.graph}  # Usando dicionário para suportar grafos não numericamente indexados
        distances[self.initial_node] = 0 # Distancia do node inicial para ele mesmo é 0
        
        # print("Distances initialized:", distances)
        visited = [None] * len(self.graph) # Inicializa todos os nodes como None, ou seja, não visitados (array de tamanho |V|)
        # visited = {node: None for node in self.graph}  # Usando dicionário para suportar grafos não numericamente indexados
        order = [] # Guarda a ordem de visita dos nodes
        
        heap = Heap() # Min-heap para pegar o próximo node com a menor distancia
        heap.insert((0, self.initial_node, None))  # (distance, node, previous_node)
        
        while not heap.is_empty():
            current_distance, current_node, previous_node = heap.extract_min() # Extrai o node com a menor distancia
            
            # print(f"Processing node_{current_node} with current_distance {current_distance}, distances: {int(current_node) == self.initial_node:}")
            if visited[current_node] is not None: # Se já foi visitado, next
                continue
            
            # Se não...
            visited[current_node] = previous_node if previous_node is not None else current_node # Marca o lugar do node atual, com o node anterior (o visited serve como um mapa de parentes)

            order.append(current_node) # Adiciona o node atual na ordem para não se perder no print do output final
            
            # Para cada vizinho do node atual...
            for neighbor, weight in self.graph[current_node].items():
                if visited[neighbor] is None: # Se o vizinho não foi visitado ainda
                    new_distance = current_distance + weight # Calcula a nova distancia
                    if new_distance < distances[neighbor]: # Se a nova distancia é menor que a distancia atual
                        distances[neighbor] = new_distance
                        heap.insert((new_distance, neighbor, current_node)) # Insere no heap a nova distancia, o vizinho e o node atual como previous_node
                
        return distances, visited, order