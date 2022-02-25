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
