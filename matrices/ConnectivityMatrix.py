import random
from matrices.Matrix import Matrix

__author__ = 'azank'


class ConnectivityMatrix(Matrix):
    def __init__(self, size):
        super(ConnectivityMatrix, self).__init__(size, 'Adjacency')
        # matrix filling
        for i in range(size):
            for j in range(size):
                if random.randint(0, 5) == 0:
                    self.apex[i][j] = 0
                else:
                    self.apex[i][j] = random.randint(0, 1)

        # put 0 on the diagonal
        self.diagonal_zero()

    def add_arc(self, x, y, val):
        self.apex[x][y] = val

    def hasArc(self,x,y):
        return True if self.apex[x][y] else False
