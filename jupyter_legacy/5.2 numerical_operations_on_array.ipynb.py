import numpy as np

# Elementwise Operations




a = np.array([1, 2, 3, 4]) #create an array

a + 1
a ** 2


b = np.ones(4) + 1

a - b
a * b
# Matrix multiplication

c = np.diag([1, 2, 3, 4])

print(c * c)
print("*****************")
print(c.dot(c))


a = np.array([1, 2, 3, 4])
b = np.array([5, 2, 2, 4])
a == b
a > b
#array-wise comparisions
a = np.array([1, 2, 3, 4])
b = np.array([5, 2, 2, 4])
c = np.array([1, 2, 3, 4])

np.array_equal(a, b)
np.array_equal(a, c)


a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)

np.logical_or(a, b)
np.logical_and(a, b)


a = np.arange(5)

np.sin(a)   
np.log(a)
np.exp(a)   #evaluates e^x for each element in a given input


a = np.arange(4)

a + np.array([1, 2])

# Basic Reductions


x = np.array([1, 2, 3, 4])
np.sum(x)
#sum by rows and by columns

x = np.array([[1, 1], [2, 2]])
x
x.sum(axis=0)   #columns first dimension
x.sum(axis=1)  #rows (second dimension)


x = np.array([1, 3, 2])
x.min()
x.max()
x.argmin()# index of minimum element
x.argmax()# index of maximum element


np.all([True, True, False])
np.any([True, False, False])
#Note: can be used for array comparisions
a = np.zeros((50, 50))
np.any(a != 0)
np.all(a == a)
a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
((a <= b) & (b <= c)).all()


x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
x.mean()
np.median(x)
np.median(y, axis=-1) # last axis
x.std()          # full population standard dev.




#load data into numpy array object
data = np.loadtxt('populations.txt')
data
year, hares, lynxes, carrots = data.T #columns to variables
print(year)
#The mean population over time
populations = data[:, 1:]
populations
#sample standard deviations
populations.std(axis=0)
#which species has the highest population each year?

np.argmax(populations, axis=1)

# Broadcasting




a = np.tile(np.arange(0, 40, 10), (3,1))
print(a)

print("*************")
a=a.T
print(a)

b = np.array([0, 1, 2])
b

a + b
a = np.arange(0, 40, 10)
a.shape

a = a[:, np.newaxis]  # adds a new axis -> 2D array
a.shape
a
a + b

# Array Shape Manipulation


a = np.array([[1, 2, 3], [4, 5, 6]])
a.ravel() #Return a contiguous flattened array. A 1-D array, containing the elements of the input, is returned. A copy is made only if needed.
a.T #Transpose
a.T.ravel()




print(a.shape)
print(a)
b = a.ravel()
print(b)
b = b.reshape((2, 3))
b
b[0, 0] = 100
a


a = np.zeros((3, 2))
b = a.T.reshape(3*2)
b[0] = 50
a






z = np.array([1, 2, 3])
z
z[:, np.newaxis]


a = np.arange(4*3*2).reshape(4, 3, 2)
a.shape
a
a[0, 2, 1]


a = np.arange(4)
a.resize((8,))
a


b = a
a.resize((4,)) 


#Sorting along an axis:
a = np.array([[5, 4, 6], [2, 3, 2]])
b = np.sort(a, axis=1)
b
#in-place sort
a.sort(axis=1)
a
#sorting with fancy indexing
a = np.array([4, 3, 1, 2])
j = np.argsort(a)
j
a[j]
