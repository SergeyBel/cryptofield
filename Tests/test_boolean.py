import sys
sys.path.append("../Boolean")
from boolean import *
import unittest


class TestBoolean(unittest.TestCase):
  
  def testZhegalkin1(self):
    f = "0011"
    ans = "0010"
    pol = ZhegalkinPolynom(f)
    self.assertEquals(ans, pol)

  def TestZhegalkin2(self):
    f = "11010011"
    ans = "10111001"
    pol = ZhegalkinPolynom(f)
    self.assertEquals(ans, pol)
    
  def testWalshSpec1(self):
    f = "1110"
    self.assertEquals(WalshSpectrum(f, 2), [-2, -2, -2, 2])
    
  def testNonlineartyBool1(self):
    f = "0000010100110110"
    self.assertEquals(NonlineartyBool(f), 6)
  
  def testIsLinearBoolFalse(self): 
    f = "0000010100110110"
    self.assertEqual(IsLinear(f, 4), False)
  
  def testIsLinearBoolTrue(self):
    f = "01101001"
    self.assertEqual(IsLinear(f, 3), True)
  
  def testDegBool1(self):  
    f = "11010011"
    self.assertEqual(Deg(f), 3)
  
  def testDegBool2(self):  
    f = "0000010100110110"
    self.assertEqual(Deg(f), 2)

  def testIsMonotoneTrue(self): 
    f = "00010111"
    self.assertEqual(IsMonotone(f), True)

  def testIsMonotoneFalse(self):
    f = "0110"
    self.assertEqual(IsMonotone(f), False)

  def testIsMonotoneFalse2(self):
    f = "1011"
    self.assertEqual(IsMonotone(f), False)

if __name__ == '__main__':
    unittest.main(self)

