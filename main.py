from graph import read_file
from djikstra import Dijkstra


if __name__ == "__main__":
    file_path = 'casos_teste_v3/caso_teste_muito_pequeno_2.txt' 
    graph, initial_node = read_file(file_path)
    
    graph, initial_node = read_file(file_path)
    
    dijkstra_solver = Dijkstra(graph, initial_node)
    distances = dijkstra_solver.dijkstra()