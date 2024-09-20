
# Tuples



# Tuple creation
#empty tuple
t = ()

#tuple having integers
t = (1, 2, 3)
print(t)

#tuple with mixed datatypes
t = (1, 'raju', 28, 'abc')
print(t)

#nested tuple
t = (1, (2, 3, 4), [1, 'raju', 28, 'abc'])
print(t)
#only parenthesis is not enough
t = ('satish')
type(t)
#need a comma at the end
t = ('satish',)
type(t)
#parenthesis is optional
t = "satish", 
print(type(t))

print(t)

# Accessing Elements in Tuple
t = ('satish', 'murali', 'naveen', 'srinu', 'brahma')

print(t[1])
#negative index
print(t[-1]) #print last element in a tuple
#nested tuple
t = ('ABC', ('satish', 'naveen', 'srinu'))

print(t[1])
print(t[1][2])
#Slicing
t = (1, 2, 3, 4, 5, 6)

print(t[1:4])

#print elements from starting to 2nd last elements
print(t[:-2])

#print elements from starting to end
print(t[:])

# Changing a Tuple

#unlike lists, tuples are immutable
#This means that elements of a tuple cannot be changed once it has been assigned. But, if the element is itself a mutable datatype like list, its nested items can be changed.
#creating tuple
t = (1, 2, 3, 4, [5, 6, 7])

t[2] = 'x' #will get TypeError
t[4][1] = 'satish'
print(t)
#concatinating tuples

t = (1, 2, 3) + (4, 5, 6)
print(t)
#repeat the elements in a tuple for a given number of times using the * operator.
t = (('satish', ) * 4)
print(t)

# Tuple Deletion
#we cannot change the elements in a tuple. 
# That also means we cannot delete or remove items from a tuple.

#delete entire tuple using del keyword
t = (1, 2, 3, 4, 5, 6)

#delete entire tuple
del t



# Tuple Count
t = (1, 2, 3, 1, 3, 3, 4, 1)

#get the frequency of particular element appears in a tuple
t.count(1)

# Tuple Index
t = (1, 2, 3, 1, 3, 3, 4, 1)

print(t.index(3)) #return index of the first element is equal to 3

#print index of the 1



# Tuple Memebership 
#test if an item exists in a tuple or not, using the keyword in.
t = (1, 2, 3, 4, 5, 6)

print(1 in t)
print(7 in t)

# Built in Functions

# Tuple Length
t = (1, 2, 3, 4, 5, 6)
print(len(t))

# Tuple Sort
t = (4, 5, 1, 2, 3)

new_t = sorted(t)
print(new_t) #Take elements in the tuple and return a new sorted list 
             #(does not sort the tuple itself).
#get the largest element in a tuple
t = (2, 5, 1, 6, 9)

print(max(t))
#get the smallest element in a tuple
print(min(t))
#get sum of elments in the tuple
print(sum(t))
