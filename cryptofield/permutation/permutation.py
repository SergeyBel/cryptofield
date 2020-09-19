from random import randint
from cryptofield.common import *
from cryptofield.permutation.cycles import *


class Permutation:
  def __init__(self, func):
    self.func = func
    self.length = len(func)

  def isPermutation(self):
    f = sorted(self.func)
    for i in range(len(f) - 1):
      if f[i] == f[i + 1]:
        return False
    return True

  def inversePermutation(self):
    inv = Permutation([self.func.index(i) for i in range(self.length)])
    return inv
  
  def getCycles(self):
    cycles = [0] * (self.length + 1)
    flags = [False] * self.length
    
    for i in range(self.length):
      if flags[i] == False:
        cycleLen = 1
        flags[i] = True
        j = self.func[i]
        while flags[j] != True:
          cycleLen += 1
          flags[j] = True
          j = self.func[j]
        cycles[cycleLen] += 1
    cycles.pop(0)  # delete 0-length cycle
    return PermutationCycles(cycles)

  def nextPermutation(self):
    n = self.length
    perm = self.func
    j = n - 2
    while j >= 0 and perm[j] > perm[j + 1]:
      j-=1
    if j == -1:
      return False
    k = n - 1
    while perm[k] < perm[j]:
      k -= 1

    swapArr(perm, k, j)
  
    left = j + 1
    right = n - 1
    while left < right:
      swapArr(perm, left, right)
      left += 1
      right -= 1
  
    return Permutation(perm)  

  def __str__(self):
    return str(self.func)

  def __eq__(self, other):
    return self.func == other.func
  
  @staticmethod
  def randomPermutation(max):
    nums = list(i for i in range(max))
    perm = list()
    for i in range(max):
      j = randint(0, len(nums) - 1)
      perm.append(nums[j])
      del nums[j]
    
    return Permutation(perm)
  




def PermCompose(f, g):
  h = []
  for i in range(len(f.func)):
    h.append(f.func[g.func[i]])
  return Permutation(h)
    