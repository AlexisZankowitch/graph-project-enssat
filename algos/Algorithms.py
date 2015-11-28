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
