from cryptofield.fieldpolynom import *

F = FField(4)
x = FPolynom(F, [1, 0, 5, 15])
print (x)
y = FPolynom(F, [0, 7, 8, 3])
print (y)
print ('Arithmetic:')
print (x + y)
print (x - y)
print (x * y)
print (x / y)
print (x % y)


z = x + y
print ()
print ('Polynom:', z)
print ('Deg:', z.deg())
print ('Rank:', z.rank())
print ('Derivative:', z.derivative())
print ('Values for all x:', z.values())
print ('Is linear:', z.isLinear())
print ('Is affine:', z.isAffine())
print ('Random polynom deg 10')
print (FPolynom.random(F, 10))
