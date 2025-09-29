"""
Tommy Garrdo
Lab 8, unit test
Sep 29, 2025
"""

import unittest
import calculations
# Function to add and return the sum of two numbers
def addtwonumbers(a,b):
    return a+b
# create a code to test function addtwonumbers
print("\n ---- Example 1: test for equality ----")
class TestAddFunction(unittest.Testcase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3),5)
    
print("\n ---- Example 2: unittest for calculations ----")
class TestCalculation(unittest.Testcase):
    def testmultiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5)
        self.assertEqual(calculations.multiplythreenumbers(2,3),6)
        self.assertEqual(calculations.multiplythreenumbers(2,3,4),24)
        self.assertEqual(calculations.multiplythreenumbers(0),0)

    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8,4),2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9,2),4.5)
        self.assertIsNone(calculations.dividetwonumbers(9,0))

if __name__ == "__main__":
    unittest.main()