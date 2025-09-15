"""
Tommy Garrido
Function file
Sep 15, 2025
Lab 5, functions
"""
import random

# example 1: Define a function that passes two numbers and returns the product of it 
# call the function
def product(a=0, b=0):
    c = a * b
    return c


# Example 2: Function to calculate the hypotenuse 
def hypotenuse(side1, side2):
    return (side1**2 +side2**2)**0.5


# Example 3: Functin to check if the number is positive, negative or zero. 
# The function returns a string
def check_number(num):
    if(num>0):
        return "POSITIVE"
    elif(num<0):
        return "NEGATIVE"
    else:
        return "ZERO"
    
# Example 4: Function to calculate the average of a list of grades, and return 'true' if the average is greater than 60, otherwise, it return 'false'
def check_grades(grades):
    # Initialize the average grade value
    avg = 0 
    # Sum the individual 'g' from list 'grades' into 'avg'
    for grade in grades:
        avg += grade
    # find the average grade
    avg /= len(grades)
    return avg
    # check if the average is greater than 60
    
def check_pass(avg_grade):
    if(avg_grade >= 60):
        return True
    else:
        return False
    

# LAB EXERCISE 
def r(min, max, guess):
    min = random.randint(1,4)
    max = random.randint(5,10)
    guess = random.randint(min, max)
    return min, max, guess

    

def guess(g, GUESS_NUMBER):
    if(GUESS_NUMBER==g):
        return "You got it!"
    elif(g<GUESS_NUMBER):
        return "The number is smaller than the guess number"
    elif(g>GUESS_NUMBER):
        return "The number is bigger than the guess number"
    
