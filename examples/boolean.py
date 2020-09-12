from cryptofield.boolean import *

vec = "1110"
f = BooleanFunction(vec)
print ('zhegalkin polynom:')
print (f.zhegalkinPolynom())
print ('zhegalkin deg:', f.deg())
print ('is linear:', f.isLinear())
print ('is monotone:', f.isMonotone())
print ('walsh spetrum:')
print (f.walshSpectrum())
print ('fourier spetrum:')
print (f.fourierSpectrum())
print ('nonlinearty:', f.nonlinearty())
print ('next boolean functon:')
print (f.nextBoolFunction())
print ('random boolean functon:')
print (f.randomBooleanfunction(16))
