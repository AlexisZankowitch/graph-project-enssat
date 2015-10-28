from matrices.AdjacencyMatrix import AdjacencyMatrix

__author__ = 'azank'


class Dijkstra:
    def __init__(self, size):
        self.accessibleNode = []
        self.weightNode = []
        self.adjacencyMatrix = AdjacencyMatrix(4)
        self.adjacencyMatrix.print()

    def list_construction(self):
        for i in range(self.adjacencyMatrix.size):
            adj = []
            weight = []
            for j in range(self.adjacencyMatrix.size):
                if self.adjacencyMatrix.sommet[i][j] != 0:
                    adj.append(j)
                    weight.append(self.adjacencyMatrix.sommet[i][j])
            self.accessibleNode.append(adj)
            self.weightNode.append(weight)
        print('accessible nodes '+str(self.accessibleNode))
        print('nodes weight '+str(self.weightNode))
