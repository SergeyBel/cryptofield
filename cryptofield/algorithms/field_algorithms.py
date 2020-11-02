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
