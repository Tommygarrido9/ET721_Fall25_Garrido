"""
Tommy Garrido 
Lab 7, accessing data in a file (functions)
Sep 29, 2025
"""

def testing():
    print("TOMMY GARRIDO")

# EXAMPLE 1: Read file
def read_data(filename):
    # pipe a text line in a file with a python code
    with open(filename, "r") as file1:
        filecontent = file1.read()
        print(filecontent)
    # check if the file is closed
    print(f"Is the file closed? {file1.closed}")

# Example 2: Reading specific portion of a file
def read_up(filename):
    with open(filename, 'r') as file1:
        #read the first 30 characters
        print(file1.read(30))
        # read the next 5 characters
        print(file1.read(5))
    
# Example 3: read lines
def read_readline(filename):
    with open(filename, "r") as file1:
        # read up to 20 charaters of the first line
        print(file1.readline(20))
        # continue reading the next line up to 5 characters
        print(file1.readline(5))

#EXAMPLE 4 readlines
def read_all(filename):
    with open(filename, "r") as file1:
        print(file1.readlines())

# EXAMPLE 5: loop through a readlines file
def read_each(filename):
    with open(filename, "r") as file1:
        filelines = file1.readlines()
        for eachline in filelines:
            print(eachline.strip())
            #strip() removes the new line character \n

# EXAMPLE 6: create a new file
def new_file(filename):
    with open(filename, "w") as file1:
        file1.write("Python Basics for data analysis\n")
        file1.write("Tommy Garrido")

# EXAMPLE 7: append data into an existing file

from datetime import datetime
def stamp_date(filename):
    with open(filename, "a") as file:
        file.write(f"\n\n{datetime.now()}")

# EXERCISE
def email_read(filename, email):
    count_email = 0
    with open(filename, "r") as file1:
        filelines = file1.readlines()
        # loop through each line in 'filelines'
        for eachline in filelines:
            if email in eachline:
                count_email += 1
        print(count_email)