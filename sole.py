from pymatrix import Pymatrix


class Sole(Pymatrix):
    def __init__(self, matrix, column_vector):
        self.matrix = matrix
        self.column_vector = column_vector

    def gaussian_elimination(self):
        pass

    def gauss_jordan_elimination(self):
        pass

    def cramers_rule(self):
        pass