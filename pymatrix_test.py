import unittest
from pymatrix import Pymatrix


class PymatrixTest(unittest.TestCase):

    def testtest(self):
        self.assertEqual(True, True)

    # NEED TO BE FIXED
    def test_madition(self):
        mat = Pymatrix([[1, 2, 3], [6, 5, 4]])
        self.assertEqual(mat.maddition([[1, 3, 5], [4, 2, 3]]), [[2, 5, 8], [10, 7, 7]])

    def test_mmultiply(self):
        mat = Pymatrix([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(mat.mmultiply([[2, 6, 5], [1, 8, 3]]), [[4, 22, 11], [10, 50, 27], [16, 78, 43]])


if __name__ == '__main__':
    mat = Pymatrix([[3, 2, 1], [7, -3, 2], [3, 4, 0]])
    mat.mdeterminant()

    # mat = Pymatrix([[2, 2, -1, 1], [4, 3, -1, 2], [8, 5, -3, 4],[3, 3, -2, 2]])
    # print(mat.mmultiply([[1], [1], [-1], [-1]]))
    # mat.mprint()
