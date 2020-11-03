from cryptofield.boolean import *
import unittest


class TestBoolean(unittest.TestCase):
  
  def testZhegalkin1(self):
    f = BooleanFunction("0011")
    ans = anf("0010")
    pol = f.anf()
    self.assertEqual(ans, pol)

  def testZhegalkin2(self):
    f = BooleanFunction("11010011")
    ans = anf("10111001")
    pol = f.anf()
    self.assertEqual(ans, pol)
    
  def testWalshSpec1(self):
    f = BooleanFunction("1110")
    self.assertEqual(f.walshSpectrum(), [-2, -2, -2, 2])
    
  def testNonlineartyBool1(self):
    f = BooleanFunction("0000010100110110")
    self.assertEqual(f.nonlinearty(), 6)
  
  def testIsLinearBoolFalse(self): 
    f = BooleanFunction("0000010100110110")
    self.assertEqual(f.isLinear(), False)
  
  def testIsLinearBoolTrue(self):
    f = BooleanFunction("01101001")
    self.assertEqual(f.isLinear(), True)
  
  def testDegBool1(self):  
    f = BooleanFunction("11010011")
    self.assertEqual(f.deg(), 3)
  
  def testDegBool2(self):  
    f = BooleanFunction("0000010100110110")
    self.assertEqual(f.deg(), 2)

  def testIsMonotoneTrue(self): 
    f = BooleanFunction("00010111")
    self.assertEqual(f.isMonotone(), True)

  def testIsMonotoneFalse(self):
    f = BooleanFunction("0110")
    self.assertEqual(f.isMonotone(), False)

  def testIsMonotoneFalse2(self):
    f = BooleanFunction("1011")
    self.assertEqual(f.isMonotone(), False)

if __name__ == '__main__':
    unittest.main(self)

