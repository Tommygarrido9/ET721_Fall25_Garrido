"""
Tommy Garrido
Lab 3, Python conditional statement and loops
September 8, 2025
"""

# conditional statement
print("\n ----------- Example 1: if, else, elif, .... (EXERCISE) -------------")
"""
Modify example 1:
- use while loop to validate if the user_number is between 1 and 9 
- user can only guess 3 times. This can be done using a for loop or a while loop
"""

# guess a number between 1 and 9 
GUESS_NUM = 8
ATTEMPTS = 2
# collect the number
user_num = int(input("Guess a number: "))
while user_num<1 or user_num>9:
    user_num = int(input("Invalid Input! Guess another number: "))

while ATTEMPTS>=1:
    if (user_num == GUESS_NUM):
        print(f"Great Job! {user_num} is the guess number!")
        break
    elif (user_num>GUESS_NUM):
        print(f"{user_num} should be lower!")
        user_num = int(input("Guess a number: "))
        while user_num<1 or user_num>9:
            user_num = int(input("Invalid Input! Guess another number: "))
        ATTEMPTS -= 1
    elif (user_num<GUESS_NUM):
        print(f"{user_num} should be higher!")
        user_num = int(input("Guess a number: "))
        while user_num<1 or user_num>9:
            user_num = int(input("Invalid Input! Guess another number: "))
        ATTEMPTS -= 1
    else:
        print("ERROR!")

if (ATTEMPTS==0):
    print("You have used all of your attempts!")



print("End of Guessing!")


print("\n ----------- Example 2: Control flow with logical operators -------------")

# 'and, 'or, 'not' operators.
# 'and' operator returns TRUE ONLY if all statements are TRUE
# 'or' operator returns TRUE if at least one statement is TRUE

"""
Example 2:
- children under the age of 9 are only given milk for breakfast
- children from 10 to 14 are given a sandwich
- children from 15 to 17 are given a burger
"""
age_student = int(input("Enter an age: "))
lunch = "None"
if age_student < 9:
    lunch = "milk"
elif age_student >= 10 and age_student <= 14:
    lunch = "sandwich"
elif age_student >= 15 and age_student <= 17:
    lunch = "burger"    
else:
    lunch = "None"

print(f"At age {age_student} the food is {lunch}")

print("\n ----------- Example 3: for loop -------------")
# 'for' loop enables the program to execut a code block multiple times
for n in range (2,10):
    print(n)

print("\n ----------- Example 4: for loop in a list-------------")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")

print("\n ----------- Example 5: while loop as a counter-------------")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\n ----------- Example 6: while loop to validate a number-------------")
# valdate if a number is between -5 and 5 (inclusive)
num = int(input("Enter a number between -5 and 5: "))
# use a while to recollect if the num is not between -5 and 5
while num<-5 or num>5:
    input("ERROR! Enter a number between -5 and 5: ")

print(f"Entered number = {num}")
