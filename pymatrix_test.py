import unittest
from pymatrix import Pymatrix


class PymatrixTest(unittest.TestCase):

    def testtest(self):
        self.assertEqual(True, True)

    # NEED TO BE FIXED
    def madition_test(self):
        mat = Pymatrix([[1, 2, 3], [6, 5, 4]])
        mat.maddition([[1, 3, 5], [4, 2, 3]])
        self.assertEqual(mat, [[2, 5, 8], [10, 7, 7]])

    def mmultiply_test(self):
        mat = Pymatrix([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(mat.mmultiply([[2, 6, 5], [1, 8, 3]]), [[4, 22, 11], [10, 50, 27], [16, 78, 43]])


if __name__ == '__main__':
    unittest.main()