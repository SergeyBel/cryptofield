import sys
sys.path.append("../SymbolPolynom")
from symbol_element import *
import unittest

class TestSymbolElement(unittest.TestCase):

  def testSElementAdd1(self):
    a = SElement([SMonom('a')])
    b = SElement([SMonom('b')])
    ans = SElement([SMonom('a'), SMonom('b')])
    self.assertEquals(ans, a + b)

  def testSElementAdd2(self):
    a = SElement([SMonom('a')])
    b = SElement([SMonom('b')])
    c = SElement([SMonom('c')])
    ans = SElement([SMonom('a'), SMonom('b'), SMonom('c')])
    self.assertEquals(ans, c + a + b)

  def testSElementAdd3(self):
    a = SElement([SMonom('a')])
    b = SElement([SMonom('a')])
    ans = SElement(['0'])
    self.assertEquals(ans, a + b)

  def testSElementAdd4(self):
    a = SElement([SMonom('a')])
    b = SElement([SMonom('0')])
    ans = SElement(['a'])
    self.assertEquals(ans, a + b)

  def testSElementAdd5(self):
    a = SElement([SMonom('1')])
    b = SElement([SMonom('a')])
    ans = SElement(['a', '1'])
    self.assertEquals(ans, a + b)

  def testSElementAdd6(self):
    a = SElement('a1')
    b = SElement('a2')
    ans = SElement(['a1', 'a2'])
    self.assertEquals(ans, a + b)

  def testSElementMul1(self):
    a = SElement([SMonom('a')])
    b = SElement([SMonom('a')])
    ans = SElement([SMonom('a')])
    self.assertEquals(ans, a * b)

  def testSElementMul2(self):
    a = SElement([SMonom('a')])
    b = SElement([SMonom('b')])
    ans = SElement([SMonom(['a', 'b'])])
    self.assertEquals(ans, a * b)

  def testSElementMul3(self):
    a = SElement([SMonom('a')])
    b = SElement([SMonom('b'), SMonom('c')])
    ans = SElement([SMonom(['a', 'b']), SMonom(['a', 'c'])])
    self.assertEquals(ans, a * b)

  def testSElementMul4(self):
    a = SElement([SMonom('1')])
    b = SElement([SMonom('b')])
    ans = SElement([SMonom('b')])
    self.assertEquals(ans, a * b)

  def testSElementMul5(self):
    a = SElement([SMonom('0')])
    b = SElement([SMonom('b')])
    ans = SElement([SMonom('0')])
    self.assertEquals(ans, a * b)

  def testSElementMul6(self):
    a = SElement([SMonom(['a', 'b', 'c']), SMonom(['b', 'c'])])
    b = SElement([SMonom('a')])
    ans = SElement([SMonom('0')])
    self.assertEquals(ans, a * b)