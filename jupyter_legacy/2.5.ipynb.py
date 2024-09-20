
# Variables



# Variable Assignments
#We use the assignment operator (=) to assign values to a variable

a = 10
b = 5.5
c = "ML"

# Multiple Assignments
a, b, c = 10, 5.5, "ML"
a = b = c = "AI" #assign the same value to multiple variables at once

# Storage Locations
x = 3

print(id(x))               #print address of variable x
y = 3

print(id(y))               #print address of variable y


y = 2
print(id(y))               #print address of variable y

# Data Types 



# Numbers


a = 5                               #data type is implicitly set to integer
print(a, " is of type", type(a))
a = 2.5                            #data type is changed to float
print(a, " is of type", type(a))
a = 1 + 2j                          #data type is changed to complex number
print(a, " is complex number?") 
print(isinstance(1+2j, complex))

# Boolean


a = True                          #a is a boolean type
print(type(a))

# Python Strings




s = "This is Online AI course"
print(s)
print(s[0])
#last char s[len(s)-1] or s[-1]
#slicing
s[5:]

# Python List


a = [10, 20.5, "Hello"]
print(a[1])               #print 1st index element


a[1] = 30.7
print(a)

# Python Tuple


t = (1, 1.5, "ML")
print(t[1]) #extract particular element
t[1] = 1.25

# Python Set


a = {10, 30, 20, 40, 5}
print(a)
print(type(a))             #print type of a


s = {10, 20, 20, 30, 30, 30}
print(s)                    #automatically set won't consider duplicate elements
print(s[1]) #we can't print particular element in set because 
            #it's unorder collections of items

# Python Dictionary




d = {'a': "apple", 'b': "bat"}
print d['a']

# Conversion between Datatypes


float(5)     #convert interger to float using float() method
int(100.5)   #convert float to integer using int() method
str(20)      #convert integer to string


int('10p')
user = "satish"
lines = 100

print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code" )
#remove str and gives error


a = [1, 2, 3]

print(type(a))      #type of a is list 

s = set(a)          #convert list to set using set() method

print(type(s))      #now type of s is set
list("Hello")       #convert String to list using list() method
