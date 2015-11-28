from matrices.ConnectivityMatrix import ConnectivityMatrix

__author__ = 'azank'


class Test_Adjacency(ConnectivityMatrix):
    def __init__(self, size):
        super().__init__(size)
        self.apex = [[0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1],
                     [0, 0, 0, 0]]
