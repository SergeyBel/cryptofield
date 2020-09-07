from symbol_monom import *

class SElement:
  def __init__(self, coeffs):
    if (isinstance(coeffs, set)):
      self.coeffs = coeffs
    else:
      if not (isinstance(coeffs, list)):
        coeffs = [coeffs]
      monoms = set()
      for c in coeffs:
        if isinstance(c, str):
          monoms.add(SMonom(c))
        else:
          monoms.add(c)
      self.coeffs = monoms
    self.normilize()

  def normilize(self):
    zero = SMonom('0')
    self.coeffs.discard(zero)

  def len(self):
    return len(self.coeffs)

  def __add__(self, other):
    coeffs = self.coeffs.symmetric_difference(other.coeffs)
    return SElement(coeffs)

  def toString(self):
    if len(self.coeffs) == 0:
      return '0'
    s = []
    for c in self.coeffs:
      s.append(c.toString())
    return ' + '.join(s)

  def __mul__(self, other):
    coeffs = {}
    for a in self.coeffs:
      for b in other.coeffs:
        c = a * b
        if coeffs.get(c) != None:
          coeffs[c] = not coeffs[c]
        else:
          coeffs[c] = True
        
    result = set()
    for k in coeffs.keys():
      if coeffs[k]:
        result.add(k)
    return SElement(result)

  def __pow__(self, n):
    return self

  def __str__(self):
   return self.toString()

  def __eq__(self, other):
    return self.coeffs == other.coeffs

  def evaluate(self, values):
    s = 0
    for c in self.coeffs:
      s ^= c.evaluate(values)
    return s


