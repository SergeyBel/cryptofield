from cryptofield.ffield import *
from cryptofield.common import *
from cryptofield.boolean import *
import itertools
from random import randint

#polynom a_0+a_1*X+...+a_n-1*X^n = (a_0, a_1,...,a_n-1)


class FPolynom:
  def __init__(self, field, coeffs, isField = False):
    self.field = field
    self.nullElement = FElement(self.field, 0)
    self.oneElement = FElement(self.field, 1)
    if (isField == False):
      self.c = []
      for i in range(len(coeffs)):
        self.c.append(FElement(field, coeffs[i]))
    else:
      self.c = coeffs[:]
    self.__polynomCorrect(self.field, self.c)

  def __polynomCorrect(self, F, x):
    NullElem = FElement(F, 0)
    while (len(x) > 1  and x[-1] == NullElem):
      del x[-1]
    return x
    
  def __add__(self, other):
    return FPolynom(self.field, self.__polynomAdd(self.field, self.c, other.c), True)

  def __polynomAdd(self, F, x, y): 
    lenX = len(x)
    lenY = len(y)
    ans = []
    if lenX > lenY:
      c = x
      m = lenX
      n = lenY
    else:
      c = y
      m = lenY
      n = lenX
    
    for i in range(n):
      ans.append(x[i] + y[i])
    ans[n:m] = c[n:m]
    return self.__polynomCorrect(F, ans)

  def __polynomSub(self, F, x, y): 
    return self.__polynomAdd(F, x, y)
    
  def __sub__(self, other):
    return self + other
    
  def __mul__(self, other):
    return FPolynom(self.field, self.__polynomMul(self.field, self.c, other.c), True)

  def __polynomMul(self, F, x, y):
    lenX = len(x)
    lenY = len(y)
    n = lenX + lenY - 1
    ans = [self.nullElement] * n
    for i in range(0, lenX):
      for j in range(0, lenY):
        ans[i + j] += x[i] * y[j]
    return self.__polynomCorrect(F, ans)

  def __truediv__(self, other):
    (divisor, rest) = self.__polynomDiv(self.field, self.c, other.c)  # x / y
    return FPolynom(self.field, divisor, True)
    
  def __mod__(self, other):
    (divisor, rest) = self.__polynomDiv(self.field, self.c, other.c)  # x % y
    return FPolynom(self.field, rest, True)

  def __pow__(self, n):
    p = FPolynom(self.field, [1])
    x = self.copy()
    while (n):
      if (n & 1):
        p *= x;
        n -= 1
      else:
        x *= x;
        n >>= 1;
    return p

  def __polynomDiv(self, F, x, y):
    degX = self.__degPolynom(F, x)
    degY = self.__degPolynom(F, y)

    n = max(len(x) - len(y) + 1, 1)
    divisor = [self.nullElement] * n
    g = x[:]
    while (degX >= degY):
      p = degX - degY    #divisor degree
      c = g[-1] / y[-1] #divisor coeff
      d = [self.nullElement] * (p + 1)
      d[-1] = c
      divisor = self.__polynomAdd(F, divisor, d)
      z = self.__polynomMul(F, y, d)
      g = self.__polynomSub(F, g, z)
      degX = self.__degPolynom(F, g)
    return (self.__polynomCorrect(F, divisor), self.__polynomCorrect(F, g))
    
  def __len__(self):
    return len(self.c)

  
  def __eq__(self,other):
    return self.field == other.field and self.c == other.c
    
  def __hash__(self):
    s = ""
    for i in range(len(self.c)):
      s = s + str(self.c[i])
    t = tuple(s)
    return hash( (self.field, t) )
    
  def correct(self):
    return FPolynom(self.field, self.__polynomCorrect(self.field, self.c), True)
  
  def deg(self):
    return self.__degPolynom(self.field, self.c)

  def __degPolynom(self, F, coeffs):
    i = len(coeffs) - 1
    while  i >= 0 and coeffs[i] == self.nullElement:
      i = i - 1
    return i
  
  def normalize(self):
    self.correct()
    self.c = self.__polynomNormalize(self.field, self.c)

  def __polynomNormalize(self, F, x):
    c = x[-1]
    normalizator = [FElement(F, F.Inverse(c.f))]
    z = self.__polynomMul(F, x, normalizator)
    return z
    
  def derivative(self):
    """
    f = a_0+a_1*X+...+a_n-1*X^n
    f' = a_1+2*a_2*X+...+(n-1)a_n-1*X^(n-1)
    n * a = a + a + a + ... + a, n times
    """
    t = self.copy()
    t.c.pop(0)
    for i in range(len(t.c)):
      k = self.nullElement
      for j in range(i + 1):
        k = k + t.c[i]
      t.c[i] = k
    return t.correct()
    
  def copy(self):
    return FPolynom(self.field, self.c[:], True)
    
  def value(self, x, isField = True):
    v = self.nullElement
    for i in range(len(self.c)):
      v = v + self.c[i] * self.__fPow(self.field, x, i)
    if (isField == True):
      return v
    else:
      return v.f 

  def __fPow(self, F, x, n):
    p = self.oneElement
    while (n):
      if (n & 1):
        p *= x;
        n -= 1
      else:
        x *= x;
        n >>= 1;
    return p
    
  def values(self, isField = True):
    N = 2 ** self.field.n
    values = []
    for i in range(N):
      values.append(self.value(FElement(self.field, i), isField))
    return values

  def fromPermutation(self, perm, isFieldPerm = False):
    n = 2**self.field.n
    self.c = [self.nullElement] * n
    constants = list()
    for i in range(n):
      constants.append(FElement(self.field, i))

    if (isFieldPerm == False):
      perm = self.__funcToFieldFunc(perm)
    
    for i in range(1, n):
      for j in range(n):
        self.c[i]  += perm[j] * FPow(self.field, constants[j], n - i - 1)
    self.c[0] = perm[0];
    self.correct()

  def __funcToFieldFunc(self, f):
    a = list()
    for i in range(len(f)):
      a.append(FElement(self.field, f[i]))
    return a

  def isLinear(self):
    for i in range(len(self.c)):
      if (not self.c[i] == self.nullElement) and isPowerTwo(i) == False:
        return False
    return True

  def isAffine(self):
    for i in range(len(self.c)):
      if (not self.c[i] == self.nullElement) and isPowerTwo(i) == False and i != 0:
        return False
    return True

  def rank(self):
    rank = 0
    for i in range(len(self.c)):
      if not self.c[i] == self.nullElement:
        rank +=1
    return rank

  #reduce polynom in field using x^q = x
  def reduce(self):
    N = 2**self.field.n
    for i in range(N, len(self.c)):
      j = int ((i / N + i % N) % N)
      if (j == 0):
        j = 1
      self.c[j] += self.c[i]
      self.c[i] = self.nullElement
    self.correct()

  @staticmethod
  def random(F, n):
    N = 2**F.n
    coeffs = list()
    for i in range(n):
      coeffs.append(randint(0, N - 1))
    coeffs.append(randint(1, N - 1))
    return FPolynom(F, coeffs)

  def __str__(self):
    return self.__strPolynom(self.field, self.c)
  
  def texString(self):
    return self.strPolynom(self.field, self.c, False, True)

  
  def __strPolynom(self, F, coeffs, polynom = False, isTex = False):
    s = ""
    if (self.__degPolynom(F, coeffs) == -1):
      return "0"
    n = len(coeffs) - 1
    first = True
    for i in range(n, -1, -1):
      if (coeffs[i] == self.nullElement):
        continue
      if polynom == True:
        coeff = str(coeffs[i])
      else:
        coeff = str(coeffs[i].f)

      if (coeff == '1' and i != 0):
        coeff = ''


      before = " + "
      power = str(i)

      if (isTex == True):
        power = "{" + power + "}"

      if (first == True):
        before = ""
        first = False

      if i == 0:
        monom = coeff
      elif i == 1:
        monom = coeff + 'X'
      else:
        monom = coeff + "X^" + power

      s = s + before + monom

    return s


  

  

  



  

  


