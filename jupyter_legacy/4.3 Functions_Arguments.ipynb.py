
# Function Arguments

def greet(name, msg):
    """
    This function greets to person with the provided message
    """
    print("Hello {0} , {1}".format(name, msg))

#call the function with arguments
greet("satish", "Good Morning")

#suppose if we pass one argument

greet("satish") #will get an error


# Different Forms of Arguments

# 1. Default Arguments


def greet(name, msg="Good Morning"):
    """
    This function greets to person with the provided message
    if message is not provided, it defaults to "Good Morning"
    """
    print("Hello {0} , {1}".format(name, msg))

greet("satish", "Good Night")

#with out msg argument
greet("satish")




#will get a SyntaxError : non-default argument follows default argument

# 2. Keyword Arguments



# Example:
def greet(**kwargs):
    """
    This function greets to person with the provided message
    """
    if kwargs:
        print("Hello {0} , {1}".format(kwargs['name'], kwargs['msg']))
greet(name="satish", msg="Good Morning")


# 3. Arbitary Arguments



# Example:
def greet(*names):
    """
    This function greets all persons in the names tuple 
    """
    print(names)
    
    for name in names:
        print("Hello,  {0} ".format(name))

greet("satish", "murali", "naveen", "srikanth")


