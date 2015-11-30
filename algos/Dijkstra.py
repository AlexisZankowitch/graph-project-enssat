from _ctypes import sizeof
import random
from matrices.WeightMatrix import WeightMatrix

__author__ = 'azank'


class Dijkstra:
    """
    recursive dijkstra, not done
    """
    def __init__(self, size):
        self.weightMatrix = WeightMatrix(size)
        self.start = random.randint(0, self.weightMatrix.size - 1)
        self.finish = random.randint(0, self.weightMatrix.size - 1)
        self.accessibleNode = []
        self.weightNode = []
        self.nodes_list = []
        self.weight_way = 0
        self.initialization()

    def list_construction(self):
        for i in range(self.weightMatrix.size):
            adj = []
            weight = []
            for j in range(self.weightMatrix.size):
                if self.weightMatrix.apex[i][j] != 0:
                    adj.append(j)
                    weight.append(self.weightMatrix.apex[i][j])
            self.accessibleNode.append(adj)
            self.weightNode.append(weight)

    def closer_node(self, i):
        min_weight = 999  # infinite val
        c_node = 0
        for j in range(len(self.accessibleNode[i])):
            if min_weight > self.weightNode[i][j]:
                min_weight = self.weightNode[i][j]
                c_node = j
        self.weight_way += min_weight
        self.nodes_list.append(self.accessibleNode[i][c_node])
        print('nodes list :' + str(self.nodes_list))
        print("weight's way :" + str(self.weight_way))
        # print('node :' + str(i))
        # print('weight :'+ str(self.weightNode[i][j]))

    def dijkstra_print(self):
        self.weightMatrix.print()
        print('Start :' + str(self.start))
        print('Finish :' + str(self.finish))
        print('accessible nodes :' + str(self.accessibleNode))
        print('nodes weight :' + str(self.weightNode))

    def define_finish(self):
        """
        finish point must not be equal to start point and not be directly accessible from the beginning in order to test
        the algorithm.
        :return: Boolean
        """
        reset = False
        c = 0
        while (self.finish == self.start or self.finish in self.accessibleNode[self.start]) and c < 100:
            self.finish = random.randint(self.finish, self.weightMatrix.size - 1)
            c += 1
            print(c)
            if c >= 100:
                reset = True
        return reset

    def initialization(self):
        self.nodes_list.append(self.start)
        self.list_construction()
        # test if the matrix is ok to launch the algorithm
        if self.define_finish():
            self.__init__(self.weightMatrix.size)
        else:
            self.algorithm()

    def algorithm(self):
        self.dijkstra_print()
        self.closer_node(self.start)
