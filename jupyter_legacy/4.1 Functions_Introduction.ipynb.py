
# Python Functions





# Syntax:





# Example:
def print_name(name):
    """ 
    This function prints the name
    """
    print("Hello " + str(name)) 
    

# Function Call


print_name('satish')


# Doc String






print(print_name.__doc__) # print doc string of the function


# return Statement






def get_sum(lst):
    """
    This function returns the sum of all the elements in a list
    """
    #initialize sum
    _sum = 0
    
    #iterating over the list
    for num in lst:
        _sum += num
    return _sum

s = get_sum([1, 2, 3, 4])
print(s)

#print doc string
print(get_sum.__doc__)


# How Function works in Python?



# Scope and Life Time of Variables









# Example:
global_var = "This is global variable"

def test_life_time():
    """
    This function test the life time of a variables
    """
    local_var = "This is local variable"
    print(local_var)       #print local variable local_var
    
    print(global_var)      #print global variable global_var
    
    

#calling function
test_life_time()

#print global variable global_var
print(global_var)

#print local variable local_var
print(local_var)


# Python program to print Highest Common Factor (HCF) of two numbers
def computeHCF(a, b):
    """
    Computing HCF of two numbers
    """
    smaller = b if a > b else a  #consice way of writing if else statement
    
    hcf = 1
    for i in range(1, smaller+1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf

num1 = 6
num2 = 36

print("H.C.F of {0} and {1} is: {2}".format(num1, num2, computeHCF(num1, num2)))

