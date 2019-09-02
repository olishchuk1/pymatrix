from pprint import pprint


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
        rows = len(self.matrix)
        cols = len(matrix[0])
        result_matrix = [[0 for i in range(cols)] for i in range(rows)]
        # try:
        #     for i in range(len(self.matrix)):
        #         for j in range(len(self.matrix[0])):
        #
        return result_matrix

    # def rotate(self, turn_number):
    #     turn_number = turn_number % 4
    #     for i in self.matrix:
    #         for j in self.matrix[i]:


def main():
    mat = Pymatrix([[1, 2, 3], [6, 5, 4]])
    pprint(mat.mmultiply([[1, 3], [1, 5], [4, 2]]))
    mat.mprint()


if __name__ == '__main__':
    main()