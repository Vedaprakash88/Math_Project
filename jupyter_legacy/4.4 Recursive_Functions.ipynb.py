
# Recurison



# Example:
#python program to print factorial of a number using recurion

def factorial(num):
    """
    This is a recursive function to find the factorial of a given number
    """
    return 1 if num == 1 else (num * factorial(num-1))

num = 5
print ("Factorial of {0} is {1}".format(num, factorial(num)))


# Advantages



# Disadvantages



# Python program to display the fibonacci sequence up to n-th term using recursive function
def fibonacci(num):
    """
    Recursive function to print fibonacci sequence
    """
    return num if num <= 1 else fibonacci(num-1) + fibonacci(num-2)

nterms = 10
print("Fibonacci sequence")
for num in range(nterms):
    print(fibonacci(num))

