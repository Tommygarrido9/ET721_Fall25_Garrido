"""
Tommy Garrdo
Lab 8, unit test
Sep 29, 2025
October 6, 2025
"""

import unittest
import calculations
import bankaccount
from employee import Employee # import class "Employee" from employee.py

# Function to add and return the sum of two numbers
def addtwonumbers(a,b):
    return a+b
# create a code to test function addtwonumbers
print("\n ---- Example 1: test for equality ----")
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3),5)
    
print("\n ---- Example 2: unittest for calculations ----")
class TestCalculation(unittest.TestCase):
    def testmultiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5)
        self.assertEqual(calculations.multiplythreenumbers(2,3),6)
        self.assertEqual(calculations.multiplythreenumbers(2,3,4),24)
        self.assertEqual(calculations.multiplythreenumbers(0),0)

    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8,4),2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9,2),4.5)
        self.assertIsNone(calculations.dividetwonumbers(9,0))

    def test_addition(self):
        self.assertEqual(calculations.addthreenumbers(5,6,2),13)

print("\n ---- Example 3: unittest for Employee ----")
class TestEmployee(unittest.TestCase):
    # create a test template
    def setUp(self):
        self.emp1 = Employee('Peter', 'Pan', 50000)
    #create a test for employees email
    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, 'Peter.Pan@email.com')
    # create a test for employees full name
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Peter Pan')
        # update first name 
        self.emp1.first = "Will"
        #re-test full name
        self.assertEqual(self.emp1.fullname, 'Will Pan')

    #create a test for salary
    def test_salary(self):
        # first, raise the salary
        self.emp1.apply_raise()
        # second, test salary
        self.assertEqual(self.emp1.salary, 52500)

    
        

print("\n ---- EXERCISE! ----")
#unit test should include the following: 
#Use the setUp method from unittest.TestCase to create a default BankAccount instance before each test. 
#Test that the account is initialized with the correct balance. 
#Test that a deposit operation correctly adds the specified amount to the balance. 
#Test that a withdrawal operation correctly subtracts the specified amount from the balance. 
#Test that attempting to withdraw more than the available balance raises the appropriate exception.
#Test a sequence of deposits and withdrawals to ensure correct balance calculations. 
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = bankaccount.BankAccount("Tommy Garrido", 5000)
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 5000)
    def test_deposit(self):
        self.account.deposit(6000)
        self.assertEqual(self.account.balance, 11000)
    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 4500)
    def test_overdrawl(self):
        self.account.withdraw(6000)
    def test_sequence(self):
        self.account.deposit(3400)
        self.account.withdraw(2000)
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 6500)





if __name__ == "__main__":
    unittest.main()