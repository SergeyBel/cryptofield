from cryptofield.permutation import *
import unittest


class TestPermutation(unittest.TestCase):

  def testIsPermutaion1(self):
    p = Permutation([1, 4, 6, 3, 7, 2, 5, 0])
    ans = True
    x = p.isPermutation()
    self.assertEqual(x, ans)

  def testIsPermutaion2(self):
    p = Permutation([1, 1, 1, 1, 1, 1, 1, 1])
    ans = False
    x = p.isPermutation()
    self.assertEqual(x, ans)
  
  def testGetCycles1(self):
    p = Permutation([3, 1, 5, 0, 4, 2])
    answer = [2, 2, 0, 0, 0, 0]
    c = p.getCycles()
    self.assertEqual(c.cycles, answer)
  
  def testInvPermutation1(self):
    p = Permutation([5, 3, 6, 1, 2, 7, 0, 4])
    ans = Permutation([6, 3, 4, 1, 7, 0, 2, 5])
    inv = p.inversePermutation()
    self.assertEqual(inv, ans)
  
  def testNextPermutation1(self):
    p = Permutation([0, 1, 7, 6, 5, 4, 3, 2])
    ans = Permutation([0, 2, 1, 3, 4, 5, 6, 7])
    next = p.nextPermutation()
    self.assertEqual(next, ans)
  
  def testPermCompose1(self):
    f = Permutation([0, 1, 7, 6, 5, 4, 3, 2])
    g = Permutation([7, 1, 6, 5, 4, 3, 2, 0])
    ans = Permutation([7, 1, 0, 2, 3, 4, 5, 6])
    next = PermCompose(g, f)
    self.assertEqual(next, ans)