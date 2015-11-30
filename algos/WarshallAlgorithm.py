
from algos.Algorithms import Algorithms

__author__ = 'azank'


class WarshallAlgorithm (Algorithms):
    def __init__(self):
        super().__init__()

    def warshall(self, matrix):
        """
        Call this method to launch Warshall algorithm.
        :param matrix: connectivity matrix or routing matrix
        """
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for x in range(len(self.matrix)):
                if self.has_arc(x, i):
                    for y in range(len(self.matrix)):
                        """
                        Check if there is an arc between i and y, and if the value of (x,y) = 0
                        """
                        if self.has_arc(i, y) and not self.has_arc(x, y):
                            self.add_arc(x, y, self.matrix[x][i])
    def test_result(self, expected_matrix):
        """
        Checks if the matrices are the same.
        :param expected_matrix: matrix
        :return: String
        """
        res = True
        if len(self.matrix) is not None and len(self.matrix) == len(expected_matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if not self.is_equal(expected_matrix, i, j):
                        res = False
        return "Result is correct" if res else "Result is not correct"