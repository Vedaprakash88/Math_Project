
# Python Input and Output

# Python Output


print("Hello World")
a = 10
print("The value of a is", a) #python 3
print "The value of a is " + str(a)

# Output Formatting
a = 10; b = 20 #multiple statements in single line.

print("The value of a is {} and b is {}".format(a, b))    #default
a = 10; b = 20  #multiple statements in single line

print("The value of b is {1} and a is {0}".format(a, b)) #specify position of arguments
#we can use keyword arguments to format the string
print("Hello {name}, {greeting}".format(name="satish", greeting="Good Morning"))
#we can combine positional arguments with keyword arguments
print('The story of {0}, {1}, and {other}'.format('Bill', 'Manfred',
                                                       other='Georg'))

# Python Input


num = input("Enter a number: ")
print num
