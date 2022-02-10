# 1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

from array import *

arr = array('i', [1, 2, 3, 4, 5])
for i in arr:
    print(i)
print("Access first three items individually")
print(arr[0])
print(arr[2])
print(arr[4])

# 2. Write a Python program to append a new item to the end of the array. 

from array import *

arr = array('i', [1, 3, 5, 7, 9])
print("Original array : ", arr)
arr.append(11)
print("Append 11 at the end of the array : ", arr)

# 3. Write a Python program to reverse the order of the items in the array. 

from array import *

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array : ", arr)
print("Reverse the order of the items : ", arr[::-1])
