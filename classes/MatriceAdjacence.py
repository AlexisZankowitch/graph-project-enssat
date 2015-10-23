import random

__author__ = 'azank'


class MatriceAdjacence:
    # fonction d'initialisation de la matrice et remplissage de celle-çi
    def __init__(self, size=4):
        self.nbrSom = size  # nombre de sommets
        self.sommet = {}  # collection de listes constituant la matrice
        self.depart = 0  # sommet de départ
        self.arrive = 0  # sommet d'arrivée
        for i in range(size * size):  # remplissage des listes
            if (random.randint(0, 9) == 0):  # 1chance sur 9 d’avoir un 0
                self.sommet[i] = 0  # dans la matrice
            else:  # sinon le poids du segment
                self.sommet[i] = random.randint(1, 9)  # est pris au hasard
        self.diag_zero()
