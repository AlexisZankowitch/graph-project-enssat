import random
from matrices.Matrix import Matrice

__author__ = 'azank'


class BoolMatrix(Matrice):
    def __init__(self, size):
        super(BoolMatrix, self).__init__(size,'Bool')
        # matrix filling
        for i in range(size):
            for j in range(size):
                if random.randint(0, 9) == 0:
                    self.apex[i][j] = 0
                else:
                    self.apex[i][j] = random.randint(0, 1)

        # put 0 on the diagonal
        self.diagonal_zero()
