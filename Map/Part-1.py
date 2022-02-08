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

6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.

def change_cases(string):
    return str(string).upper(), str(string).lower()

chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:")
print(chars)
result = set(map(change_cases, chars))
print("After converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(result)
