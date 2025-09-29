"""
Tommy Garrido 
Lab 7, accessing data in a file (functions)
Sep 29, 2025
"""

def testing():
    print("TOMMY GARRIDO")

def read_data(filename):
    # pipe a text line in a file with a python code
    fileuser = open(filename, 'r')
    # use a loop to go over each line in file user
    for each in fileuser:
        print(each)
    