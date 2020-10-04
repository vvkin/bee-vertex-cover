import numpy as np
import sys


def greedy_solve(file_name: str) -> list:
    adj_matrix = np.load(file_name + '.npy')
    v_cover = []
    
    while np.sum(adj_matrix):  # while there are uncovered edges
        powers = adj_matrix.sum(axis=1) 
        max_idx = np.argmax(powers)
        v_cover.append(max_idx)

        adj_matrix[max_idx, :] = 0
        adj_matrix[:, max_idx] = 0
    
    return v_cover

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        answer = greedy_solve(file_name)
        print(len(answer), '\n', answer)
    except IndexError:
        sys.exit('Incorrect number of input parameters')
    except:
        sys.exit('Sorry, but something went wrong')
