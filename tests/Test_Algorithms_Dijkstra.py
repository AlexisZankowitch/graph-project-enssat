from algos.DijkstraAlgorithm import DijkstraAlgorithm
from matrices.Dijkstra_Matrices import Dijkstra_Matrices
from matrices.WeightMatrix import WeightMatrix

__author__ = 'azank'

test_algorithm = DijkstraAlgorithm()

matrices = Dijkstra_Matrices()

"""
Tests
"""

test_algorithm.dijkstra(matrices.matrix_one)

test_algorithm.dijkstra(matrices.matrix_two)

test_algorithm.dijkstra(matrices.matrix_three)

"""
Test on random matrix
"""

matrix = WeightMatrix(5)
test_algorithm.dijkstra(matrix.apex)

