from matrices.AdjacencyMatrix import AdjacencyMatrix
from matrices.RoutageMatrix import RoutageMatrix
from matrices.Test_Adjacency import Test_Adjacency

__author__ = 'azank'


def warshall_algorithm(matrix):
    for i in range(len(matrix.apex)):
        for x in range(len(matrix.apex)):
            if matrix.hasArc(x, i):
                for y in range(len(matrix.apex)):
                    if matrix.hasArc(i, y):
                        matrix.add_arc(x, y, 1)


def warshall_routage(matrix):
    for i in range(len(matrix.apex)):
        for x in range(len(matrix.apex)):
            if matrix.hasArc(x, i):
                for y in range(len(matrix.apex)):
                    if matrix.hasArc(i, y) and not (matrix.hasArc(x, y)):
                        matrix.add_arc(x, y, matrix.apex[x][i])


class Warshall:
    def __init__(self):
        self.adjacencyMatrix = None
        self.routageMatrix = None

    def warhsall(self, size):
        self.adjacencyMatrix = AdjacencyMatrix(size)
        self.adjacencyMatrix.print()
        warshall_algorithm(self.adjacencyMatrix)
        self.adjacencyMatrix.print()

    def routage(self, size):
        self.routageMatrix = RoutageMatrix(size)
        self.routageMatrix.print()
        warshall_routage(self.routageMatrix)
        self.routageMatrix.print()

    def test_warshall(self):
        test = Test_Adjacency(3)
        warshall_algorithm(test)
        result = [[0, 1, 1, 1],
                  [0, 0, 1, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]
        res = True
        for i in range(len(test.apex)):
            for j in range(len(test.apex)):
                if test.apex[i][j] != result[i][j]:
                    res = False

        return res
