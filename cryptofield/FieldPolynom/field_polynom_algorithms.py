import sys
sys.path.append("../FieldMatrix")
sys.path.append("../Boolean")
from field_polynom import *
from fieldmatrix import *
from boolean import *

def PolynomEquilid(F, x, y):
	if (x.Deg() < y.Deg()):
		f = y.Copy()
		g = x.Copy()
	else:
		f = x.Copy()
		g = y.Copy()
		
	polNull = FPolynom(F, [0])
	
	if g == polNull:
		return f
		
	while True:
		r = f % g
		if r == polNull:
			break
		f = g
		g = r
	g.Normalize()
	return g
	
def PolynomPow(F, x, n):
	p = FPolynom(F, [1])
	while (n):
		if (n & 1):
			p *= x;
			n -= 1
		else:
			x *= x;
			n >>= 1;
	return p
	
def RandomFPolynom(F, n):
	N = 2**F.n
	coeffs = list()
	for i in range(n):
		coeffs.append(randint(0, N - 1))
	coeffs.append(randint(1, N - 1))
	return FPolynom(F, coeffs)
	
def NextCoeffs(F, c):
	N = FElement(F, 2**F.n - 1)
	i = 0
	n = len(c)
	while (i < n) and (c[i] == N):
		i = i + 1
	if i == n:
		return False
	c[i] = FElement(F, c[i].f + 1)
	for j in range(0, i):
		c[j] = FElement(F, 0)
	return c
	
def NextLinearPolynom(F, f):
	coeffs = [FElement(F,0)] * F.n
	for i in range(F.n):
		if (2**i < len(f.c)):
			coeffs[i] = f.c[2**i]
	nextCoeffs = NextCoeffs(F, coeffs)
	if nextCoeffs == False:
		return False
	twoPower = 0
	
	coeffs = [FElement(F,0)] * 2**F.n
	for i in range(2**F.n):
		if (i == 2**twoPower):
			coeffs[i] = nextCoeffs[twoPower]
			twoPower += 1
	g = FPolynom(F, coeffs, True)
	return g
	
def NextAffinePolynom(F, f):
	N = 2**F.n - 1
	g = f.Copy()
	c = g.c[0]
	if c == FElement(F, N):
		g.c[0] = FElement(F, 0)
		g = NextLinearPolynom(F, g)
	else:
		g.c[0] = FElement(F, g.c[0].f + 1)
	return g

#return FPolynom Tr(b*x)
def CreateTr(F, betta):
	n = F.n
	coeffs = [FElement(F, 0)] * 2**n
	for i in range(n):
		j = 2**i
		c = FPow(F, betta, 2**i)
		coeffs[j] = c
	return FPolynom(F, coeffs, True)
	
def DualBasis(F):
	n = F.n
	alpha = FElement(F, 2)
	basis = list()
	dualBasis = list()
	tr = CreateTr(F, FElement(F, 1))

	a = FMatrix(F, n, n)
	for i in range(n):
		for j in range(i + 1):
			a[j, i] = a[i, j] = tr.Value(FPow(F, alpha, i + j))
	b = a.Inverse()
	for i in range(n):
		num = "";
		t = b.GetRow(i)
		for j in range(len(t)):
			num += str(t[j].f)
		dualBasis.append(FElement(F, BinaryStrToValue(num[::-1])))
	return dualBasis

def FromZhekalkinPolynom(F, coeffs):
	n = F.n
	coords = []
	dualBasis = DualBasis(F)
	dualBasis = dualBasis[::-1]
	f = FPolynom(F, [])
	for i in range(n):
		coords.append(CreateTr(F, dualBasis[i]))
	for i in range(len(coeffs)):
		if (coeffs[i] == "1"):
			monom = FPolynom(F, [1])
			decomp = list(ValueToBinaryStr(i, n))
			for j in range(n):
				if decomp[j] == "1":
					monom *= coords[j];
			f += monom
	f.Reduce()
	return f

def FromInt (F, a):
  g = ValueToBinaryStr(a)[::-1]
  c = []
  for j in range(len(g)):
    c.append(int(g[j]))
  return FPolynom(F, c)



def IrreducibleProduct(F, n):
	divisors = NumberDivisors(n)
	f = FPolynom(F, [1])
	for d in divisors:
		c = [0] * (2**(n / d) + 1)
		c[1] = 1
		c[2**(n / d)] = 1
		g = FPolynom(F, c)
		m = Mobius(d)
		if m == 1:
			f *= g
		elif m == -1:
			f /= g
	return f