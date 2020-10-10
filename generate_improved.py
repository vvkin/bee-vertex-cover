from networkx.classes.function import non_neighbors
import numpy as np
import networkx as nx


def remove_edges(graph: nx.Graph, max_deg: int) -> nx.Graph: 
    v_num = graph.number_of_nodes()
    to_remove = [x for x in range(v_num) if graph.degree[x] > max_deg]
    
    for src in to_remove: # iterate over vertices with degree > max_deg
        to_remove = np.maximum(0, graph.degree[src] - max_deg)
        neighbors = [x for x in graph.neighbors(src)]
        
        for dest in neighbors[:to_remove + 1]:
            graph.remove_edge(src, dest)
    
    return graph


def add_edges(graph: nx.Graph, min_deg: int, max_deg: int) -> nx.Graph:    
    v_num = graph.number_of_nodes()
    to_add = [x for x in range(v_num) if graph.degree[x] < min_deg]
        
    for src in to_add:
        for dest in non_neighbors(graph, src): # iterate over non adj vertices
            if graph.degree[src] >= max_deg: 
                break
                
            if graph.degree[dest] < max_deg:
                graph.add_edge(src, dest)
                    
    return graph

def generate_graph(v_num:int, min_deg:int, max_deg: int) -> nx.Graph:
    degrees = np.random.randint(min_deg, max_deg + 1, size=v_num)
    graph = nx.generators.degree_seq.expected_degree_graph(degrees, selfloops=False)
    
    graph = remove_edges(graph, max_deg)
    graph = add_edges(graph, min_deg, max_deg)
        
    return graph

if __name__ == '__main__':
    graph = generate_graph(300, 299, 299)