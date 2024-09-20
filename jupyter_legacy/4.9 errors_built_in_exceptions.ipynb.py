
# Python Errors and Built-in-Exceptions


if a < 3




1 / 0
open('test.txt')

# Python Built-in Exceptions
dir(__builtins__)

# Python Exception Handling - Try, Except and Finally



# Catching Exceptions in Python


# import module sys to get the type of exception
import sys

lst = ['b', 0, 2]

for entry in lst:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
    except:
        print("Oops!", sys.exc_info()[0],"occured.")
        print("Next entry.")
        print("***************************")
print("The reciprocal of", entry, "is", r)

# Catching Specific Exceptions in Python


import sys

lst = ['b', 0, 2]

for entry in lst:
    try:
        print("****************************")
        print("The entry is", entry)
        r = 1 / int(entry)
    except(ValueError):
        print("This is a ValueError.")
    except(ZeroDivisionError):
        print("This is a ZeroError.")
    except:
        print("Some other error")
print("The reciprocal of", entry, "is", r)

# Raising Exceptions


raise KeyboardInterrupt
raise MemoryError("This is memory Error")
try:
    num = int(input("Enter a positive integer:"))
    if num <= 0:
        raise ValueError("Error:Entered negative number")
except ValueError as e:
    print(e)

# try ... finally


try:
    f = open('sample.txt')
    #perform file operations
    
finally:
    f.close()
