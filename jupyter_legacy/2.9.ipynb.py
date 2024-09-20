
# Python while Loop



# Syntax:





# Flow Chart



# Example
#Find product of all numbers present in a list

lst = [10, 20, 30, 40, 60]

product = 1
index = 0

while index < len(lst):
    product *= lst[index]
    index += 1

print("Product is: {}".format(product))


# while Loop with else



numbers = [1, 2, 3,4,5]

#iterating over the list
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
    
else:
    print("no item left in the list")

# Python Program to check given number is Prime number or not
num = int(input("Enter a number: "))        #convert string to int


isDivisible = False;

i=2;
while i < num:
    if num % i == 0:
        isDivisible = True;
        print ("{} is divisible by {}".format(num,i) )
    i += 1;
    
if isDivisible:
    print("{} is NOT a Prime number".format(num))
else:
    print("{} is a Prime number".format(num))


