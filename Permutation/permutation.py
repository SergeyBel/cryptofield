import sys
sys.path.append("../Common")
from random import randint
from common import *


def InvPermutation(f):
	inv = [f.index(i) for i in range(len(f))]
	return inv
	
	
def IsPermutation(func):
	f = sorted(func)
	for i in range(len(f) - 1):
		if f[i] == f[i + 1]:
			return False
	return True
	
	

def GetCycles(perm):
	#all cycles store in list cycles cycles[length] = list of cycles with this length
	cycles = list()
	for i in range(len(perm) + 1):
		cycles.append(list())
	flags = [0] * len(perm)
	for i in range(len(perm)):
		if flags[i] == 0:
			j = perm[i]
			cycle = []
			cycleLen = 0
			while flags[j] != 1:
				cycle.append(j)
				cycleLen += 1
				flags[j] = 1
				j = perm[j]
			cycles[cycleLen].append(cycle)
	return cycles
			


			
def StrCycles(cycles):
	s = ""
	for i in range(len(cycles)):
		cs = cycles[i]  #all cyles with length i
		if cs:
			for cycle in cs:
				s += CycleToStr(cycle)
	return s
	
def CycleToStr(cycle):
	s = "("
	for i in range(len(cycle)):
		s = s + str(cycle[i])
		if i != len(cycle) - 1:
			s = s + ","
	s = s + ")"
	return s
				

def CycleStruct(cycle):
	struct = [0] * (len(cycle) - 1)
	for i in range(1, len(cycle)):
		struct[i - 1] = len(cycle[i])
	return struct
			
	

	
def RandomPermutation(max):
	nums = list(i for i in range(max))
	perm = list()
	for i in range(max):
		j = randint(0, len(nums) - 1)
		perm.append(nums[j])
		del nums[j]
		
	return perm
	

def NextPermutation(perm):
	n = len(perm)
	j = n - 2
	while j >= 0 and perm[j] > perm[j + 1]:
		j-=1
	if j == -1:
		return False
	k = n - 1
	while perm[k] < perm[j]:
		k-=1

	SwapArr(perm, k, j)
	
	left = j + 1
	right = n - 1
	while left < right:
		SwapArr(perm, left, right)
		left += 1
		right -= 1
	
	return perm
	
def PermCompose(f, g):
	h = []
	for i in range(len(f)):
		h.append(f[g[i]])
	return h
		