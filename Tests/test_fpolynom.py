import sys
sys.path.append("../FieldPolynom")
from field_polynom import *
from field_polynom_algorithms import *
import unittest


class TestBoolean(unittest.TestCase):
  def testAdd1(self):
    F = FField(4)
    x = FPolynom(F, [1, 0, 5, 15])
    y = FPolynom(F, [0, 7, 8, 3])
    z = x + y
    answer = FPolynom(F, [1, 7, 13, 12])
    self.assertEquals(z, answer)
    
  def testAdd2(self):
    F = FField(5)
    x = FPolynom(F, [1, 4, 17, 30])
    y = FPolynom(F, [1, 4, 17, 30])
    z = x + y
    answer = FPolynom(F, [0])
    self.assertEquals(z, answer)
    
  def testSub1(self):
    F = FField(4)
    x = FPolynom(F, [1, 0, 5, 15])
    y = FPolynom(F, [0, 7, 8])
    z = x - y
    answer = FPolynom(F, [1, 7, 13, 15])
    self.assertEquals(z, answer)
    
    
  def testMul1(self):
    F = FField(2)
    x = FPolynom(F, [1, 1])
    y = FPolynom(F, [1, 1])
    z = x * y
    answer = FPolynom(F, [1, 0, 1])
    self.assertEquals(z, answer)
    
  def testMul2(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 1])
    y = FPolynom(F, [0, 1])
    answer = FPolynom(F, [0, 1, 0, 1])
    z = x * y
    self.assertEquals(z, answer)
    
  def testMul3(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 3])
    y = FPolynom(F, [3, 2])
    answer = FPolynom(F, [3, 3, 1, 1])
    z = x * y
    self.assertEquals(z, answer)
    
  def testMul4(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 2, 3])
    y = FPolynom(F, [0])
    answer = FPolynom(F, [0])
    z = x * y
    self.assertEquals(z, answer)
    
  def testDiv1(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 2])
    y = FPolynom(F, [1, 0, 2 ,3])
    answer = FPolynom(F, [0])
    z = x / y
    self.assertEquals(z, answer)
    
  def testDiv2(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 3])
    y = FPolynom(F, [1, 1])
    answer = FPolynom(F, [1, 3])
    z = x / y
    self.assertEquals(z, answer)
    
  def testDiv3(self):
    F = FField(6)
    x = FPolynom(F, [20, 22, 15, 17])
    y = FPolynom(F, [0, 25, 14, 18])
    c = FPolynom(F, [31, 25, 50])
    d = x * y + c
    answer = x
    z = d / y
    self.assertEquals(z, answer)
    
  def testDiv4(self):
    F = FField(2)
    x = FPolynom(F, [1, 2, 2, 3])
    y = FPolynom(F, [1, 1, 1, 1])
    answer = FPolynom(F, [3])
    z = x / y
    self.assertEquals(z, answer)
    
  def testMod1(self):
    F = FField(2)
    x = FPolynom(F, [1, 2 ,3])
    y = FPolynom(F, [1, 1])
    answer = FPolynom(F, [0])
    z = x % y
    self.assertEquals(z, answer)
    
  def testMod2(self):
    F = FField(6)
    x = FPolynom(F, [20, 22, 15, 17])
    y = FPolynom(F, [0, 25, 14, 18])
    c = FPolynom(F, [31, 25, 50])
    d = x * y + c
    answer = c
    z = d % y
    self.assertEquals(z, answer)
    
  def testEquilid1(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 1])
    y = FPolynom(F, [3, 2, 1])
    z = PolynomEquilid(F, x, y)
    answer = FPolynom(F, [1, 1])
    self.assertEquals(z, answer)

  def testEquilid2(self):
    F = FField(8)
    a = FPolynom(F, [35, 22, 15, 89, 64])
    x = FPolynom(F, [1, 23, 45, 176, 90, 87, 65, 30])
    y = x * a
    z = PolynomEquilid(F, x, y)
    answer = PolynomEquilid(F, x, x)
    self.assertEquals(z, answer)
  
  def testDerivative1(self):
    F = FField(8)
    x = FPolynom(F, [1, 23, 45, 176, 90, 87, 65, 30])
    y = x.Derivative()
    answer = FPolynom(F, [23, 0, 176, 0, 87, 0, 30])
    self.assertEquals(y, answer)

  def testIsLinear1(self):
    F = FField(2)
    x = FPolynom(F, [0, 1, 1, 0, 1, 0, 0, 0, 1])
    answer = True
    self.assertEquals(x.IsLinear(), answer)

  def testIsLinear2(self):
    F = FField(4)
    x = FPolynom(F, [0, 1, 1, 3, 1, 0, 0, 0, 1])
    answer = False
    self.assertEquals(x.IsLinear(), answer)

  def testIsAffine1(self):
    F = FField(2)
    x = FPolynom(F, [1, 1, 1, 0, 1, 0, 0, 0, 1])
    answer = True
    self.assertEquals(x.IsAffine(), answer)

  def testIsAffine2(self):
    F = FField(4)
    x = FPolynom(F, [3, 1, 1, 0, 1, 0, 0, 2, 1])
    answer = False
    self.assertEquals(x.IsAffine(), answer)

  def testRank1(self):
    F = FField(4)
    x = FPolynom(F, [3, 1, 1, 0, 1, 0, 0, 2, 1])
    answer = 6
    self.assertEquals(x.Rank(), answer)

  def testReduce1(self):
    F = FField(2)
    f = FPolynom(F, [1, 1, 1, 1, 1])
    f.Reduce()
    answer = FPolynom(F,[1, 0, 1, 1])
    self.assertEquals(f, answer)

  def testReduce2(self):
    F = FField(4)
    f = FPolynom(F, [0, 0, 0, 0, 4, 13, 3, 7, 10, 13, 8, 5, 12, 4, 15, 1, 8, 14, 10, 11, 12, 11, 11, 0, 2, 9, 13, 0, 14, 0, 0, 0, 2])
    f.Reduce()
    answer = FPolynom(F, [0, 8, 12, 10, 15, 1, 8, 12, 10, 15, 1, 8, 12, 10, 15, 1])
    self.assertEquals(f, answer)

  def testFromZhekalkinPolynom1(self):
    F = FField(2)
    f = "0011"
    zhekalkin = ZhegalkinPolynom(f)
    g = FromZhekalkinPolynom(F, zhekalkin)
    answer = FPolynom(F, [0, 1, 1])
    self.assertEquals(g, answer)

  def testFromZhekalkinPolynom2(self):
    F = FField(2)
    f = "0001"
    zhekalkin = ZhegalkinPolynom(f)
    g = FromZhekalkinPolynom(F, zhekalkin)
    answer = FPolynom(F, [0, 2, 3, 1])
    self.assertEquals(g, answer)

  def testFromZhekalkinPolynom3(self):
    F = FField(2)
    f = "0110"
    zhekalkin = ZhegalkinPolynom(f)
    g = FromZhekalkinPolynom(F, zhekalkin)
    answer = FPolynom(F, [0, 2, 3])
    self.assertEquals(g, answer)

  def testFromZhekalkinPolynom4(self):
    F = FField(4)
    f = "0"*15 + "1"
    zhekalkin = ZhegalkinPolynom(f)
    g = FromZhekalkinPolynom(F, zhekalkin)
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    self.assertEquals(g.Values(False), answer)

  def testPow1(self):
    F = FField(2)
    x = PolynomPow(F, FPolynom(F, [0, 1, 1]), 2)
    answer = FPolynom(F, [0, 0, 1, 0, 1])
    self.assertEquals(x, answer)

  def testPow2(self):
    F = FField(2)
    x = PolynomPow(F, FPolynom(F, []), 1)
    answer = FPolynom(F, [])
    self.assertEquals(x, answer)

  def testPow3(self):
    F = FField(2)
    x = PolynomPow(F, FPolynom(F, []), 0)
    answer = FPolynom(F, [1])
    self.assertEquals(x, answer)

  def testFromPermutation1(self):
    F = FField(2)
    f = [1, 3, 0, 2] #t*x^2 + 1
    answer = FPolynom(F, [FElement(F, 1), FElement(F, 0), FElement(F, 2), FElement(F, 0)], True)
    pol = FPolynom(F, [])
    pol.FromPermutation(f)
    self.assertEquals(pol, answer)

  def testFromPermutation2(self):
    F = FField(2)
    f = [1, 2, 2, 0] #x^3 + x^2 + x(t + 1) + 1
    answer = FPolynom(F, [1, 3, 1, 1])
    pol = FPolynom(F, [])
    pol.FromPermutation(f)
    self.assertEquals(pol, answer)

  def testFromPermutation3(self):
    F = FField(2)
    f = [1, 1, 1, 1] 
    answer = f
    pol = FPolynom(F, [])
    pol.FromPermutation(f)
    self.assertEquals(pol.Values(False), answer)

  def testDeg(self):
    F = FField(2)
    f = [1, 3, 0, 2] #t*x^2 + 1
    answer = 2
    pol = FPolynom(F, [])
    pol.FromPermutation(f)
    self.assertEquals(pol.Deg(), answer)