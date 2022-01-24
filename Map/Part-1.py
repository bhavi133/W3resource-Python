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
