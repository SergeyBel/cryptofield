import math
from random import randint
from cryptofield.common import *
from cryptofield.boolean.zhegalkin import *


class BooleanFunction:
  def __init__(self, vec):
    self.vec = list(vec)
    self.N = len(vec)
    self.n = int(math.log2(self.N))

  def isLinear(self):
    return self._isLinearVector(self.vec, self.n)

  def _isLinearVector(self, boolVec, n):
    if (n == 0):
      return True
    N = 2**n
    half = int(N / 2)
    if boolVec[0] == boolVec[half]:
      c = 0
    else:
      c = 1
    for i in range(0, half):
      if int(boolVec[i]) != int(boolVec[i + half]) ^ c:
        return False
    return self._isLinearVector(boolVec[:half], n - 1)

  def isMonotone(self):
    return self._isMonotoneVec(self.vec)

  def _isMonotoneVec(self, f):
    length = len(f)
    if length == 1:
      return True
    leftPart = f[:int(length / 2)]
    rightPart = f[int(length / 2):]
    for i in range(len(leftPart)):
      if int(leftPart[i]) > int(rightPart[i]):
        return False
    return self._isMonotoneVec(leftPart) and self._isMonotoneVec(rightPart)

  
  def nonlinearty(self):
    u = "0" * self.n
    maxn = -self.N - 1
    while u != False:
      c = abs(self.__walshCoeff(u))
      if  c > maxn:
        maxn = c
      u = nextBoolVec(u)
      
    return int(2**(self.n - 1) - maxn / 2)
      
  

  def walshSpectrum(self):
    res = list()
    u = "0" * self.n
    while u != False:
      res.append(self.__walshCoeff(u))
      u = nextBoolVec(u)
    return res
  
  def __walshCoeff(self, u):
    #W_f(u) = Sum_(x in V_n)((-1) ^ (f(x) xor <x,u>)
    summa = 0
    x = 0
    while x < self.N:
      p = int(self.vec[x]) ^ scalarBool(valueToBinaryStr(x, self.n), u)
      if p % 2 ==  0:
        summa = summa + 1
      else:
        summa = summa - 1
      x = x + 1
    return summa
  
  def fourierSpectrum(self):
    res = list()
    u = "0" * self.n
    while u != False:
      res.append(self._fourierCoeff(u))
      u = nextBoolVec(u)
    return res
  
  def _fourierCoeff(self, u):
    #F_f(u) = Sum_(x in V_n)(f(x)(-1) ^ (<x,u>))
    summa = 0
    x = 0
    while x < self.N:
      p = scalarBool(valueToBinaryStr(x, self.n), u)
      if p % 2 ==  0:
        summa = summa + int(self.vec[x])
      else:
        summa = summa - int(self.vec[x])
      x = x + 1
    return summa
  
  
  #https://habrahabr.ru/post/275527/
  def anf(self):
    res = [self.vec[0]]
    func = self.vec
    while len(func) != 1:
      coefs = []
      for i in range(0, len(func) - 1):
        coefs.append(str((int(func[i]) ^ int(func[i + 1]))))
      res.append(coefs[0])
      func = coefs
    return anf(res)
  
  
  def deg(self):
    zh = self.anf()
    return zh.deg()


  def nextBoolFunction(self):
    t = nextBoolVec(self.vec)
    return BooleanFunction(t)

  @staticmethod
  def randomBooleanfunction(length):
    vec = ""
    for i in range(0, length):
      vec += str(randint(0, 1))
    return BooleanFunction(vec)

  def __str__(self):
    return "".join(self.vec)

  def __eq__(self, other):
    return self.vec == other.vec
