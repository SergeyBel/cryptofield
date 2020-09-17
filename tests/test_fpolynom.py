from cryptofield.fieldpolynom import *
import unittest


class TestFpolynom(unittest.TestCase):
  def testAdd1(self):
    F = FField(4)
    x = FPolynom(F, [1, 0, 5, 15])
    y = FPolynom(F, [0, 7, 8, 3])
    z = x + y
    answer = FPolynom(F, [1, 7, 13, 12])
    self.assertEqual(z, answer)
    
  def testAdd2(self):
    F = FField(5)
    x = FPolynom(F, [1, 4, 17, 30])
    y = FPolynom(F, [1, 4, 17, 30])
    z = x + y
    answer = FPolynom(F, [0])
    self.assertEqual(z, answer)
    
  def testSub1(self):
    F = FField(4)
    x = FPolynom(F, [1, 0, 5, 15])
    y = FPolynom(F, [0, 7, 8])
    z = x - y
    answer = FPolynom(F, [1, 7, 13, 15])
    self.assertEqual(z, answer)
    
    
  def testMul1(self):
    F = FField(2)
    x = FPolynom(F, [1, 1])
    y = FPolynom(F, [1, 1])
    z = x * y
    answer = FPolynom(F, [1, 0, 1])
    self.assertEqual(z, answer)
    
  def testMul2(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 1])
    y = FPolynom(F, [0, 1])
    answer = FPolynom(F, [0, 1, 0, 1])
    z = x * y
    self.assertEqual(z, answer)
    
  def testMul3(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 3])
    y = FPolynom(F, [3, 2])
    answer = FPolynom(F, [3, 3, 1, 1])
    z = x * y
    self.assertEqual(z, answer)
    
  def testMul4(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 2, 3])
    y = FPolynom(F, [0])
    answer = FPolynom(F, [0])
    z = x * y
    self.assertEqual(z, answer)
    
  def testDiv1(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 2])
    y = FPolynom(F, [1, 0, 2 ,3])
    answer = FPolynom(F, [0])
    z = x / y
    self.assertEqual(z, answer)
    
  def testDiv2(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 3])
    y = FPolynom(F, [1, 1])
    answer = FPolynom(F, [1, 3])
    z = x / y
    self.assertEqual(z, answer)
    
  def testDiv3(self):
    F = FField(6)
    x = FPolynom(F, [20, 22, 15, 17])
    y = FPolynom(F, [0, 25, 14, 18])
    c = FPolynom(F, [31, 25, 50])
    d = x * y + c
    answer = x
    z = d / y
    self.assertEqual(z, answer)
    
  def testDiv4(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 2, 3])
    y = FPolynom(F, [1, 1, 1, 1])
    answer = FPolynom(F, [3])
    z = x / y
    self.assertEqual(z, answer)
    
  def testMod1(self):
    F = FField(2)
    x = FPolynom(F, [1, 2 ,3])
    y = FPolynom(F, [1, 1])
    answer = FPolynom(F, [0])
    z = x % y
    self.assertEqual(z, answer)
    
  def testMod2(self):
    F = FField(6)
    x = FPolynom(F, [20, 22, 15, 17])
    y = FPolynom(F, [0, 25, 14, 18])
    c = FPolynom(F, [31, 25, 50])
    d = x * y + c
    answer = c
    z = d % y
    self.assertEqual(z, answer)

  def testPow1(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 2, 3])
    n = 1
    answer = x
    z = x ** n
    self.assertEqual(z, answer)

  def testPow2(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 2, 3])
    n = 0
    answer = FPolynom(F, [1])
    z = x ** n
    self.assertEqual(z, answer)

  def testPow3(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 1])
    n = 2
    answer = FPolynom(F, [1, 0, 0, 0, 1])
    z = x ** n
    self.assertEqual(z, answer)
    
  
  def testDerivative1(self):
    F = FField(8)
    x = FPolynom(F, [1, 23, 45, 176, 90, 87, 65, 30])
    y = x.derivative()
    answer = FPolynom(F, [23, 0, 176, 0, 87, 0, 30])
    self.assertEqual(y, answer)

  def testIsLinear1(self):
    F = FField(2)
    x = FPolynom(F, [0, 1, 1, 0, 1, 0, 0, 0, 1])
    answer = True
    self.assertEqual(x.isLinear(), answer)

  def testIsLinear2(self):
    F = FField(4)
    x = FPolynom(F, [0, 1, 1, 3, 1, 0, 0, 0, 1])
    answer = False
    self.assertEqual(x.isLinear(), answer)

  def testIsAffine1(self):
    F = FField(2)
    x = FPolynom(F, [1, 1, 1, 0, 1, 0, 0, 0, 1])
    answer = True
    self.assertEqual(x.isAffine(), answer)

  def testIsAffine2(self):
    F = FField(4)
    x = FPolynom(F, [3, 1, 1, 0, 1, 0, 0, 2, 1])
    answer = False
    self.assertEqual(x.isAffine(), answer)

  def testRank1(self):
    F = FField(4)
    x = FPolynom(F, [3, 1, 1, 0, 1, 0, 0, 2, 1])
    answer = 6
    self.assertEqual(x.rank(), answer)

  def testReduce1(self):
    F = FField(2)
    f = FPolynom(F, [1, 1, 1, 1, 1])
    f.reduce()
    answer = FPolynom(F,[1, 0, 1, 1])
    self.assertEqual(f, answer)

  def testReduce2(self):
    F = FField(4)
    f = FPolynom(F, [0, 0, 0, 0, 4, 13, 3, 7, 10, 13, 8, 5, 12, 4, 15, 1, 8, 14, 10, 11, 12, 11, 11, 0, 2, 9, 13, 0, 14, 0, 0, 0, 2])
    f.reduce()
    answer = FPolynom(F, [0, 8, 12, 10, 15, 1, 8, 12, 10, 15, 1, 8, 12, 10, 15, 1])
    self.assertEqual(f, answer)

  def testFromPermutation1(self):
    F = FField(2)
    f = [1, 3, 0, 2] #t*x^2 + 1
    answer = FPolynom(F, [FElement(F, 1), FElement(F, 0), FElement(F, 2), FElement(F, 0)], True)
    pol = FPolynom(F, [])
    pol.fromPermutation(f)
    self.assertEqual(pol, answer)

  def testFromPermutation2(self):
    F = FField(2)
    f = [1, 2, 2, 0] #x^3 + x^2 + x(t + 1) + 1
    answer = FPolynom(F, [1, 3, 1, 1])
    pol = FPolynom(F, [])
    pol.fromPermutation(f)
    self.assertEqual(pol, answer)

  def testFromPermutation3(self):
    F = FField(2)
    f = [1, 1, 1, 1] 
    answer = f
    pol = FPolynom(F, [])
    pol.fromPermutation(f)
    self.assertEqual(pol.values(False), answer)

  def testDeg(self):
    F = FField(2)
    f = [1, 3, 0, 2] #t*x^2 + 1
    answer = 2
    pol = FPolynom(F, [])
    pol.fromPermutation(f)
    self.assertEqual(pol.deg(), answer)

