from algos.Algorithms import Algorithms
from matrices.Dijkstra_Matrices import Dijkstra_Matrices

__author__ = 'azank'

test_algorithm = Algorithms()

# test Warshall algorithm
matrices = Dijkstra_Matrices()

test_algorithm.dijkstra(matrices.matrix_one)

test_algorithm.dijkstra(matrices.matrix_two)

test_algorithm.dijkstra(matrices.matrix_three)
