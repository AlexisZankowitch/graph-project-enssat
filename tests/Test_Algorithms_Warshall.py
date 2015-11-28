from algos.WarshallAlgorithm import WarshallAlgorithm
from matrices.ConnectivityMatrix import ConnectivityMatrix
from matrices.RoutingMatrix import RoutingMatrix
from matrices.Warshall_Matrices import Warshall_Matrices

__author__ = 'azank'

test_algorithm = WarshallAlgorithm()

# test Warshall algorithm
matrices = Warshall_Matrices()

"""
Tests
"""

test_algorithm.warshall(matrices.matrix_one)
test_algorithm.print_matrix('Fermeture transitive matrix_one :')
print(test_algorithm.test_result(matrices.matrix_one_expected))

test_algorithm.warshall(matrices.matrix_two)
test_algorithm.print_matrix('Fermeture transitive matrix_two :')
print(test_algorithm.test_result(matrices.matrix_two_expected))

test_algorithm.warshall(matrices.matrix_routage)
test_algorithm.print_matrix('Fermeture transitive matrix_routage :')
print(test_algorithm.test_result(matrices.matrix_routage_expected))

"""
Test on random matrix
"""

matrix = ConnectivityMatrix(5)
matrix.print()
test_algorithm.warshall(matrix.apex)
test_algorithm.print_matrix('Fermeture transitive matrice aleatoire :')

matrix = RoutingMatrix(10)
matrix.print()
test_algorithm.warshall(matrix.apex)
test_algorithm.print_matrix('Fermeture transitive routage matrice aleatoire :')