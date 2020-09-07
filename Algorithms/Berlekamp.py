import sys
sys.path.append("../Boolean")
sys.path.append("../FField")
sys.path.append("../FFIeldFunc")
sys.path.append("../Cryptonalysis")
sys.path.append("../FieldPolynom")
sys.path.append("../FieldMatrix")
from ffield import *
from field_polynom import *
from field_polynom_algorithms import *
from fieldmatrix import *


# functions for compatibility with GenericMatrix constructor
def AddAbstract(x, y):
	return x + y
	
def SubAbstract(x, y):
	return x - y
	
def MulAbstract(x, y):
	return x * y
	
def DivAbstract(x, y):
	return x / y

def EqAbstract(x, y):
	return x == y	
	

	
def RandomTest():
	F = FField(4)
	n = 1000
	deg = 4
	for i in range(n):
		print "i = ", i
		f = RandomFPolynom(F, deg)
		ft = f.Copy()
		print "f = ", f
		k = Berlekamp(F, f)
		y = FPolynom(F, [1])
		for t in k:
			y = y * t
		if not y == ft:
			print "Error"
			print "Factors"
			for m in k:
				print m
			print "Y = ", y, y.c
			return
		else:
			print len(k)
			
	

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
		if g.Deg() > 0:
			gcds.append(g)
	return gcds

	
def Root(F, a):
	#2-root of a, x^2=a => x = a^(N/2)
	N = 2**F.n
	return FPow(F, a, N / 2)
	

def PolynomPRoot(F, f):
	for i in range(len(f.c)):
		if not f.c[i] == FElement(F, 0):
			t = Root(F, f.c[i])
			f.c[i] = FElement(F, 0)
			f.c[i / 2] = t
	f.Correct()
	return f
	
	
	
def Berlekamp(F, polynom):
	f = polynom.Copy()
	factors = list()
	if f.Deg() <= 1:
		factors.append(f)
		return factors

	if not f.c[-1] == FElement(F, 1):
		factors.append(FPolynom(F, [f.c[-1]], True))
		f.Normalize()
	d = f.Derivative()
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
			d = f.Derivative()
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
	n = f.Deg()
	q = 2**F.n
	I = FMatrix(F, n, n)
	I.Ident()
	x = FPolynom(F, [0, 1])
	
	B = FMatrix(F, n, n)
	for i in range(0, n):
		y = PolynomPow(F, x, i * q) #bi = x^(iq) in GF(q)
		y = y % f
		B.SetRow(i, ExpendRow(F, y.c, n))
	B = B - I
	basis = B.KerBasis()
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

"""
G = FField(4)

f = FPolynom(G, [11, 0, 1])
x = Berlekamp(G, f)

for t in x:
	print t
"""

#RandomTest()





