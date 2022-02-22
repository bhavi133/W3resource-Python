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
