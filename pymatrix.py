class Pymatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def mprint(self):
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                print(j, end=" ")
            print()
        pass

    def mmultiply(self, matrix):
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

    def maddition(self, matrix):
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
        result_matrix = [[0 for col in range(len(self.matrix))] for row in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[j][i] = self.matrix[i][j]
        self.matrix = result_matrix
        pass

    def mrotate(self):
        result_matrix = [[0 for col in range(len(self.matrix[0]))] for row in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[i][j] = self.matrix[i][len(self.matrix[0]) - 1 - j]
                # left turn -> result_matrix[i][j] = self.matrix[len(self.matrix) - 1 - i][j]
        self.matrix = result_matrix
        pass


def main():
    mat = Pymatrix([[1, 2, 3], [6, 5, 4]])
    mat.maddition([[1, 3, 5], [4, 2, 3]])
    mat.mprint()
    mat.mtranpose()
    mat.mrotate()
    mat.mprint()


if __name__ == '__main__':
    main()