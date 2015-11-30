from algos.Algorithms import Algorithms
from matrices.Dijkstra_Matrices import Dijkstra_Matrices
from matrices.WeightMatrix import WeightMatrix

__author__ = 'azank'

test_algorithm = Algorithms()

matrices = Dijkstra_Matrices()

"""
Tests
"""

test_algorithm.dijkstra(matrices.matrix_one)
print(test_algorithm.test_result(matrices.matrix_one_expected))

test_algorithm.dijkstra(matrices.matrix_two)
print(test_algorithm.test_result(matrices.matrix_two_expected))

test_algorithm.dijkstra(matrices.matrix_three)
print(test_algorithm.test_result(matrices.matrix_three_expected))

"""
Test on random matrix
"""
print("Test on random matrix")
matrix = WeightMatrix(5)
test_algorithm.dijkstra(matrix.apex)

