
from algos.AlgorithmsTools import AlgorithmsTools

__author__ = 'azank'


class WarshallAlgorithm (AlgorithmsTools):
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