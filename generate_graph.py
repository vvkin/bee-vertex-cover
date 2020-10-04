#!/usr/bin/env python

"""
Script to generate random undirected graph
with given number of vertices and edges.
Power of each vertex ∈ [2, max_power] (if there are enough edges)
Usage: python generate_graph.py [vertex_num] [edges_num] [max_power] [file_name]
"""

import numpy as np
import sys

class TooSmallPower(Exception): pass # just custom Exception to handle errors with mask

if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit('Incorrect number of parameters')
    
    try:
        v_num, e_num, max_power = map(np.int, sys.argv[1:4])
        file_handler = open(sys.argv[4], 'w')
        
        powers = np.zeros(v_num, np.int) # degree of each vertex
        vertices = np.arange(v_num) # just range
 
        file_handler.write(f'{v_num} {e_num}\n')

        for _ in range(e_num):
            mask = powers < 2 # vertices with power less than two
            mask = powers < max_power if not np.any(mask) else mask # else select random vertices
            if np.count_nonzero(mask) < 2: raise TooSmallPower # here are at least two valid vertices
            
            src = np.random.choice(vertices[mask])
            mask[src] = False  # prevent (src == dest)
            dest = np.random.choice(vertices[mask])
            powers[src] += 1; powers[dest] += 1

            file_handler.write(f'{src} {dest}\n')
            
        file_handler.close()
    
    except TooSmallPower:
        file_handler.close()
        sys.exit('Too small maximal power of each vertex!')
    except ValueError:
        sys.exit('Incorrect type of input parameters')
    except:
        sys.exit('Sorry, but something went wrong')
