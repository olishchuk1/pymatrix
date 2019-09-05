from pymatrix import Pymatrix


class Sole(Pymatrix):
    def __init__(self, matrix, column_vector):
        self.matrix = matrix
        self.column_vector = column_vector

    def gaussian_elimination(self, matrix):
        # eliminate columns
        for col in range(len(matrix[0])):
            for row in range(col + 1, len(matrix)):
                r = [(row_value * (-(matrix[row][col] / matrix[col][col]))) for row_value in matrix[col]]
                matrix[row] = [sum(pair) for pair in zip(matrix[row], r)]
        # now backsolve by substitution
        result = []
        matrix.reverse()  # makes it easier to backsolve
        for row in range(len(matrix)):
            if row == 0:
                result.append(matrix[row][-1] / matrix[row][-2])
            else:
                inner = 0
                # substitute in all known coefficients
                for column in range(row):
                    inner += (result[column] * matrix[row][-2 - column])
                # the equation is now reduced to ax + b = c form
                # solve with (c - b) / a
                result.append((matrix[row][-1] - inner) / matrix[row][-row - 2])
        result.reverse()
        return result

    def gauss_jordan_elimination(self):
        pass

    def cramers_rule(self):
        pass