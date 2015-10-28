__author__ = 'azank'


class Matrice:
    def __init__(self,size,name):
        self.name = name
        self.nbrSom = size
        self.apex = []
        self.start = 0
        self.arrive = 0
        self.size = size
        # matrix creation
        self.apex = [[0] * size for i in range(size)]

    def diagonal_zero(self):
        for i in range(self.nbrSom):
            self.replace_val(i, i, 0)

    def replace_val(self, x, y, val):
        self.apex[x][y] = val

    def print(self):
        print(str(self.name)+' matrix : ')
        for i in range(self.size):
            print(self.apex[i])



