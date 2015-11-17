from algos.Algorithms import Algorithms
from matrices.Warshall_Matrices import Warshall_Matrices

__author__ = 'azank'

test_algorithm = Algorithms()

# test Warshall algorithm
matrices = Warshall_Matrices()

test_algorithm.warshall(matrices.matrix_one)
test_algorithm.print_matrix('Fermeture transitive matrix_one :')
print(test_algorithm.test_result(matrices.matrix_one_expected))

test_algorithm.warshall(matrices.matrix_two)
test_algorithm.print_matrix('Fermeture transitive matrix_two :')
print(test_algorithm.test_result(matrices.matrix_two_expected))

test_algorithm.warshall(matrices.matrix_routage)
test_algorithm.print_matrix('Fermeture transitive matrix_routage :')
print(test_algorithm.test_result(matrices.matrix_routage_expected))
