import numpy as np
import random

l = list(range(100))
random.shuffle(l)

l
# search for an elemnt q in the list: O(n) where n is the length of the list
q = 31
isFound=False;
for ele in l:
    if ele==31:
        print("Found")
        isFound=True
        break;
if isFound == False:
    print("Not Found")
    
    

#What if the list is sorted? Can we search faster?
# Show O(log n)

import math

#Source: http://www.geeksforgeeks.org/binary-search/ 
#Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + math.floor((r - l)/2)
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1


l.sort();
arr = l;
q =31;
binarySearch(arr,0,len(arr)-1,q)


# Find elements common in two lists:
l1 = list(range(100))
random.shuffle(l1)


l2 = list(range(50))
random.shuffle(l2)

# find common elements : O(n*m)
cnt=0;
for i in l1:
    for j in l2:
        if i==j:
            print(i)
            cnt += 1;
print("Number of common elements:", cnt)                      
# Find elements common in two lists:
l1 = list(range(100))
random.shuffle(l1)


l2 = list(range(50))
random.shuffle(l2)

# find common elemnts in lists in O(n) time and O(m) space if m<n

## add all elements in the smallest list into a hashtable/Dict: O(m) space
smallList = {}
for ele in l2:
    smallList[ele] = 1; # any value is OK. Key is important
    
# Now find common element 
cnt=0;
for i in l1:
    if smallList.get(i) != None: # search happens in constant time.
        print(i);
        cnt += 1;
print("Number of common elements:", cnt)                      

