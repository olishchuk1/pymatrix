from pymatrix import Pymatrix


class Sole(Pymatrix):
    def __init__(self, matrix, column_vector):
        self.matrix = matrix
        self.column_vector = column_vector

    def gaussian_elimination(self):
        matrix = self.matrix
        for i in range(len(matrix)):
            matrix[i].append(self.column_vector[i][0])
        # eliminate columns
        for col in range(len(self.matrix[0])):
            for row in range(col + 1, len(matrix)):
                r = [(row_value * (-(matrix[row][col] / matrix[col][col]))) for row_value in matrix[col]]
                matrix[row] = [sum(pair) for pair in zip(matrix[row], r)]

        result = []
        matrix.reverse()
        for sol in range(len(matrix)):
            if sol == 0:
                result.append(matrix[sol][-1] / matrix[sol][-2])
            else:
                inner = 0
                # substitute in all known coefficients
                for x in range(sol):
                    inner += (result[x] * matrix[sol][-2 - x])
                # the equation is now reduced to ax + b = c form
                # solve with (c - b) / a
                result.append((matrix[sol][-1] - inner) / matrix[sol][-sol - 2])
        result.reverse()
        return result

    def gauss_jordan_elimination(self):
        """

        :return:
        """
        pass

    def cramers_rule(self):
        """

        :return:
        """
        pass