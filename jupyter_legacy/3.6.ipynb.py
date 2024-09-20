
# Strings





# How to create a string?


myString = 'Hello'

print(myString)


myString = "Hello"
print(myString)


myString = '''Hello'''
print(myString)

# How to access characters in a string?


myString = "Hello"

#print first Character
print(myString[0])

#print last character using negative indexing
print(myString[-1])

#slicing 2nd to 5th character
print(myString[2:5])


print(myString[15])
print(myString[1.5])

# How to change or delete a string ?


myString = "Hello"
myString[4] = 's' # strings are immutable


del myString # delete complete string
print(myString)

# String Operations

# Concatenation


s1 = "Hello "
s2 = "Satish"

#concatenation of 2 strings
print(s1 + s2)

#repeat string n times
print(s1 * 3)

# Iterating Through String
count = 0
for l in "Hello World":
    if l == 'o':
        count += 1
print(count, ' letters found')

# String Membership Test
print('l' in 'Hello World') #in operator to test membership
print('or' in 'Hello World')

# String Methods


"Hello".lower()
"Hello".upper()
"This will split all words in a list".split()
' '.join(['This', 'will', 'split', 'all', 'words', 'in', 'a', 'list'])
"Good Morning".find("Mo")
s1 = "Bad morning"

s2 = s1.replace("Bad", "Good")

print(s1)
print(s2)

# Python Program to Check where a String is Palindrome or not ?
myStr = "Madam"

#convert entire string to either lower or upper
myStr = myStr.lower()

#reverse string
revStr = reversed(myStr)


#check if the string is equal to its reverse
if list(myStr) == list(revStr):
    print("Given String is palindrome")
else:
    print("Given String is not palindrome")


# Python Program to Sort Words in Alphabetic Order?
myStr = "python Program to Sort words in Alphabetic Order"

#breakdown the string into list of words
words = myStr.split()

#sort the list
words.sort()

#print Sorted words are
for word in words:
    print(word)


