__author__ = 'azank'

# TODO expected results
class Dijkstra_Matrices:
    """
    Contains several matrices and their expected results for the verifications
    """
    def __init__(self):
        self.matrix_one = [[0, 10, 0, 30, 100],
                           [0, 0, 50, 0, 0],
                           [0, 0, 0, 0, 10],
                           [0, 0, 20, 0, 60],
                           [0, 0, 0, 0, 0]]

        self.matrix_two = [[0, 2, 5, 4, 0, 0, 0],
                           [0, 0, 2, 0, 7, 0, 0],
                           [0, 0, 0, 1, 4, 3, 0],
                           [0, 0, 0, 0, 0, 4, 0],
                           [0, 0, 0, 0, 0, 1, 5],
                           [0, 0, 0, 0, 0, 1, 7],
                           [0, 0, 0, 0, 0, 0, 0]]

        self.matrix_three = [[0, 2, 5, 4, 0, 0, 0],
                             [2, 0, 2, 0, 7, 0, 0],
                             [5, 2, 0, 1, 4, 3, 0],
                             [4, 0, 1, 0, 0, 4, 0],
                             [0, 7, 4, 0, 0, 1, 5],
                             [0, 0, 3, 4, 1, 0, 7],
                             [0, 0, 0, 0, 0, 0, 0]]
