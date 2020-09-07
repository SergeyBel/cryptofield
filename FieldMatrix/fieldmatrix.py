import sys
sys.path.append("../FField")
from ffield import *
from genericmatrix import *



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
	
def NewMatrix(F, n, m):
	return GenericMatrix((n, m), FElement(F, 0), FElement(F, 1), 
					   AddAbstract, SubAbstract, MulAbstract, DivAbstract, EqAbstract)
					   
# Test row consists of all nulls
def IsNullRow(F, r):
	for j in range(len(r)):
		if not (r[j] == FElement(F, 0)):
			return False
	return True;

	
class FMatrix:
	def __init__(self, F, n, m):
		self.matrix = NewMatrix(F, n, m)
		self.field = F
		self.n = n
		self.m = m
		
		
	def FromRows(self, rows):
		self.n = len(rows)
		self.m = len(rows[0])
		self.field = rows[0][0].f
		self.matrix = NewMatrix(self.field, self.n, self.m)
		for i in range(self.n):
			self.matrix.SetRow(i, rows[i])
			
		
	def Ident(self):
		self.matrix = NewMatrix(self.field, self.n, self.m)
		
		for i in range(self.n):
			r = [FElement(self.field, 0)] * self.m
			r[i] = FElement(self.field, 1)
			self.matrix.SetRow(i, r)
			
	def SetRow(self, index, row):
		self.matrix.SetRow(index, row)
	
	def GetRow(self, index):
		return self.matrix.GetRow(index)
		
	def Size (self):
		return self.matrix.Size()
		
	def GetColumn(self,c):
		return self.matrix.GetColumn(c)

	def Transpose(self):
		self.matrix.Transpose()

	def Copy(self):
		m = FMatrix(self.field, self.n, self.m)
		m.matrix = self.matrix
		return m
		
	def SwapRows(self,i,j):
		self.matrix.SwapRows(i, j)
		
	def KerBasis(self):
		basis = list()
		C = self.matrix.LowerGaussianElim() # C - is a result of the same LowerGaussianElim to identity matrix
		for i in range(self.n):
			r = self.GetRow(i)
			if IsNullRow(self.field, r):
				basis.append(C.GetRow(i))
		return basis

	def Inverse(self):
		m = self.Copy()
		m.matrix = self.matrix.Inverse()
		return m


	def Solve(self, b):
		x = self.matrix.Solve(b)
		return x
		
	def __mul__(self, other):
		m = self.Copy()
		m.matrix = self.matrix * other.matrix
		return m
		
	def __add__(self, other):
		m = self.Copy()
		m.matrix = self.matrix + other.matrix
		return m
	
	def __sub__(self, other):
		m = self.Copy()
		m.matrix = self.matrix - other.matrix
		return m

	def __eq__(self, other):
		if (self.n != other.n or self.m != other.m):
			return False
		for i in range(self.n):
			if self.GetRow(i) != other.GetRow(i):
				return False
		return True
		
	def __setitem__ (self, (x,y), data):
		self.matrix[x, y] = data

	def __getitem__ (self, (x,y)):
		return self.matrix[x, y]
		
	def __str__(self):
		return str(self.matrix)

"""
F = FField(4)				
m = FMatrix(F, 4, 4)
a = FElement(F, 0)
b = FElement(F, 1)

m.SetRow(0, [a, a, a, a])
m.SetRow(1, [a, b, b, a])
m.SetRow(2, [a, b, b, b])
m.SetRow(3, [a, b, b, b])


print m
basis = m.KerBasis()
print m
"""

		
	
					   
					