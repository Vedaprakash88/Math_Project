
# Modules





# How to import a module?


import example #imported example module



example.add(10, 20)




# Examples:
import math
print(math.pi)

import datetime
datetime.datetime.now()


# import with renaming
import math as m
print(m.pi)


# from...import statement


from datetime import datetime 
datetime.now()


# import all names
from math import *
print("Value of PI is " + str(pi))


# dir() built in function


dir(example)

print(example.add.__doc__)

