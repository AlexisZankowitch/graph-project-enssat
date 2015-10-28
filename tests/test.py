from algos.Dijkstra import Dijkstra
from matrices.BoolMatrix import BoolMatrix
from matrices.AdjacencyMatrix import AdjacencyMatrix

__author__ = 'azank'

# print('Matrice adjacence : ')
# matriceAdjacence = MatriceAdjacence(4)
# matriceAdjacence.print()
#
# print('Matrice bool : ')
# matriceBool = MatriceBool(4)
# matriceBool.print()

print('Dijkstra : ')
dijkstra = Dijkstra(4)
dijkstra.list_construction()