
# Python Comments




#Print Hello, world to console
print("Hello, world")

# Multi Line Comments


#This is a long comment
#and it extends 
#Multiple lines


"""This is also a
perfect example of
multi-line comments"""

# DocString in python


def double(num):
    """
    function to double the number
    """
    return 2 * num

print double(10)
print double.__doc__ #Docstring is available to us as the attribute __doc__ of the function

# Python Indentation


for i in range(10):
    print i


if True:
    print "Machine Learning"
    c = "AAIC"
if True: print "Machine Learning"; c = "AAIC"

# Python Statement




 a = 1  #single statement

# Multi-Line Statement


a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8
print a
#another way is
a = (1 + 2 + 3 +
    4 + 5 + 6 + 
    7 + 8)
print a
a = 10; b = 20; c = 30   #put multiple statements in a single line using ;
