"""
Tommy Garrido
Sep 17, 2025
Lab 6: Objects and classes
"""

print("\n--------- Example 1: create a class ---------")
class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # method
    def add_radius(self, r):
        self.radius += r
        return self.radius



class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    # method to calculate the area
    def area(self):
        return self.width * self.height
    
    # method to calculate the perimeter
    def perimeter(self):
        return 2*self.width+2*self.height


# Creating an instance of a class, which is an object
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(2,5,"magenta")
rectangle2 = Rectangle(7,3,"blue")

#accessing information in an object
print(f"The color of circle2 = {circle2.color}")
print(f"The width of rectangle1 = {rectangle1.width}")

# updating data in an object
# change circle 1 color from "red" to "yellow"
print(f"The color of circle1 before the update = {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle1 after the update = {circle1.color}")

# accessing method
print(f"Radius of circle2 = {circle2.radius}")
circle2.add_radius(5)
print(f"Radius of circle2 after method add_radius = {circle2.radius}")

# accessing methods in Rectangle
print(f"The area of the rectangle1 with width {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}")
print(f"The perimeter of rectangle2 = {rectangle2.perimeter()}")


print("\n--------- EXERCISE! ---------")

class BankAccount(object):
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # method to add the deposited amount of money into the account
    def deposit(self, amount):
        self.balance += amount
        if(amount < 0):
            return "ERROR! You cannot deposit negative dollars!"
        return self.balance
    # method to subtract the withdrawn amount of money from the account 
    def withdraw(self, amount):
        self.balance -= amount
        if(amount > self.balance):
            return "ERROR! You are overdrawing!"
        elif(amount < 0):
            return "ERROR! You cannot withdraw negative dollars!"
        return self.balance


# Crearting an instance of class BankAccount
useraccount = BankAccount("254468853", "Tommy Garrido", 6000)
# Demonstrating withdrawls and deposits
useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)

print(f"Final balance: {useraccount.balance}")
