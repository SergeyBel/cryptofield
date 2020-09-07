import sys
sys.path.append("../Common")
import math
from random import randint
from common import *

def XOR(vec1, vec2):
	res = ""
	for i in range(0, len(vec1)):
		res = res + str(int(vec1[i]) ^ int(vec2[i]))
	return res
	
def ScalarBool(vec1, vec2):
	s = 0
	for i in range(0, len(vec1)):
		s = s + ( (int(vec1[i]) & int(vec2[i])))
	return s
	
def NextBoolVec(vec):
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
	
def WalshCoeff(f, u, n):
	#W_f(u) = Sum_(x in V_n)((-1) ^ (f(x) xor <x,u>)
	sum = 0
	x = 0
	while x < 2**n:
		p = int(f[x]) ^ ScalarBool(ValueToBinaryStr(x, n), u)
		if p % 2 ==  0:
			sum = sum + 1
		else:
			sum = sum - 1
		x = x + 1
	return sum
	
	
def WalshSpectrum(f, n):
	res = list()
	u = "0" * n
	while u != False:
		res.append(WalshCoeff(f, u, n))
		u = NextBoolVec(u)
	return res
	
def FourierCoeff(f, u, n):
	#F_f(u) = Sum_(x in V_n)(f(x)(-1) ^ (<x,u>))
	sum = 0
	x = 0
	while x < 2**n:
		p = ScalarBool(ValueToBinaryStr(x, n), u)
		#print ValueToBinaryStr(x, n), u, p, f[x]
		if p % 2 ==  0:
			sum = sum + int(f[x])
		else:
			sum = sum - int(f[x])
		x = x + 1
	return sum
	
	
def FourierSpectrum(f, n):
	res = list()
	u = "0" * n
	while u != False:
		res.append(FourierCoeff(f, u, n))
		u = NextBoolVec(u)
	return res
	
	
def NonlineartyBool(f):
	n = int(math.log(len(f), 2))
	u = "0" * n
	maxn = -(2**(n)) - 1
	while u != False:
		c = abs(WalshCoeff(f, u, n))
		if  c > maxn:
			maxn = c
		u = NextBoolVec(u)
			
	return 2**(n - 1) - maxn / 2
			
		
	
def IsLinear(boolVec, n):
	if (n == 0):
		return True
	N = 2**n
	if boolVec[0] == boolVec[N / 2]:
		c = 0
	else:
		c = 1
	for i in range(0, N / 2):
		if int(boolVec[i]) != int(boolVec[i + N / 2]) ^ c:
			return False
	return IsLinear(boolVec[:(N / 2)], n - 1)
	
	
def PrintEquations(equations):
	for i in range(0, len(equations[0])):
		for j in range(0, len(equations)):
			print equations[j][i],
		print
	
def FuncShiftBool(f):
	count = 0
	for i in range(0, len(f)):
		count = count + int(f[i])
	return 2 * count - len(f)
	
	
def RandBoolVec(length):
	vec = ""
	for i in range(0, length):
		vec += str(randint(0, 1))
	return vec
	
#https://habrahabr.ru/post/275527/
def ZhegalkinPolynom(func):
	res = func[0:1]
	func = list(func)
	while len(func) != 1:
		coefs = ""
		for i in range(0, len(func) - 1):
			coefs  = coefs + str((int(func[i]) ^ int(func[i + 1])))
		res = res + coefs[0:1]
		func = coefs
	return res
	
def StrZhegalkinPolynom(coeffs):
	variablesNum = int(math.log(len(coeffs), 2))
	coeffs = list(coeffs)
	s = ""
	for i in range(len(coeffs)):
		if coeffs[i] == "1":
			decomp = list(ValueToBinaryStr(i, variablesNum))
			monom = ""
			for j in range(variablesNum):
				if decomp[j] == "1":
					monom = monom + "x" + str(j + 1)
			if monom == "":
				monom = "1"
			#print i, ValueToBinaryStr(i, variablesNum), monom
			s = s + monom + "+"
	s = s[:-1]  # delete last +
	if s == "":
		s = "0"
	return s
	
	
def Deg(func):
	max = 0
	pol = list(ZhegalkinPolynom(func))
	for i in range(len(pol)):
		if pol[i] == "1":
			k = (bin(i)[2:]).count("1")
			#print i, bin(i)[2:], k
			if k > max:
				max = k;
	return max
			
def BooleanToList(f):
	c = []
	for i in range(len(f)):
		c.append(int(f[i]))
	return c

def IsMonotone(f):
	length = len(f)
	if length == 1:
		return True
	leftPart = f[:length / 2]
	rightPart = f[length / 2:]
	for i in range(len(leftPart)):
		if int(leftPart[i]) > int(rightPart[i]):
			return False
	return IsMonotone(leftPart) and IsMonotone(rightPart)

	
	
