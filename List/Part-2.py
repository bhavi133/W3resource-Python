# 21. Write a Python program to convert a list of characters into a string.

l1 = ['w', '3', 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e']
str1 = ""
for i in l1:
    str1 += i
print(str1)

# 22. Write a Python program to find the index of an item in a specified list.

nums = [43, 24, 9, 12]
print(nums.index(9))
print(nums.index(43))

# 23. Write a Python program to flatten a shallow list.

list1 = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
list2 = [j for i in list1 for j in i]
print(list2)

# 24. Write a Python program to append a list to the second list.

l1 = ['red', 'white', 'black']
l2 = [0, 2, 3]
l1.extend(l2)
print(l1)
