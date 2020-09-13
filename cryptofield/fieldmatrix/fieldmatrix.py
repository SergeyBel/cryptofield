from cryptofield.ffield import *

	
class FMatrix:
	def __init__(self, F, n, m):
		self.nullElement = FElement(F, 0)
		self.oneElement = FElement(F, 1)
		self.matrix =  self.__newMatrix(F, n, m)
		self.field = F
		self.n = n
		self.m = m
		
	def loadRows(self, rows):
		self.n = len(rows)
		self.m = len(rows[0])
		self.field = rows[0][0].f
		self.matrix = self.__newMatrix(self.field, self.n, self.m)
		for i in range(self.n):
			self.matrix.SetRow(i, rows[i])
	
	@staticmethod
	def __newMatrix(F, n, m):
		 return GenericMatrix((n, m), FElement(F, 0), FElement(F, 1), 
					   AddAbstract, SubAbstract, MulAbstract, DivAbstract, EqAbstract)
		
	def ident(self):
		self.matrix = self.__newMatrix(self.field, self.n, self.m)
		
		for i in range(self.n):
			r = [self.nullElement] * self.m
			r[i] = self.oneElement
			self.matrix.SetRow(i, r)
			
	def setRow(self, index, row):
		self.matrix.SetRow(index, row)
	
	def getRow(self, index):
		return self.matrix.GetRow(index)
		
	def size(self):
		return self.matrix.Size()
		
	def getColumn(self,c):
		return self.matrix.GetColumn(c)

	def transpose(self):
		m = self.copy()
		m.matrix.Transpose()
		return m


	def copy(self):
		m = FMatrix(self.field, self.n, self.m)
		m.matrix = self.matrix
		return m
		
	def swapRows(self, i, j):
		self.matrix.SwapRows(i, j)
		
	def kerBasis(self):
		basis = list()
		C = self.matrix.LowerGaussianElim() # C - is a result of the same LowerGaussianElim to identity matrix
		for i in range(self.n):
			r = self.getRow(i)
			if self.isNullRow(i):
				basis.append(C.GetRow(i))
		return basis

	# Test row consists of all nulls
	def isNullRow(self, index):
		r = self.getRow(index)
		for j in range(len(r)):
			if not (r[j] == self.nullElement):
				return False
		return True;

	def inverse(self):
		m = self.copy()
		m.matrix = self.matrix.Inverse()
		return m


	def solve(self, b):
		x = self.matrix.Solve(b)
		return x
		
	def __mul__(self, other):
		m = self.copy()
		m.matrix = self.matrix * other.matrix
		return m
		
	def __add__(self, other):
		m = self.copy()
		m.matrix = self.matrix + other.matrix
		return m
	
	def __sub__(self, other):
		m = self.copy()
		m.matrix = self.matrix - other.matrix
		return m

	def __eq__(self, other):
		if (self.n != other.n or self.m != other.m):
			return False
		for i in range(self.n):
			if self.getRow(i) != other.getRow(i):
				return False
		return True
		
	def __setitem__ (self, coordinates, data):
		(x,y) = coordinates
		self.matrix[x, y] = data

	def __getitem__ (self, coordinates):
		(x,y) = coordinates
		return self.matrix[x, y]
		
	def __str__(self):
		return str(self.matrix)


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