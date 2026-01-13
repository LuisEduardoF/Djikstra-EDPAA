from heap import Heap

# Funcao para ler o grafo do arquivo de entrada
# input: file_path
# output: graph (dicionario de adjacencia) (|V| + |E|), initial_node integer
def read_file(file_path): 
    graph = {}
    initial_node = None
    
    with open(file_path, 'r') as file:
        for line in file:
            if initial_node is None: # Le o node inicial
                initial_node = int(line.strip().split('_')[1])
                continue
            
            # Le a matriz de adjacência
            parts = line.strip().split(',')
            node = int(parts[0].split('_')[1])
            edges = {}
            
            # Le pesos das arestas
            for i, weight in enumerate(parts[1:]):
                neighbor = i
                if neighbor >= node:
                    neighbor += 1
                try:
                    if float(weight) > 0 and float(weight) != float('inf'):
                        edges[int(neighbor)] = float(weight)
                except ValueError: # Se vier 'bomba' ou qualquer outra coisa que não seja float, admite como inf
                    continue
            graph[node] = edges
         
    return graph, initial_node 

# graph => Dicionario de adjacencia {node: {neighbor: weight, ...}, ...}
# initial_node => Nodo inicial para o Dijkstra
