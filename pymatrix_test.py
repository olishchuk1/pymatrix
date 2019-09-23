import unittest
from pprint import pprint

from pymatrix import Pymatrix
from sole import Sole


# class PymatrixTest(unittest.TestCase):
#
#     def testtest(self):
#         self.assertEqual(True, True)
#
#     # NEED TO BE FIXED
#     def test_madition(self):
#         mat = Pymatrix([[1, 2, 3], [6, 5, 4]])
#         self.assertEqual(mat.maddition([[1, 3, 5], [4, 2, 3]]), [[2, 5, 8], [10, 7, 7]])
#
#     def test_mmultiply(self):
#         mat = Pymatrix([[1, 2], [3, 4], [5, 6]])
#         self.assertEqual(mat.mmultiply([[2, 6, 5], [1, 8, 3]]), [[4, 22, 11], [10, 50, 27], [16, 78, 43]])




if __name__ == '__main__':
    mat = Sole([[1, 2, 3, 4], [5, 2, 4, 5], [2, 4, 5, 6], [6, 4, 2, 3]], [[4], [2], [3], [2]])
    mat.gauss_inverted_matrix()
