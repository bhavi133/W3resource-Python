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

# 25. Write a Python program to select an item randomly from a list.

from random import choice

l = ['red', 'white', 'black', 'blue']
print(choice(l))

# 26. Write a Python program to check whether two lists are circularly identical.

l1 = [10, 10, 0, 0, 10]
l2 = [10, 10, 10, 0, 0]
l3 = [1, 10, 10, 0, 0]
print("Comparing l1 and l2 : ", ' '.join(map(str, l2)) in ' '.join(map(str, l1*2)))
print("Comparing l1 and l3 : ", ' '.join(map(str, l3)) in ' '.join(map(str, l1*2)))
print("Comparing l2 and l3 : ", ' '.join(map(str, l3)) in ' '.join(map(str, l2*2)))
print("Comparing l2 and l1 : ", ' '.join(map(str, l1)) in ' '.join(map(str, l2*2)))
print("Comparing l3 and l1 : ", ' '.join(map(str, l1)) in ' '.join(map(str, l3*2)))
print("Comparing l3 and l2 : ", ' '.join(map(str, l2)) in ' '.join(map(str, l3*2)))

# 27. Write a Python program to find the second smallest number in a list.

def second_smallest(nums):
    if (len(nums) < 2):
        return
    if ((len(nums) == 2) and (nums[0] == nums[1])):
        return
    duplicate = set()
    unique = []
    for i in nums:
        if i not in duplicate:
            unique.append(i)
            duplicate.add(i)
            unique.sort()
    return unique[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2, 2]))
print(second_smallest([2]))

# 28. Write a Python program to find the second largest number in a list.

def second_largest(nums):
    if (len(nums) < 2):
        return
    if ((len(nums) == 2) and (nums[0] == nums[1])):
        return
    duplicate = set()
    unique = []
    for i in nums:
        if i not in duplicate:
            unique.append(i)
            duplicate.add(i)
            unique.sort()
    return unique[-2]

print(second_largest([1, 2, 3, 4, 4]))
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_largest([2, 2]))
print(second_largest([1]))

# 29. Write a Python program to get unique values from a list.

def unique_values(list1):
    unique = []
    for i in list1:
        if i not in unique:
            unique.append(i)
    return unique

l1 = [10, 20, 30, 40, 20, 50, 60, 40]
print(unique_values(l1))

# 30. Write a Python program to get the frequency of the elements in a list.

def frequency(l1):
    dict1 = {}
    for i in l1:
        dict1[i] = l1.count(i)
    return dict1

l1 = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
print(frequency(l1))

# 31. Write a Python program to count the number of elements in a list within a specified range.

def count_range_in_list(list1, r1, r2):
    ctr = 0
    for i in list1:
        if r1 <= i <= r2:
            ctr += 1
    return ctr

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(list2, 'a', 'e'))

# 32. Write a Python program to check whether a list contains a sublist.

def is_sublist(l1, l2):
    if ''.join(map(str, l2)) in ''.join(map(str, l1)):
        return True
    else:
        return False

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_sublist(a, b))
print(is_sublist(a, c))

# 33. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

list1 = ['p', 'q']
n = 5
result = [f"{j}{i}" for i in range(1, n+1) for j in list1]
print(result)

# 36. Write a Python program to get variable unique identification number or string.

int1 = 100
print(id(int1))
str1 = 'w3resource'
print(id(str1))
