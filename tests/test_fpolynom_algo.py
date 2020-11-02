from cryptofield.fieldpolynom import *
from cryptofield.algorithms import *
import unittest


class TestFPolynomAlgorithms(unittest.TestCase):

  def testEquilid1(self):
    F = FField(2)
    x = FPolynom(F, [1, 0, 1])
    y = FPolynom(F, [3, 2, 1])
    z = PolynomEquilid(F, x, y)
    answer = FPolynom(F, [1, 1])
    self.assertEqual(z, answer)

  def testEquilid2(self):
    F = FField(8)
    a = FPolynom(F, [35, 22, 15, 89, 64])
    x = FPolynom(F, [1, 23, 45, 176, 90, 87, 65, 30])
    y = x * a
    z = PolynomEquilid(F, x, y)
    answer = PolynomEquilid(F, x, x)
    self.assertEqual(z, answer)



  def testBerlekamp1(self):
    F = FField(1)
    #x^8 + x^6 + x^4 + x^3 + x^1 = (1 + x + x^2)(1 + x + x^4 + x^5 + x^6)
    f = FPolynom(F, [1, 0, 0, 1, 1, 0, 1, 0, 1])
    x = Berlekamp(F, f)
    y = FPolynom(F, [1])
    for t in x:
      y = y * t
    self.assertEqual(y, f)
  
  def testBerlekamp2(self):
    F = FField(1)
    #x^2 + x = x * (x + 1)
    f = FPolynom(F, [0, 1, 1])
    x = Berlekamp(F, f)
    for t in x:
      y = FPolynom(F, [1])
    for t in x:
      y = y * t
    self.assertEqual(y, f)
  
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
    
    self.assertEqual(answer, True)
  
  def testBerlekamp4(self):
    F = FField(4)
    #6 + 14x^2 = 13(14+x)(14+x)
    f = FPolynom(F, [6, 0, 13])
    x = Berlekamp(F, f)
    p = FPolynom(F, [1])
    for t in x:
      p = p * t
    self.assertEqual(f, p)
