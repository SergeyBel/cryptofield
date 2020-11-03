# Cryptofield

Cryptofield is a library to work with discrete algebraic objects. Useful for research in discrete mathematics and cryptography


## Boolean functions
The most important characteristics of boolean functions can be calculated: ANF, algebraic degree, nonlinearity, walsh coefficients 
```python
vec = "1110"
f = BooleanFunction(vec)
print ('ANF:')
print (f.anf())
print (f.deg())
print (f.isLinear())
print (f.isMonotone())
```

## Finite fields polynomials
Finite fields polynomials can be created and algebraic functions supported. Euclidean  and Berlekamp's algorithms for polynomials are supported 
```python
F = FField(4)
x = FPolynom(F, [1, 0, 5, 15]) # 15X^3 + 5X^2 + 1
print (x)
y = FPolynom(F, [0, 7, 8, 3]) # 3X^3 + 8X^2 + 7X
print (y)
print (x + y)
print (x - y)
print (x * y)
print (x / y)
print (x % y)
```
## Finite fields matrix
Matrix with elements from finite fields can be used for calculations. All necessary functions like transposition, inverse, equations solving are available

```python
F = FField(2)
m = FMatrix(F, 4, 4)
m.setRow(0, [FElement(F, 0), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
m.setRow(1, [FElement(F, 0), FElement(F, 0), FElement(F, 1), FElement(F, 0)])
m.setRow(2, [FElement(F, 1), FElement(F, 1), FElement(F, 0), FElement(F, 0)])
m.setRow(3, [FElement(F, 1), FElement(F, 0), FElement(F, 1), FElement(F, 1)])

print(m.transpose())
print (m.inverse())
print (m.solve([FElement(F, 1), FElement(F, 0), FElement(F, 1), FElement(F, 1)]))

```
## Examples
See examples directory for more information

## Acknowledgments
Based on Emin Martinian FField library



