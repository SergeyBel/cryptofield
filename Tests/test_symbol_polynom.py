import sys
sys.path.append("../SymbolPolynom")
from symbol_polynom import *
import unittest

class TestSymbolPolynom(unittest.TestCase):
  def testSPolynomAdd1(self):
    a = SPolynom([SElement('a')])
    b = SPolynom([SElement('b')])
    ans = SPolynom([SElement([SMonom('a'), SMonom('b')])])
    self.assertEquals(ans, a + b)

  def testSPolynomAdd2(self):
    a = SPolynom([SElement('a'), SElement('c')])
    b = SPolynom([SElement('a')])
    ans = SPolynom([SElement([]), SElement('c')])
    self.assertEquals(ans, a + b)

  def testSPolynomAdd3(self):
    a = SPolynom([SElement('a')])
    b = SPolynom([SElement('a')])
    ans = SPolynom([SElement('0')])
    self.assertEquals(ans, a + b)

  def testSPolynomAdd4(self):
    a = SPolynom([SElement('a'), SElement('b'), SElement('c')])
    b = SPolynom([SElement('b'), SElement('c'), SElement('a')])
    ans = SPolynom([SElement(['a', 'b']), SElement(['b', 'c']), SElement(['a', 'c'])])
    self.assertEquals(ans, a + b)

  def testSPolynomMul1(self):
    a = SPolynom([SElement('a')])
    b = SPolynom([SElement('b')])
    ans = SPolynom([SElement([SMonom(['a', 'b'])])])
    self.assertEquals(ans, a * b)

  def testSPolynomMul2(self):
    a = SPolynom([SElement('a')])
    b = SPolynom([SElement('a')])
    ans = SPolynom([SElement(['a'])])
    self.assertEquals(ans, a * b)

  def testSPolynomMul3(self):
    a = SPolynom([SElement('a'), SElement('b')])
    b = SPolynom([SElement('c')])
    ans = SPolynom([SElement(SMonom(['a', 'c'])), SElement(SMonom(['b', 'c']))])
    self.assertEquals(ans, a * b)

  def testSPolynomMul4(self):
    a = SPolynom([SElement('a'), SElement('b')])
    b = SPolynom([SElement('c'), SElement('d')])
    ans = SPolynom([SElement(SMonom(['a', 'c'])), SElement([SMonom(['b', 'c']), SMonom(['a', 'd'])]), SElement(SMonom(['b', 'd']))])
    self.assertEquals(ans, a * b)

  def testSPolynomMul5(self):
    a = SPolynom([SElement('a'), SElement('1')])
    b = SPolynom([SElement('c')])
    ans = SPolynom([SElement(SMonom(['a', 'c'])), SElement(['c'])])
    self.assertEquals(ans, a * b)

  def testSPolynomMul6(self):
    a = SPolynom([SElement('a'), SElement('1')])
    b = SPolynom([SElement('a'), SElement('0'), SElement('1')])
    ans = SPolynom([SElement(['a']), SElement(['a']), SElement(['a']), SElement(['1'])])
    self.assertEquals(ans, a * b)

  def testSPolynoPow1(self):
    a = SPolynom([SElement('a')])
    ans = a
    self.assertEquals(ans, a ** 2)

  def testSPolynoPow2(self):
    a = SPolynom([SElement('a'), SElement('b')])
    ans = SPolynom([SElement('a'), SElement([]), SElement('b')])
    self.assertEquals(ans, a ** 2)

  def testSPolynomExpr1(self):
    a = SPolynom([SElement('a'), SElement('1')])
    b = SPolynom([SElement('a'), SElement('b'), SElement('1')])
    ans = SPolynom([SElement('a'), SElement('a'), SElement(SMonom(['a', 'b'])), SElement('b'), SElement('a'), SElement('1')]) 
    self.assertEquals(ans, a * b ** 2)

  def testSPolynomShift1(self):
    a = SPolynom([SElement('a'), SElement('1')])
    ans = SPolynom([SElement('0'),SElement('a'), SElement('1')])
    self.assertEquals(ans, a.shift(1))

  def testSPolynomShift2(self):
    a = SPolynom([SElement('a'), SElement('1')])
    ans = SPolynom([SElement('0'), SElement('0'), SElement('a'), SElement('1')])
    self.assertEquals(ans, a.shift(2))

  def testSPolynomShift3(self):
    a = SPolynom([SElement('a'), SElement('1')])
    ans = a
    self.assertEquals(ans, a.shift(0))

  def testSPolynomPow1(self):
    a = SPolynom([SElement('a'), SElement('b')])
    ans = SPolynom([SElement('a'), SElement(SMonom(['a', 'b'])), SElement(SMonom(['a', 'b'])), SElement('b')])
    self.assertEquals(ans, a ** 3)

  def testSPolynomPow2(self):
    a = SPolynom([SElement('a'), SElement('b')])
    ans = SPolynom([SElement('1')])
    self.assertEquals(ans, a ** 0)

  def testSPolynomPow3(self):
    a = SPolynom([SElement('a'), SElement('b')])
    ans = SPolynom([SElement('a'), SElement('b')])
    self.assertEquals(ans, a ** 1)

  def testSPolynomPow4(self):
    a = SPolynom([SElement('a'), SElement('b'), SElement('c')])
    ansCoeff = [SElement('0')] * 17
    ansCoeff[0] = SElement('a')
    ansCoeff[8] = SElement('b')
    ansCoeff[16] = SElement('c')
    ans = SPolynom(ansCoeff)
    self.assertEquals(ans, a ** 8)