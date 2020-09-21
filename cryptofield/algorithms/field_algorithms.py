from cryptofield.fieldpolynom import *
from cryptofield.fieldmatrix import *

def PolynomEquilid(F, x, y):
  if (x.deg() < y.deg()):
    f = y.copy()
    g = x.copy()
  else:
    f = x.copy()
    g = y.copy()
    
  polNull = FPolynom(F, [0])
  
  if g == polNull:
    return f
    
  while True:
    r = f % g
    if r == polNull:
      break
    f = g
    g = r
  g.normalize()
  return g


#return FPolynom Tr(b*x)
def CreateTr(F, betta):
  n = F.n
  coeffs = [FElement(F, 0)] * 2**n
  for i in range(n):
    j = 2**i
    c = FPow(F, betta, 2**i)
    coeffs[j] = c
  return FPolynom(F, coeffs, True)
  
def DualBasis(F):
  n = F.n
  alpha = FElement(F, 2)
  basis = list()
  dualBasis = list()
  tr = CreateTr(F, FElement(F, 1))

  a = FMatrix(F, n, n)
  for i in range(n):
    for j in range(i + 1):
      a[j, i] = a[i, j] = tr.value(FPow(F, alpha, i + j))
  b = a.inverse()
  for i in range(n):
    num = ""
    t = b.getRow(i)
    for j in range(len(t)):
      num += str(t[j].f)
    dualBasis.append(FElement(F, binaryStrToValue(num[::-1])))
  return dualBasis

def FromZhekalkinPolynom(F, coeffs):
  n = F.n
  coords = []
  dualBasis = DualBasis(F)
  dualBasis = dualBasis[::-1]
  f = FPolynom(F, [])
  for i in range(n):
    coords.append(CreateTr(F, dualBasis[i]))
  for i in range(len(coeffs)):
    if (coeffs[i] == "1"):
      monom = FPolynom(F, [1])
      decomp = list(valueToBinaryStr(i, n))
      for j in range(n):
        if decomp[j] == "1":
          monom *= coords[j]
      f += monom
  f.reduce()
  return f


def IrreducibleProduct(F, n):
  divisors = numberDivisors(n)
  f = FPolynom(F, [1])
  for d in divisors:
    c = [0] * (2**(n / d) + 1)
    c[1] = 1
    c[2**(n / d)] = 1
    g = FPolynom(F, c)
    m = mobius(d)
    if m == 1:
      f *= g
    elif m == -1:
      f /= g
  return f
