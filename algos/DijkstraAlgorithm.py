import math

from algos.AlgorithmsTools import AlgorithmsTools

__author__ = 'azank'


class DijkstraAlgorithm (AlgorithmsTools):
    def __init__(self):
        super().__init__()

    def dijkstra(self, matrix):
        """
        Call this method to launch Dijkstra algorithm.
        :param matrix: valued matrix
        """
        self.matrix = matrix
        self.print_matrix('dijkstra')
        """
        Initialization
        """
        E = [0]  # list of node which have been used
        D = []  # list of the shortest way between the arc(0,x)
        Prev = [0] * len(self.matrix) # list of the previous node
        """
        Build D list
        """
        for i in range(len(self.matrix)):
            if self.has_arc(0, i):
                D.append(self.matrix[0][i])
            else:
                D.append(math.inf)
        """
        Dijkstra algorithm
        """
        D[0] = 0
        Dd = D.copy()
        for i in range(1, len(self.matrix)):
            t = self.get_imin(Dd)
            Dd[t] = math.inf
            E.append(t)
            successors = self.get_successor(t, E)
            for successor in successors:
                history = D[successor]
                D[successor] = min(D[successor], D[t] + self.get_weight(successor, t))
                """
                Stores the previous noed
                """
                if history != D[successor]:
                    Prev[successor] = t
                Dd[successor] = D[successor]
                for val in E:
                    Dd[val] = math.inf
        self.matrix= D # useful to test if the result is correct
        """
        Display
        """
        print('Prev :' + str(Prev))
        print('Result : ' + str(D))