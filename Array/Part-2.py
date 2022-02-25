# 11. Write a Python program to remove a specified item using the index from an array.

from array import *

arr = array('i', [1, 3, 5, 7, 9])
print("Original array : ", arr)
print("Remove the third item form the array : ")
arr.pop(2)
print("New array : ", arr)

# 12. Write a Python program to remove the first occurrence of a specified element from an array.

from array import *

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array : ", arr)
print("Remove the first occurrence of 3 from the said array : ")
arr.remove(3)
print("New array : ", arr)

# 13. Write a Python program to convert an array to an ordinary list with the same items.

from array import *

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array : ", arr)
lst = arr.tolist()
print("Convert the said array to an ordinary list with the same items : ")
print(lst)

# 14. Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct.

def test_duplicate(arr):
    arr_set = set(arr)
    return len(arr) != len(arr_set)

print(test_duplicate([1, 2, 3, 4, 5]))
print(test_duplicate([1, 2, 3, 4, 4]))
print(test_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5]))

# 18. Write a Python program to create an array contains six integers. Also print all the members of the array.

from array import *

arr = array('i', [10, 20, 30, 40, 50])
for i in arr:
    print(i)

# 19. Write a Python program to get an array buffer information.

from array import array

arr = array("I", (12, 25))
print("Array buffer start address in memory and number of elements : ", arr.buffer_info())

# 20. Write a Python program to get the length of an array.

from array import array

def length(arr):
    ctr = 0
    for i in arr:
        ctr += 1
    return ctr

arr = array('i', [10, 20, 30, 40, 50])
print("The length of the array is : ", length(arr))

# 21. Write a Python program to get the array size of types unsigned integer and float.

from array import array

arr = array("I", (12, 25))
print(arr.itemsize)
arr = array("f", (12.236, 36.36))
print(arr.itemsize)
