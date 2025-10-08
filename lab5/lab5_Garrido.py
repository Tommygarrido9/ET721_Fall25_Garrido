"""
Tommy Garrido
Sep 15, 2025
Lab 5, functions
"""

"""
-  pre-defined function: Python library
- user-defined function: create by the programmer

what is a function?
- A block of code that begins with 'def' follows by the name of the function and parentheses ():
- The body of the function is indented after the colon :
- The body of the function only run when the function is called
"""
# Import python file
from lab5_Garrido_Function import *
import random
# call the function
print("\n------- Example 1: Intro Function -------")
n1 = 2
n2 = 5
p = product(n1, n2)
print(f"The product of {n1} and {n2} is {p}")
p = product()
print(f"The product is {p}")
p = product(5)
print(f"The product is {p}")

print("\n------- Example 2: Function to calculate the hypotenuse -------")
s1 = 5
s2 = 3
hyp = hypotenuse(s1, s2)
print(f"The hypotenuse is {hyp:0.2f}")

print("\n------- Example 3: Function to check if the number is positive, negative or zero -------")
c = check_number(-3)
print(f"The number is {c}")
c = check_number(5)
print(f"The number is {c}")
c = check_number(0)
print(f"The number is {c}")

print("\n------- Example 4: Function to calculate the average of a list of grades -------")
g = [50,60,85,93,72]
avg = check_grades(g)
print(f"Did I pass the class? {check_pass(avg)}")
g = [50,60,30,50]
print(f"Did I pass the class? {check_pass(check_grades(g))}")


print("\n------- LAB EXERCISE! -------")
GUESS_NUMBER = 5
min = 0
max = 0
g = 0
min, max, g = r(min, max, g)
print(f"The random number is between {min} and {max}")
print(f"The guess number is {g}")
print(guess(g, GUESS_NUMBER))