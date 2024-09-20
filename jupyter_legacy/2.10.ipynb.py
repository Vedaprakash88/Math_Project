
# Python for Loop



# Syntax:





# Flow Chart



# Example
#Find product of all numbers present in a list

lst = [10, 20, 30, 40, 50]

product = 1
#iterating over the list
for ele in lst:
    product *= ele

print("Product is: {}".format(product))

# range() function


#print range of 10
for i in range(10):
    print(i)
#print range of numbers from 1 to 20 with step size of 2
for i in range(0, 20, 5):
    print(i)
lst = ["satish", "srinu", "murali", "naveen", "bramha"]

#iterate over the list using index
#for index in range(len(lst)):
#    print(lst[index])
for ele in lst:
    print(ele)

# for loop with else


numbers = [1, 2, 3]

#iterating over the list
for item in numbers:
    print(item)
else:
    print("no item left in the list")
for item in numbers:
    print(item)
    if item % 2 == 0:
        break
else:
    print("no item left in the list")

# Python Program to display all prime numbers within an interval
index1 = 20
index2 = 50

print("Prime numbers between {0} and {1} are :".format(index1, index2))

for num in range(index1, index2+1):      #default step size is 1
    if num > 1:
        isDivisible = False;
        for index in range(2, num):
            if num % index == 0:
                isDivisible = True;
        if not isDivisible:        
            print(num);
    

