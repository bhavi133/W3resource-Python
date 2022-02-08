# 1. Write a Python program to triple all numbers of a given list of integers. Use Python map.

list1 = [1, 2, 3, 4, 5, 6]
print("Original List:")
print(list1)
list2 = list(map(lambda x : x * 3, list1))
print("Triple of said list numbers:")
print(list2)

# 2. Write a Python program to add three given lists using Python map and lambda.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
print("Original Lists:")
print(l1)
print(l2)
print(l3)
l4 = list(map(lambda x, y, z : x + y + z, l1, l2, l3))
print("New list after adding above three lists:")
print(l4)

# 3. Write a Python program to listify the list of given strings individually using Python map.

colors= ['Red', 'Blue', 'Black', 'White', 'Pink']
print("Original List:")
print(colors)
print("After listify the list of strings are:")
list1 = list(map(list, colors))
print(list1)

# 4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.

bases = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original bases and index:")
print(base
list1 = list(map(pow, bases, index))
print("Power of said number in bases raised to the corresponding number in the index:")
print(list1)

# 5. Write a Python program to square the elements of a list using map() function.

list1 = [4, 5, 2, 9]
print("Original List:")
print(list1)
list2 = list(map(lambda x : x ** 2, list1))
print("Square the elements of the said list using map():")
print(list2)

# 6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.

def change_cases(string):
    return str(string).upper(), str(string).lower()

chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:")
print(chars)
result = set(map(change_cases, chars))
print("After converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(result)

# 7. Write a Python program to add two given lists and find the difference between lists. Use map() function.

def addition_subtrction(x, y):
    return x + y, x - y

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

list1 = list(map(addition_subtrction, nums1, nums2))
print(list1)

# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

list1 = [1, 2, 3, 4]
tup1 = (0, 1, 2, 3)
print("Original List:")
print(list1)
print("Original Tuple:")
print(tup1)
result1 = list(map(str, list1))
print("\nList of strings:")
print(result1)
result2 = tuple(map(str, tup1))
print("Tuple of strings:")
print(result2)

# 9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.

student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
print("Original Data:")
print(student_data)
student_name = list(map(lambda x : x[0], student_data))
student_dob = list(map(lambda x : x[1], student_data))
student_weight = list(map(lambda x : int(x[2][:-2]), student_data))
print("\nStudent Name:")
print(student_name)
print("Student DOB:")
print(student_dob)
print("Student Weight:")
print(student_weight)

# 10. Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate a list of the numbers.

def fibonacci(n):
    list1 = []
    list2 = []
    a = 0
    b = 1
    if n == 0:
        print(-1)
    elif n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    else:
        list1.append(a)
        list1.append(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            list2.append(c)
        list3 = list1 + list2
        print(list3)
        list4 = list(map(lambda x : x ** 2, list3))
        print(list4)

fibonacci(10)

# 11. Write a Python program to compute the sum of elements of a given array of integers, use map() function. Go to the editor

def sum_of_elements(list1):
    sum = 0
    for i in list1:
        sum += int(i)
    return sum

list1 = [1, 2, 3, 4, 5, -15]
result = list(map(int, list1))
print("Sum of all elements of the said list:")
print(sum_of_elements(list1))
      
# 12. Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers.

def func(list1):
    n = len(list1)
    n1 = 0
    n2 = 0
    n3 = 0
    for i in list1:
        if i < 0:
            n1 += 1
        elif i == 0:
            n2 += 1
        else:
            n3 += 1
    return round(n1/n, 2), round(n2/n, 2), round(n3/n, 2)
      
list1 = ['0', '1', '2', '-1', '-5', '6', '0', '-3', '-2', '3', '4', '6', '8']
result = list(map(int, list1))
print("Ratio of positive numbers, negative numbers and zeroes:")
print(func(result))
      
# 13. Write a Python program to count the same pair in two given lists. use map() function.

from operator import eq

def count_same_pair(list1, list2):
    result = sum(map(eq, list1, list2))
    return result

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [2, 2, 3, 1, 2, 6, 7, 9]
print("Original Lists:")
print(list1)
print(list2)
print("\nNumber of same pair of the said two given lists:")
print(count_same_pair(list1, list2))
      
# 14. Write a Python program to convert a given list of strings into list of lists using map function.

colors = ["Red", "Green", "Black", "Orange"]
print('Original list of strings:')
print(colors)
result = list(map(list, colors))
print("\nConvert the said list of strings into list of lists:")
print(result)

15. Write a Python program to convert a given list of tuples to a list of strings using map function.

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
result1 = list(map(' '.join, colors))
print("\nConvert the said list of tuples to a list of strings:")
print(result1)

names = [('Sheridan','Gentry'), ('Laila','Mckee'), ('Ahsan','Rivas'), ('Conna','Gonzalez')]
print("\nOriginal list of tuples:")
print(names)
result2 = list(map(' '.join, names))
print("\nConvert the said list of tuples to a list of strings:")
print(result2)
