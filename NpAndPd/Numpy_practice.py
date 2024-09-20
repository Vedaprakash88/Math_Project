# nD array library - store numerical arrays and work with them
# Lists are slow and Numpy is very fast. This is due to Numpy using fixed types (i.e., numbers) and lists can store
# flexible types. Therefore, in memory, lists need a lot more space (object type, value, and reference numbers) than numpy
# Lists are not stored in sequence, they are stored scattered-ly in memory.


# Numpys does not need type checking, require less space, uses contiguous memory (continuous blocks of memory are used -
#      helps in SIMD Vector Processing (Single Instruction Multiple Data) i.e., processors can perform one arithmetic
#      operation on multiple values and inputs at a time), effective cache utilization

# We can do all the List operations in Numpy and much more.

# Numpy is more like MATLAB replacement, but Scipy is better at this.
# Useful at plotting (Matplotlib, Seaborn are based on Numpy)
# Backend (Pandas, Connect4, digital Photography, tensorflow etc., are all based on Numpy and heavily depend on it)
# Machine Learning (Tensors in TF)

import numpy as np

# 1-d array
a = np.array([1, 2, 3])  # one row, multi column (i.e., grows in only one axis)
print(a)
# 2-d array
b = np.array([
    [9.0, 8.0, 7.0],  # multi-row, multi colum (i.e., grows in 2 axes)
    [6.0, 5.0, 4.0]
])
print(b)

# 3-d array - Multi-row, multi-column and multi-layer deep (grows in 3 axes)
c = np.array(
    [
        [
            [9.0, 8.0, 7.0],  # first layer (2d)
            [6.0, 5.0, 4.0],
        ]
        ,
        [
            [10.0, 11.0, 12.0],  # second layer (3d)
            [13.0, 14.0, 15.0]
        ]
        ,
        [
            [10.0, 11.0, 12.0],  # Third layer (3d - as it is growing in 3rd dimension)
            [13.0, 14.0, 15.0]
        ]
        ,
        [
            [10.0, 11.0, 12.0],  # fourth layer (3d - as it is growing in 3rd dimension)
            [13.0, 14.0, 15.0]
        ]
    ]
)
print(c.shape)  # (4, 2, 3), i.e., 4 layers in 3rd dimension, 2 rows and 3 columns in each dimension

# you can create 4d array using simple numpy function
# 1. create a 2d array and then specify number of dimensions
d = np.array([[10.0, 11.0, 12.0],  # fourth layer (3d - as it is growing in 3rd dimension)
              [13.0, 14.0, 15.0]], ndmin=4)
print(d)  # shape = (1, 1, 2, 3)


# Copying variables - MUST BE VERY CAREFUL

a = np.array([1,2,3])
b = a
b[0] = 100
print(a) # output is [100, 2, 3]

# this is due to variable points to the same arry location in memory (i.e. identity, IS). Therefore, we need to use copy function
a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a) # output is [1, 2, 3]
print(b) # output is [100, 2, 3]

# mathematics

# any operator is applied to each element in the array, as shown below

a = np.array([1, 2, 3, 4])
print(a+2)  # [3 4 5 6]
print(a-2)  # [-1  0  1  2]
print(a*2)  # [2 4 6 8]
print(a/2)  # [0.5 1.  1.5 2. ]
print(a**2)  # [ 1  4  9 16]
b = np.array([1, 2, 3, 4])
c = a+b
print(c)

print(np.sin(a))
print(np.cos(b))

# Linear algebra

a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)

c = np.matmul(a, b) # simple a*b does not work as the matrix sizes are not same. therefore, this becomes a matrix multiplication
print(c)

a = np.identity(5)
print(a)
print(np.linalg.det(a)) # to find determinant of a matrix
print(np.eye(2))