
# Dictionary



# Dict Creation
#empty dictionary
my_dict = {}

#dictionary with integer keys
my_dict = {1: 'abc', 2: 'xyz'}
print(my_dict)

#dictionary with mixed keys
my_dict = {'name': 'satish', 1: ['abc', 'xyz']}
print(my_dict)


#create empty dictionary using dict()
my_dict = dict()

my_dict = dict([(1, 'abc'), (2, 'xyz')])    #create a dict with list of tuples
print(my_dict)

# Dict Access
my_dict = {'name': 'satish', 'age': 27, 'address': 'guntur'}

#get name
print(my_dict['name'])
#if key is not present it gives KeyError
print(my_dict['degree'])
#another way of accessing key
print(my_dict.get('address'))
#if key is not present it will give None using get method
print(my_dict.get('degree'))

# Dict Add or Modify  Elements
my_dict = {'name': 'satish', 'age': 27, 'address': 'guntur'}

#update name 
my_dict['name'] = 'raju'

print(my_dict)
#add new key
my_dict['degree'] = 'M.Tech'

print(my_dict)

# Dict Delete or Remove Element
#create a dictionary
my_dict = {'name': 'satish', 'age': 27, 'address': 'guntur'}

#remove a particular item
print(my_dict.pop('age'))

print(my_dict)
my_dict = {'name': 'satish', 'age': 27, 'address': 'guntur'}

#remove an arbitarty key
my_dict.popitem()

print(my_dict)
squares = {2: 4, 3: 9, 4: 16, 5: 25}

#delete particular key
del squares[2]

print(squares)
#remove all items
squares.clear()

print(squares)
squares = {2: 4, 3: 9, 4: 16, 5: 25}

#delete dictionary itself
del squares

print(squares) #NameError because dict is deleted

# Dictionary Methods
squares = {2: 4, 3: 9, 4: 16, 5: 25}

my_dict = squares.copy()
print(my_dict)
#fromkeys[seq[, v]] -> Return a new dictionary with keys from seq and value equal to v (defaults to None).
subjects = {}.fromkeys(['Math', 'English', 'Hindi'], 0)
print(subjects)
subjects = {2:4, 3:9, 4:16, 5:25}
print(subjects.items()) #return a new view of the dictionary items (key, value)
subjects = {2:4, 3:9, 4:16, 5:25}
print(subjects.keys()) #return a new view of the dictionary keys
subjects = {2:4, 3:9, 4:16, 5:25}
print(subjects.values()) #return a new view of the dictionary values
#get list of all available methods and attributes of dictionary
d = {}
print(dir(d))

# Dict Comprehension
#Dict comprehensions are just like list comprehensions but for dictionaries

d = {'a': 1, 'b': 2, 'c': 3}
for pair in d.items():
    print(pair)
#Creating a new dictionary with only pairs where the value is larger than 2
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_dict = {k:v for k, v in d.items() if v > 2}
print(new_dict)
#We can also perform operations on the key value pairs
d = {'a':1,'b':2,'c':3,'d':4,'e':5}
d = {k + 'c':v * 2 for k, v in d.items() if v > 2}
print(d)

