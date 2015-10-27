import random
from matrices import MatriceAdjacence
from matrices.Matrice import Matrice

__author__ = 'azank'


class MatriceBool(Matrice):
    def __init__(self, size):
        super(MatriceBool, self).__init__(size)
        # matrice filling
        for i in range(size):
            for j in range(size):
                if random.randint(0, 9) == 0:
                    self.sommet[i][j] = 0
                else:
                    self.sommet[i][j] = random.randint(0, 1)

        # put 0 on the diagonal
        self.diagonal_zero()
