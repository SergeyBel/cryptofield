import sys
sys.path.append("../FieldMatrix")
from fieldmatrix import *
import unittest


class TestFMatrix(unittest.TestCase):
  def testMatrixGetRow1(self):
    F = FField(4)
    m = FMatrix(F, 3, 3)
    m.Ident()
    r = m.GetRow(1)
    ans = [FElement(F, 0), FElement(F, 1), FElement(F, 0)]
    self.assertEquals(r, ans)

  def testMatrixGetColumn1(self):
    F = FField(4)
    m = FMatrix(F, 5, 5)
    m.Ident()
    r = m.GetColumn(0)
    ans = [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 0), FElement(F, 0)]
    self.assertEquals(r, ans)

  def MatrixInverse():
    F = FField(2)
    m = FMatrix(F, 4, 4)
    m.SetRow(0, [FElement(F, 0), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
    m.SetRow(1, [FElement(F, 0), FElement(F, 0), FElement(F, 1), FElement(F, 0)])
    m.SetRow(2, [FElement(F, 0), FElement(F, 1), FElement(F, 0), FElement(F, 0)])
    m.SetRow(3, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
    inv = m.Inverse()
    ans = FMatrix(F, 4, 4)
    ans.SetRow(0, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
    ans.SetRow(1, [FElement(F, 0), FElement(F, 0), FElement(F, 1), FElement(F, 0)])
    ans.SetRow(2, [FElement(F, 0), FElement(F, 1), FElement(F, 0), FElement(F, 0)])
    ans.SetRow(3, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 0)])
    self.assertEquals(inv, ans)