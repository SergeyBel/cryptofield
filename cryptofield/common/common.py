import math
from cryptofield.ffield import *



def valueToBinaryStr(value, length = False):
  s = bin(value)[2:]
  if length != False:
    s  = "0" * (length - len(s)) + s
  return s

def binaryStrToValue(binaryInStr):
  return int(binaryInStr, 2)

def scalarBool(vec1, vec2):
  s = 0
  for i in range(0, len(vec1)):
    s = s + ( (int(vec1[i]) & int(vec2[i])))
  return s

def nextBoolVec(vec):
  t = list(vec)
  i = len(t) - 1
  while (t[i] == "1" and i >= 0):
    i = i - 1
  if i < 0:
    return False
  t[i] = "1"
  for j in range(i + 1, len(vec)):
    t[j] = "0"
  return "".join(t)  # convert list to to string

def swapArr(a, i, j):
  c = a[i]
  a[i] = a[j]
  a[j] = c

def isPowerTwo(n):
  return n > 0 and not (n & (n - 1))

def numberDivisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.append(i)
  return divisors

def isPrime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
    if n % i == 0:
      return False
  return True

def mobius(n):
  if n == 1:
    return 1
  k = 0
  for i in range(2, n + 1):
    if isPrime(i):
      if n % i == 0:
        if n % (i*i) == 0:
          return 0
        else:
          k  = (k + 1) % 2
  if k % 2 == 0:
    return 1
  else:
    return -1

def FPow(F, x, n):
  p = FElement(F, 1)
  while (n):
    if (n & 1):
      p *= x
      n -= 1
    else:
      x *= x
      n >>= 1
  return p
