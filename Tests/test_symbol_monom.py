import sys
sys.path.append("../SymbolPolynom")
from symbol_monom import *
import unittest

class TestSymbolMonom(unittest.TestCase):

  def testSMonomMul1(self):
    a = SMonom('a')
    b = SMonom('b')
    s = a * b
    ans = SMonom(['a', 'b'])
    self.assertEquals(ans, s)

  def testSMonomMul2(self):
    a = SMonom('a')
    b = SMonom('b')
    c = SMonom('c')
    s = c * a * b
    ans = SMonom(['a', 'b', 'c'])
    self.assertEquals(ans, s)

  def testSMonomMul3(self):
    a = SMonom('1')
    b = SMonom('b')
    s =  a * b
    ans = SMonom('b')
    self.assertEquals(ans, s)

  def testSMonomMul4(self):
    a = SMonom('0')
    b = SMonom('b')
    s =  a * b
    ans = SMonom('0')
    self.assertEquals(ans, s)

  def testSMonomMul5(self):
    a = SMonom('a')
    b = SMonom('1')
    s =  a * b
    ans = SMonom('a')
    self.assertEquals(ans, s)

  def testSMonomMul6(self):
    a = SMonom('a')
    b = SMonom('0')
    s =  a * b
    ans = SMonom('0')
    self.assertEquals(ans, s)