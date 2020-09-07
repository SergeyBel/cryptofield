import sys
sys.path.append("../FieldPolynom")
sys.path.append("../Algorithms")
from field_polynom import *
from field_polynom_algorithms import *
from Berlekamp import *
import unittest


class TestFPolynomAlgorithms(unittest.TestCase):
  def testBerlekamp1(self):
    F = FField(1)
    #x^8 + x^6 + x^4 + x^3 + x^1 = (1 + x + x^2)(1 + x + x^4 + x^5 + x^6)
    f = FPolynom(F, [1, 0, 0, 1, 1, 0, 1, 0, 1])
    x = Berlekamp(F, f)
    y = FPolynom(F, [1])
    for t in x:
      y = y * t
    self.assertEquals(y, f)
  
  def testBerlekamp2(self):
    F = FField(1)
    #x^2 + x = x * (x + 1)
    f = FPolynom(F, [0, 1, 1])
    x = Berlekamp(F, f)
    for t in x:
      y = FPolynom(F, [1])
    for t in x:
      y = y * t
    self.assertEquals(y, f)
  
  def testBerlekamp3(self):
    F = FField(1)
    #x^4 + x^3 + x = x * (x^3 + x^2 + 1)
    f = FPolynom(F, [0, 1, 0, 1, 1])
    x = Berlekamp(F, f)
    answer = False
    if (x[0] == FPolynom(F, [0, 1]) and x[1] == FPolynom(F, [1, 0, 1, 1])):
      answer = True
    
    if (x[1] == FPolynom(F, [0, 1]) and x[0] == FPolynom(F, [1, 0, 1, 1])):
      answer = True
    
    self.assertEquals(answer, True)
  
  def testBerlekamp4(self):
    F = FField(4)
    #6 + 14x^2 = 13(14+x)(14+x)
    f = FPolynom(F, [6, 0, 13])
    x = Berlekamp(F, f)
    p = FPolynom(F, [1])
    for t in x:
      p = p * t
    self.assertEquals(f, p)
    
  def testDualBasis(self):
    F = FField(4)
    dualBasis = DualBasis(F)
    answer = [FElement(F, 9), FElement(F, 4), FElement(F, 2), FElement(F, 1)]
    self.assertEquals(dualBasis, answer)