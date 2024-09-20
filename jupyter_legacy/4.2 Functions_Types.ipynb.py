
# Types Of Functions



# Built-in Functions

# 1. abs()
# find the absolute value

num = -100

print(abs(num))


# 2. all()

#return value of all() function

lst = [1, 2, 3, 4]
print(all(lst)) 

lst = (0, 2, 3, 4)    # 0 present in list 
print(all(lst))

lst = []              #empty list always true
print(all(lst))

lst = [False, 1, 2]   #False present in a list so all(lst) is False
print(all(lst))


# dir()


numbers = [1, 2, 3]

print(dir(numbers))


# divmod()


print(divmod(9, 2)) #print quotient and remainder as a tuple

#try with other number


# enumerate()




numbers = [10, 20, 30, 40]

for index, num in enumerate(numbers,10):
    print("index {0} has value {1}".format(index, num))
    

# filter()




def find_positive_number(num):
    """
    This function returns the positive number if num is positive
    """
    if num > 0:
        return num
    
number_list = range(-10, 10) #create a list with numbers from -10 to 10
print(list(number_list))

positive_num_lst = list(filter(find_positive_number, number_list))

print(positive_num_lst)


# isinstance()




lst = [1, 2, 3, 4]
print(isinstance(lst, list))

#try with other datatypes tuple, set
t = (1,2,3,4)
print(isinstance(t, list))

# map()




numbers = [1, 2, 3, 4]

#normal method of computing num^2 for each element in the list.
squared = []
for num in numbers:
    squared.append(num ** 2)

print(squared)

numbers = [1, 2, 3, 4]

def powerOfTwo(num):
    return num ** 2

#using map() function
squared = list(map(powerOfTwo, numbers))
print(squared)


# reduce()


#product of elemnts in a list
product = 1
lst = [1, 2, 3, 4]

# traditional program without reduce()
for num in lst:
    product *= num
print(product)

#with reduce()
from functools import reduce # in Python 3.

def multiply(x,y):
    return x*y;

product = reduce(multiply, lst)
print(product)


# 2. User-defined Functions





# Advantages



# Example:
def product_numbers(a, b):
    """
    this function returns the product of two numbers
    """
    product = a * b
    return product

num1 = 10
num2 = 20
print "product of {0} and {1} is {2} ".format(num1, num2, product_numbers(num1, num2))

# Python program to make a simple calculator that can add, subtract, multiply and division
def add(a, b):
    """
    This function adds two numbers
    """
    return a + b

def multiply(a, b):
    """
    This function multiply two numbers
    """
    return a * b

def subtract(a, b):
    """
    This function subtract two numbers
    """
    return a - b

def division(a, b):
    """
    This function divides two numbers
    """
    return a / b

print("Select Option")
print("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

#take input from user
choice = int(input("Enter choice 1/2/3/4"))

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if choice == 1:
    print("Addition of {0} and {1} is {2}".format(num1, num2, add(num1, num2)))
elif choice == 2:
    print("Subtraction of {0} and {1} is {2}".format(num1, num2, subtract(num1, num2)))
elif choice == 3:
    print("Multiplication of {0} and {1} is {2}".format(num1, num2, multiply(num1, num2)))
elif choice == 4:
    print("Division of {0} and {1} is {2}".format(num1, num2, division(num1, num2)))
else:
    print("Invalid Choice")

