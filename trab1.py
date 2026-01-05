import sys
from graph import read_file
from djikstra import Dijkstra
import time
import tracemalloc



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERRO NA EXECUÇÃO: python3 trab1.py <input_path> <output_path>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    graph, initial_node = read_file(input_path)
        
    dijkstra_solver = Dijkstra(graph, initial_node)
    
    tracemalloc.start()
    begin_time_original = time.time()
    distances, visited, order = dijkstra_solver.dijkstra()
    end_time_original = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    time_original = end_time_original - begin_time_original
    print(f"Execution time: {time_original:.6f} seconds")
    print(f"Current memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
    
    dijkstra_solver.output(distances, visited, order, output_path)
    
    