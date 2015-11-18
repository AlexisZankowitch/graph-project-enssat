__author__ = 'azank'


class Algorithms:
    def __init__(self):
        self.matrix = None

    def print_matrix(self, name):
        if self.matrix is not None:
            print(name)
            for i in range(len(self.matrix)):
                print(self.matrix[i])
        else:
            print("Matrix ins't initialize")

    def warshall(self, matrix):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for x in range(len(self.matrix)):
                if self.has_arc(x, i):
                    for y in range(len(self.matrix)):
                        if self.has_arc(i, y) and self.arc_null(x, y):
                            self.add_arc(x, y, self.matrix[x][i])

    def dijkstra(self, matrix):
        self.matrix = matrix
        self.print_matrix('dijkstra')
        E = [0]
        D = []
        for i in range(len(self.matrix)):
            if self.has_arc(0, i):
                D.append(self.matrix[0][i])
            else:
                D.append(9999)
        Dd = D.copy()
        for i in range(len(self.matrix)):
            t = self.get_imin(Dd)
            Dd[t] = 9999
            E.append(t)
            successors = self.get_successor(t, E)
            for successor in successors:
                D[successor] = min(D[successor], D[t] + self.get_weight(successor, t))
                Dd[successor] = D[successor]
                # remember node where we went
                for val in E:
                    Dd[val] = 9999
        D[0] = 0
        print('Result : ' + str(D))

    def get_imin(self, lists):
        return lists.index(min(lists))

    def get_successor(self, node, E):
        successors = []
        for j in range(len(self.matrix)):
            if self.has_arc(node, j):
                successors.append(j)
        return sorted(successors)

    def get_weight(self, a, b):
        return self.matrix[b][a]

    def has_arc(self, a, b):
        return self.matrix[a][b] != 0

    def arc_null(self, a, b):
        return self.matrix[a][b] == 0

    def add_arc(self, a, b, v):
        self.matrix[a][b] = v

    def is_equal(self, g, a, b):
        return self.matrix[a][b] == g[a][b]

    def test_result(self, expected_matrix):
        res = True
        if len(self.matrix) is not None and len(self.matrix) == len(expected_matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if not self.is_equal(expected_matrix, i, j):
                        res = False
        return "Result is correct" if res else "Result is not correct"
