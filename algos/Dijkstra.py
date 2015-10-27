from matrices.MatriceAdjacence import MatriceAdjacence

__author__ = 'azank'


class Dijkstra:
    def __init__(self, size):
        self.accessibleNode = []
        self.weightNode = []
        self.matriceAdjacence = MatriceAdjacence(4)
        self.matriceAdjacence.print()

    def list_construction(self):
        for i in range(self.matriceAdjacence.size):
            adj = []
            weight = []
            for j in range(self.matriceAdjacence.size):
                if self.matriceAdjacence.sommet[i][j] != 0:
                    adj.append(j)
                    weight.append(self.matriceAdjacence.sommet[i][j])
            self.accessibleNode.append(adj)
            self.weightNode.append(weight)
        print(self.accessibleNode)
        print(self.weightNode)
