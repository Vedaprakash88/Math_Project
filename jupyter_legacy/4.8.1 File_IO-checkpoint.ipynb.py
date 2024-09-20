
# FILE I/O



# Opening a File


f = open('example.txt') #open file in current direcotry



# Python File Modes


f = open('example.txt') #equivalent to 'r' 
f = open('example.txt', 'r')

f = open('test.txt', 'w')





# Closing a File


f = open('example.txt')
f.close()


try:
   f = open("example.txt")
   # perform file operations
    
finally:
   f.close()



# Writing to a File


f = open("test.txt", "w")
f.write("This is a First File\n")
f.write("Contains two lines\n")
f.close()
    
    
    



# Reading From a File


f = open("test.txt", "r")
f.read()
f = open("test.txt", "r")
f.read(4)
#f = open("test.txt","r")
f.read(10)


f.tell()
f.seek(0) #bring the file cursor to initial position
print(f.read()) #read the entire file


f.seek(0)
for line in f:
    print(line)


f = open("test.txt", "r")
f.readline()
f.readline()
f.readline()


f.seek(0)
f.readlines()

# Renaming And Deleting Files In Python.


import os

#Rename a file from test.txt to sample.txt
os.rename("test.txt", "sample.txt")
f = open("sample.txt", "r")
f.readline()
#Delete a file sample.txt
os.remove("sample.txt")
f = open("sample.txt", "r")
f.readline()

# Python Directory and File Management






import os
os.getcwd()




os.chdir("/Users/varma/")
os.getcwd()




os.listdir(os.getcwd())




os.mkdir('test')


os.rmdir('test')
import shutil

os.mkdir('test')
os.chdir('./test')
f = open("testfile.txt",'w')
f.write("Hello World")
os.chdir("../")
os.rmdir('test')

# remove an non-empty directory
shutil.rmtree('test')
os.getcwd()

