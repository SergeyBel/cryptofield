import math

def ValueToBinaryStr(value, length = False):
	s = bin(value)[2:]
	if length != False:
		s  = "0" * (length - len(s)) + s
	return s

def BinaryStrToValue(str):
	return int(str, 2)

def BooleanFuncToFieldFunc(equations):
	res = list()
	for i in range(0, len(equations[0])):
		s = ""
		for j in range(0, len(equations)):
			s = s + equations[j][i]
		res.append(BinaryStrToValue(s))
	return res
	
def SwapArr(a, i, j):
	c = a[i]
	a[i] = a[j]
	a[j] = c

def IsPowerTwo(n):
	return n > 0 and not ((n & (n - 1)))

def NumberDivisors(n):
	divisors = []
	for i in range(1, n + 1):
		if n % i == 0:
			divisors.append(i)
	return divisors

def IsPrime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
		if n % i == 0:
			return False
	return True

def Mobius(n):
	if n == 1:
		return 1
	k = 0
	for i in range(2, n + 1):
		if IsPrime(i):
			if n % i == 0:
				if n % (i*i) == 0:
					return 0
				else:
					k  = (k + 1) % 2
	if k % 2 == 0:
		return 1
	else:
		return -1

