import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.main.assignment_3 import (  
    Gaussian_Elimination,
    L_U_Factor,
    Diag_Dom,
    Positive_Definite
)

class TestAssignment2(unittest.TestCase):
  def test_1_Gaussian_Elimination(self):
    arr = np.array([
        [2, -1, 1],
        [1, 3, 1],
        [-1, 5, 4]
    ])
    arr_2 = np.array([6, 0, -3])
    print(Gaussian_Elimination(arr, arr_2))
    print()
    return
     
  def test_2_L_U_Factor(self):
    arr = np.array([
        [1, 1, 0, 3],
        [2, 1, -1, 1],
        [3, -1, -1, 2],
        [-1, 2, 3, -1]
    ])
    det, L, U = L_U_Factor(arr)
    print(det)
    print()
    print(L)
    print()
    print(U)
    print()
    return

  def test_3_Diag_Down(self):
    arr = np.array([
    [9, 0, 5, 2, 1],
    [3, 9, 1, 2, 1],
    [0, 1, 7, 2, 3],
    [4, 2, 3, 12, 2],
    [3, 2, 4, 0, 8]
    ])
    print(Diag_Dom(arr))
    print()
    return

  def test_4_Positive_Definite(self):
    arr = np.array([
        [2, 2, 1],
        [2, 3, 0],
        [1, 0, 2]
    ])
    print(Positive_Definite(arr))
    print()
    return 

class NoDotsTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        pass 

class NoDotsTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return NoDotsTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == "__main__":
    unittest.main(testRunner=NoDotsTestRunner(), verbosity=0)