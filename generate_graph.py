#!/usr/bin/env python

"""
Script to generate random undirected graph
with given number of vertices and expected power of each vertex.
Power of each vertex ∈ [0, max_power] (if there are enough edges)
Usage: python generate_graph.py [vertex_num] [max_power] [file_name]
"""

import numpy as np
import networkx as nx
import sys

if __name__ == '__main__':
    try:
        v_num, max_power = map(np.int, sys.argv[1:3])
        file_name = sys.argv[3]
        
        degrees = np.random.randint(2, max_power+1, size=v_num) # random degree of each vertex
        graph = nx.generators.degree_seq.expected_degree_graph(degrees, selfloops=False)
        np.save(file_name, nx.to_numpy_matrix(graph))

    except IndexError:
        sys.exit('Incorrect number of input parameters')
    except ValueError:
        sys.exit('Invalid input parameters')
    except:
        sys.exit('Sorry, but something went wrong')
