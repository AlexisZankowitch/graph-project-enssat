__author__ = 'azank'


class Matrice:
    def __init__(self,size):
         self.nbrSom = size
         self.sommet = []
         self.start = 0
         self.arrive = 0
         self.size = size
         # matrice creation
         self.sommet = [[0] * size for i in range(size)]

    def diagonal_zero(self):
        for i in range(self.nbrSom):
            self.replace_val(i, i, 0)

    def replace_val(self, x, y, val):
        self.sommet[x][y] = val

    def print(self):
        for i in range(self.size):
            print(self.sommet[i])



