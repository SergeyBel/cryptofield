import math
from cryptofield.common import *

class ZhegalkinPolynom:
  def __init__(self, coeffs):
    self.coeffs = list(coeffs)
    self.n = len(coeffs)

  def deg(self):
    maximum = 0
    for i in range(self.n):
      if self.coeffs[i] == "1":
        k = (bin(i)[2:]).count("1")
        if k > maximum:
          maximum = k
    return maximum

  def __str__(self):
    variablesNum = int(math.log(self.n, 2))
    s = ""
    for i in range(self.n):
      if self.coeffs[i] == "1":
        decomp = list(valueToBinaryStr(i, variablesNum))
        monom = ""
        for j in range(variablesNum):
          if decomp[j] == "1":
            monom = monom + "x" + str(j + 1)
        if monom == "":
          monom = "1"
        s = s + monom + "+"
    s = s[:-1]  # delete last +
    if s == "":
      s = "0"
    return s

  def __eq__(self, other):
    return self.coeffs == other.coeffs
    