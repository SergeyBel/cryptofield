from cryptofield.permutation import *
import unittest


class TestPermutation(unittest.TestCase):

  def testIsPermutaion1(self):
    p = [1, 4, 6, 3, 7, 2, 5, 0]
    ans = True
    x = IsPermutation(p)
    self.assertEqual(x, ans)

  def testIsPermutaion2(self):
    p = [1, 1, 1, 1, 1, 1, 1, 1]
    ans = False
    x = IsPermutation(p)
    self.assertEqual(x, ans)
  
  def testGetCycles1(self):
    f = [3, 1, 5, 0, 4, 2]
    answer = [2, 2, 0, 0, 0, 0]
    c = GetCycles(f)
    st = CycleStruct(c)
    self.assertEqual(st, answer)
  
  def testInvPermutation1(self):
    f = [5, 3, 6, 1, 2, 7, 0, 4]
    ans = [6, 3, 4, 1, 7, 0, 2, 5]
    inv = InvPermutation(f)
    self.assertEqual(inv, ans)
  
  def testNextPermutation1(self):
    f = [0, 1, 7, 6, 5, 4, 3, 2]
    ans = [0, 2, 1, 3, 4, 5, 6, 7]
    next = NextPermutation(f)
    self.assertEqual(next, ans)
  
  def testPermCompose1(self):
    f = [0, 1, 7, 6, 5, 4, 3, 2]
    g = [7, 1, 6, 5, 4, 3, 2, 0]
    ans = [7, 1, 0, 2, 3, 4, 5, 6]
    next = PermCompose(g, f)
    self.assertEqual(next, ans)