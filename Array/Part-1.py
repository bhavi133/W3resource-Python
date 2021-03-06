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

# 4. Write a Python program to get the length in bytes of one array item in the internal representation. 

from array import *

arr = array('i', [1, 3, 5, 7, 9])
print("Original array : ", arr)
print("Length in bytes of one array item : ", arr.itemsize)

# 5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents and also find the size of the memory buffer in bytes.

from array import *

arr = array('i', [1, 3, 5, 7, 9])
print("Original array: ", arr)
print("Current memory address and the length in elements of the buffer : ", arr.buffer_info())
print("The size of the memory buffer in bytes: ", arr.buffer_info()[1] * arr.itemsize)

# 6. Write a Python program to get the number of occurrences of a specified element in an array. 

from array import *

arr = array('i', [1, 3, 5, 3, 7, 9, 3])
n = int(input("Input a number : "))
print("Original array : ", arr)
print(f"Number of occurrences of the number {n} in the said array: ", arr.count(n))

# 7. Write a Python program to append items from inerrable to the end of the array.

from array import *

arr = array('i', [1, 3, 5, 7, 9])
print("Original array : ", arr)
arr.extend(arr)
print("Extended array : ", arr)

# 8. Write a Python program to convert an array to an array of machine values and return the bytes representation.

from array import *

arr = array('b', [119, 51, 114, 101, 115, 111, 117, 114, 99, 101])
res = arr.tobytes()
print("Bytes to string : ", res)

# 9. Write a Python program to append items from a specified list.

from array import *

lst = [1, 2, 6, -8]
print("Items in the list : ", lst)
arr = array('i', lst)
print("Append items from the list : ")
print("Items in the array : ", arr)

# 10. Write a Python program to insert a new item before the second element in an existing array. Go to the editor

from array import *

arr = array('i', [1, 3, 5, 7, 9])
print("Original array : ", arr)
print("Insert new value 4 before 3 : ")
arr.insert(1, 4)
print("New array : ", arr)
