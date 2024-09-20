
# Python if ... else Statement



# if statement syntax







# Flow Chart



# Example
num = 10

# try 0, -1 and None
if None:
    print("Number is positive")
print("This will print always")      #This print statement always print

#change number 


# if ... else Statement

# Syntax:



# Flow Chart



# Example
num = 10
if num > 0:
    print("Positive number")
else:
    print("Negative Number")

# if...elif...else Statement

# Syntax:



# Flow Chart



# Example:
num = 0

if num > 0:
    print("Positive number")
elif num == 0:
    print("ZERO")
else:
    print("Negative Number")

# Nested if Statements



# Example:
num = 10.5

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative Number")

# Python program to find the largest element among three Numbers
num1 = 10
num2 = 50
num3 = 15

if (num1 >= num2) and (num1 >= num3):           #logical operator   and
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("Largest element among three numbers is: {}".format(largest))

