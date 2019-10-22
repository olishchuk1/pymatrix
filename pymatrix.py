from operator import itemgetter
from pprint import pprint


class Pymatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def mprint(self):
        """
        prints matrix in matrix form
        :return: nothing
        """
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                print(j, end=" ")
            print()
        pass

    def mmultiply(self, matrix):
        """
        multiplies object matrix on another matrix
        :param second matrix:
        :return:
        """
        try:
            result_matrix = [[0 for row in range(len(self.matrix))] for col in range(len(matrix[0]))]
            for i in range(len(self.matrix)):
                for j in range(len(matrix[0])):
                    for k in range(len(matrix)):
                        result_matrix[i][j] += self.matrix[i][k] * matrix[k][j]
            self.matrix = result_matrix
        except IndexError:
            pass
        pass

    def madd(self, matrix):
        """
        adds to object matrix another matrix
        :param matrix:
        :return:
        """
        try:
            result_matrix = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    result_matrix[i][j] = self.matrix[i][j] + matrix[i][j]
            self.matrix = result_matrix
        except IndexError:
            pass
        pass

    def mtranpose(self):
        """
        transposes object matrix
        :return:
        """
        result_matrix = [[0 for col in range(len(self.matrix))] for row in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[j][i] = self.matrix[i][j]
        self.matrix = result_matrix
        pass

    def mrotate(self):
        """
        rotates matrix at 90 degrees left
        :return:
        """
        result_matrix = [[0 for col in range(len(self.matrix[0]))] for row in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[i][j] = self.matrix[i][len(self.matrix[0]) - 1 - j]
                # left turn -> result_matrix[i][j] = self.matrix[len(self.matrix) - 1 - i][j]
        self.matrix = result_matrix
        pass

    def matrix_sort(self, i):
        for k in range(len(self.matrix)-2, i, -1):
            for j in range(i, k+1):
                if self.matrix[j][i] < self.matrix[j+1][i]:
                    self.matrix[j], self.matrix[j+1] = self.matrix[j+1], self.matrix[j]
        pass

    def triangle_matrix(self):
        for y in range(len(self.matrix)):
            self.matrix_sort(y)
            for i in range(len(self.matrix) - 1 - y):
                mult = self.matrix[y + i + 1][y] / self.matrix[y][y]
                for j in range(y, len(self.matrix[i+1])):
                    self.matrix[y + i + 1][j] -= mult * self.matrix[y][j]
        pass

    def square_check(self):
        """
        checks if a matrix is a square matrix
        :return:
        """
        return len(self.matrix) == len(self.matrix[0])

    def mdeterminant(self):
        self.triangle_matrix()
        pprint(self.matrix)
        res = 1
        for i in range(len(self.matrix)):
            res *= self.matrix[i][i]
        print(res)
        pass
