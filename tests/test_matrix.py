from cryptofield.fieldmatrix import *
import unittest


class TestFMatrix(unittest.TestCase):
  def testMatrixGetRow1(self):
    F = FField(4)
    m = FMatrix(F, 3, 3)
    m.ident()
    r = m.getRow(1)
    ans = [FElement(F, 0), FElement(F, 1), FElement(F, 0)]
    self.assertEqual(r, ans)

  def testMatrixGetColumn1(self):
    F = FField(4)
    m = FMatrix(F, 5, 5)
    m.ident()
    r = m.getColumn(0)
    ans = [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 0), FElement(F, 0)]
    self.assertEqual(r, ans)

  def testMatrixInverse1(self):
    F = FField(2)
    m = FMatrix(F, 4, 4)
    m.setRow(0, [FElement(F, 0), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
    m.setRow(1, [FElement(F, 0), FElement(F, 0), FElement(F, 1), FElement(F, 0)])
    m.setRow(2, [FElement(F, 0), FElement(F, 1), FElement(F, 0), FElement(F, 0)])
    m.setRow(3, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
    inv = m.inverse()
    ans = FMatrix(F, 4, 4)
    ans.setRow(0, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
    ans.setRow(1, [FElement(F, 0), FElement(F, 0), FElement(F, 1), FElement(F, 0)])
    ans.setRow(2, [FElement(F, 0), FElement(F, 1), FElement(F, 0), FElement(F, 0)])
    ans.setRow(3, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 0)])
    self.assertEqual(inv, ans)