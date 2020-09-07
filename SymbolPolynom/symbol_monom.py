
class SMonom:
  def __init__(self, coeff):
    if isinstance(coeff, str):
      coeff = [coeff]
    self.coeffs = set(coeff)
    self.hash = hash(self.toString())

  def toString(self):
    return ''.join(self.coeffs)

  def __mul__(self, other):
    zero = SMonom('0')
    if (self == zero or other == zero):
      return zero
    one = SMonom('1')
    if (self == one):
      return other
    elif (other == one):
      return self
    else:
      coeffs = self.coeffs.union(other.coeffs)
      return SMonom(coeffs)

  def __pow__(self, n):
    return self

  def __str__(self):
    return self.strRepresentation

  def __eq__(self, other):
    return self.coeffs == other.coeffs

  def __hash__(self):
    return self.hash

  def __cmp__(self, other):
    return self.coeffs < other.coeffs;

  def evaluate(self, values):
    s = 1
    for c in self.coeffs:
      s *= values[c]
    return s

