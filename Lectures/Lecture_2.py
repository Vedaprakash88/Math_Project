
'''
Ex1: Your program gets a simple mathematical expression of the form
"<operand> <operator> <operand>"  as string. Operand is a floating
point value, operator one of the values 'add', 'sub', 'mul', 'div', 'pow'.
Read the parts from the string, evaluate the expression and print the
results to the terminal.
'''

expr = input("Please enter a string in the following format-'<float> <add/sub/mult/div/pow> <float>': ")

operand1, opr, operand2 = expr.split(" ")

print(operand1, opr, operand2)
flt1 = float(operand1)
flt2 = float(operand2)

if opr == "add":
    art_opr = "Addition"
    result = flt1 + flt2
elif opr == "sub":
    art_opr = "Subtraction"
    result = flt1 - flt2
elif opr == "mult":
    art_opr = "Multiplication"
    result = flt1 * flt2
elif opr == "div":
    art_opr = "Division"
    result = flt1 / flt2
elif opr == "pow":
    art_opr = "Power"
    result = flt1 ** flt2
else:
    print("Please check your string and re-try")

print(f'The solution for the {art_opr} operation on string "{expr}" is {result}')
##################################################################################################
my_tuple = (1,2,3,5,6)
a, b, c, d, e = my_tuple

t = (1, 'add', (5, 'mul', (10, 'div', 2))) #recursive data structure
t = ((102, 'pow', 2), 'add', (5, 'mul', (10, 'div', 2)))  # Recursive data  structure

##########################################################################################
def foo():
    global x # NOT recommended to use this process - there is a reason for isolating a process in a function
    x = 'abc'
foo()
print(x)
##########################################################################################
def foo(x):
    if x == 1:
        return 1
    else:
        return(x * foo(x-1))

bar = foo
def func1(f):
    print(f(4))
func1(bar)
#############################################################################################
t = ((102, 'pow', 2), 'add', (5, 'mul', (10, 'div', 2)))  # Recursive data structure

def foo(x):
    if x == 1:
        return 1
    else:
        return(x * foo(x-1))

l = (1, (10, (41, (11, (7, (6, 1))))))

def find_recursive(li, v):
    c, rest = li
    if c == v:
        return True
    elif type(rest) is tuple:
        return find_recursive(rest, v)
    else:
        return v == rest

print(find_recursive(l, 3))

########################################################################
#Create Fibonacci sequence using recursive function.

def fibb(n): #n = 2
    if n <= 1:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)


def fibbonaci(n):  # 2
    if n < 0:
        print("Done")
    else:
        fibbonaci(n-1)
        print(fibb(n)) # fibb(2)

fibbonaci(10)