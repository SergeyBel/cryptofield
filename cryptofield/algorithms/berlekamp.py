from cryptofield.fieldpolynom import *
from cryptofield.algorithms.field_algorithms import *


def Berlekamp(F, polynom):
  f = polynom.copy()
  factors = list()
  if f.deg() <= 1:
    factors.append(f)
    return factors

  if not f.c[-1] == FElement(F, 1):
    factors.append(FPolynom(F, [f.c[-1]], True))
    f.normalize()
  d = f.derivative()
  gcd = PolynomEquilid(F, f, d)
  if gcd == FPolynom(F, [1]):
    decomp = Berl(F, f)
    factors = factors + list(decomp)
  elif gcd == f:
    # f = g(x)^p
    # it mean it nedd to find h(x) such f(x) = h(x)^(p^s)
    # then apply to h(x)
    k = 1
    while gcd == f:
      f = PolynomPRoot(F, f)
      k = k * 2
      d = f.derivative()
      gcd = PolynomEquilid(F, f, d)
    decomp = Berl(F, f)
    factors = factors + list(decomp) * k
  else:
    r = f / gcd
    factors1 = Berlekamp(F, gcd)
    factors2 = list(Berl(F, r))
    factors = factors + factors1 + factors2
          
  return factors
    
  
def Berl(F, f):
  n = f.deg()
  q = 2**F.n
  I = FMatrix(F, n, n)
  I.ident()
  x = FPolynom(F, [0, 1])
  
  B = FMatrix(F, n, n)
  for i in range(0, n):
    y = x ** (i * q) #bi = x^(iq) in GF(q)
    y = y % f
    B.setRow(i, ExpendRow(F, y.c, n))
  B = B - I
  basis = B.kerBasis()
  k = len(basis)
  decomp = set()
  decomp.add(f)
  i = 0
  while len(decomp) < k:
    tempDecomp = set()
    h = FPolynom(F, basis[i], True)
    if h == FPolynom(F, [1]):
      i = i + 1
      continue
    
    for d in decomp:
      g =  GCDSet(F, d, h)
      tempDecomp = tempDecomp.union(g)
    i = i + 1
    decomp = tempDecomp
  return decomp


# Expend row 0's for length n 
def ExpendRow(F, row, n):
  m = n - len(row)
  for i in range(m):
    row.append(FElement(F, 0))
  return row
    
  
# Get set of GCD(f, h-c) where c in Field   
def GCDSet(F, f, h):
  gcds = list()
  N = 2**F.n
  for i in range(N):
    c = FPolynom(F, [i])
    g = PolynomEquilid(F, f, h - c)
    if g.deg() > 0:
      gcds.append(g)
  return gcds

  
def Root(F, a):
  #2-root of a, x^2=a => x = a^(N/2)
  N = 2**F.n
  return FPow(F, a, int(N / 2))
  

def PolynomPRoot(F, f):
  for i in range(len(f.c)):
    if not f.c[i] == FElement(F, 0):
      t = Root(F, f.c[i])
      f.c[i] = FElement(F, 0)
      f.c[int (i / 2)] = t
  f.correct()
  return f
