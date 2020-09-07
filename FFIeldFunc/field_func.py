from common import *
from ffield import FElement
import ffield
from boolean import *

def FieldPow(F, x, n):
	p = FElement(F, 1)
	for i in range(n):
		p = p * x
	return p	
	

	
def FieldFuncToBooleanFunc(func, m):
	ans = [""] * m
	for i in range(len(func)):
		bin = ValueToBinaryStr(func[i], m)
		for j in range(m):
			ans[j] += str(bin[j])
	return ans
	
def FielFuncFourierSpectrum(F, func):
	eq = FieldFuncToBooleanFunc(func, F.n)
	fts = []
	spectrum = []
	u = "0"*F.n
	while u != "":
		sum = 0
		for j in range(1, F.n + 1):
			sum = sum + 2**(j - 1) * FourierCoeff(eq[F.n - j ], u, F.n)
		spectrum.append(sum)
		u = NextBoolVec(u)
	return spectrum
		

def FuncToFieldFunc(F, f):
	a = list()
	for i in range(len(f)):
		a.append(FElement(F, f[i]))
	return a
	
	
	