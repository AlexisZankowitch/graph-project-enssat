import math

__author__ = 'azank'


class Algorithms:
    def __init__(self):
        self.matrix = []

    def print_matrix(self, name):
        """
        Prints the matrix
        :param name: String : name of the matrix
        """
        if self.matrix is not None:
            print(name)
            for i in range(len(self.matrix)):
                print(self.matrix[i])
        else:
            print("Matrix ins't initialize")

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
        Prev = [0] * len(self.matrix)  # list of the previous node
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
        """
        Display
        """
        print('Prev :' + str(Prev))
        print('Result : ' + str(D))
        self.matrix = D

    def get_imin(self, lists):
        """
        Returns index from the minimum value from a list.
        :param lists: list
        :rtype : integer
        """
        return lists.index(min(lists))

    def get_successor(self, node, E):
        """
        Returns all successors of a node from a list.
        :param node:
        :param E: list
        :return: list of nodes
        """
        successors = []
        for j in range(len(self.matrix)):
            if self.has_arc(node, j):
                successors.append(j)
        return sorted(successors)

    def get_weight(self, a, b):
        """
        Returns the weight of the arc (a,b).
        :param a: node
        :param b: node
        :return: int
        """
        return self.matrix[b][a]

    def has_arc(self, a, b):
        """
        Return true if there is an arc between a and b.
        :param a: node
        :param b: node
        :return: boolean
        """
        return self.matrix[a][b] != 0

    def add_arc(self, a, b, v):
        """
        Adds an arc between a and b.
        :param a: node
        :param b: node
        :param v: int, the value to add
        """
        self.matrix[a][b] = v

    def is_equal(self, g, a, b):
        """
        Returns true if the value of the arc (a,b) is equal to the value of the arc(a,b) in the matrix g.
        :param g: matrix
        :param a: node
        :param b: node
        :return: boolean
        """
        return self.matrix[a][b] == g[a][b]

    def test_result(self, expected_matrix):
        """
        Checks if the matrices are the same.
        :param expected_matrix: matrix
        :return: String
        """
        return "Result is correct" if self.matrix == expected_matrix else "Result is not correct"
