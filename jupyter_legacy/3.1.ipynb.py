
# Lists





# List Creation
emptyList = []

lst = ['one', 'two', 'three', 'four'] # list of strings

lst2 = [1, 2, 3, 4] #list of integers

lst3 = [[1, 2], [3, 4]] # list of lists

lst4 = [1, 'ramu', 24, 1.24] # list of different datatypes

print(lst4)


# List Length
lst = ['one', 'two', 'three', 'four']

#find length of a list
print(len(lst))

# List Append
lst = ['one', 'two', 'three', 'four']

lst.append('five') # append will add the item at the end

print(lst)

# List Insert
#syntax: lst.insert(x, y) 

lst = ['one', 'two', 'four']

lst.insert(2, "three") # will add element y at location x

print(lst)


# List Remove
#syntax: lst.remove(x) 

lst = ['one', 'two', 'three', 'four', 'two']

lst.remove('two') #it will remove first occurence of 'two' in a given list

print(lst)

# List Append & Extend
lst = ['one', 'two', 'three', 'four']

lst2 = ['five', 'six']

#append 
lst.append(lst2)

print(lst)
lst = ['one', 'two', 'three', 'four']

lst2 = ['five', 'six']

#extend will join the list with list1

lst.extend(lst2)

print(lst)

# List Delete
#del to remove item based on index position

lst = ['one', 'two', 'three', 'four', 'five']

del lst[1]
print(lst)

#or we can use pop() method
a = lst.pop(1)
print(a)

print(lst)
lst = ['one', 'two', 'three', 'four']

#remove an item from list
lst.remove('three')

print(lst)

# List realted keywords in Python
#keyword 'in' is used to test if an item is in a list
lst = ['one', 'two', 'three', 'four']

if 'two' in lst:
    print('AI')

#keyword 'not' can combined with 'in'
if 'six' not in lst:
    print('ML')

# List Reverse
#reverse is reverses the entire list

lst = ['one', 'two', 'three', 'four']

lst.reverse()

print(lst)

# List Sorting


#create a list with numbers
numbers = [3, 1, 6, 2, 8]

sorted_lst = sorted(numbers)


print("Sorted list :", sorted_lst)

#original list remain unchanged
print("Original list: ", numbers)
#print a list in reverse sorted order
print("Reverse sorted list :", sorted(numbers, reverse=True))

#orginal list remain unchanged
print("Original list :",  numbers)
lst = [1, 20, 5, 5, 4.2]

#sort the list and stored in itself
lst.sort()

# add element 'a' to the list to show an error

print("Sorted list: ", lst)
lst = [1, 20, 'b', 5, 'a']
print(lst.sort()) # sort list with element of different datatypes.


# List Having Multiple References
lst = [1, 2, 3, 4, 5]
abc = lst
abc.append(6)

#print original list
print("Original list: ", lst)

# String Split to create a list
#let's take a string

s = "one,two,three,four,five"
slst = s.split(',')
print(slst)
s = "This is applied AI Course"
split_lst = s.split() # default split is white-character: space or tab
print(split_lst)

# List Indexing


lst = [1, 2, 3, 4]
print(lst[1]) #print second element

#print last element using negative index
print(lst[-2])

# List Slicing


numbers = [10, 20, 30, 40, 50,60,70,80]

#print all numbers
print(numbers[:]) 

#print from index 0 to index 3
print(numbers[0:4])

print (numbers)
#print alternate elements in a list
print(numbers[::2])


#print elemnts start from 0 through rest of the list
print(numbers[2::2])


# List extend using "+"
lst1 = [1, 2, 3, 4]
lst2 = ['varma', 'naveen', 'murali', 'brahma']
new_lst = lst1 + lst2

print(new_lst)

# List Count
numbers = [1, 2, 3, 1, 3, 4, 2, 5]

#frequency of 1 in a list
print(numbers.count(1))

#frequency of 3 in a list
print(numbers.count(3))

# List Looping
#loop through a list

lst = ['one', 'two', 'three', 'four']

for ele in lst:
    print(ele)

# List Comprehensions


# without list comprehension
squares = []
for i in range(10):
    squares.append(i**2)   #list append
print(squares)
#using list comprehension
squares = [i**2 for i in range(10)]
print(squares)
#example

lst = [-10, -20, 10, 20, 50]

#create a new list with values doubled
new_lst = [i*2 for i in lst]
print(new_lst)

#filter the list to exclude negative numbers
new_lst = [i for i in lst if i >= 0]
print(new_lst)


#create a list of tuples like (number, square_of_number)
new_lst = [(i, i**2) for i in range(10)]
print(new_lst)

# Nested List Comprehensions
#let's suppose we have a matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

#transpose of a matrix without list comprehension
transposed = []
for i in range(4):
    lst = []
    for row in matrix:
        lst.append(row[i])
    transposed.append(lst)

print(transposed)

#with list comprehension
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

