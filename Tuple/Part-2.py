# 12. Write a Python program to remove an item from a tuple.

tup1 = (1, 2, 3, 4, 5)
print(tup1)
tup1 = tup1[0:2] + tup1[3:]
print(tup1)

tup1 = (1, 2, 3, 4, 5)
print(tup1)
list1 = list(tup1)
list1.remove(3)
print(tuple(list1))

# 13. Write a Python program to slice a tuple.

tup1 = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tup1)
print(tup1[0:4])
print(tup1[:])
print(tup1[5:8:1])
print(tup1[0::2])
print(tup1[-1:-4:-1])
print(tup1[-1::-1])

# 14. Write a Python program to find the index of an item of a tuple.

tup1 = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tup1)
print(tup1.index('w'))
print(tup1.index('r', 3))
print(tup1.index('e', 2, 5))
print(tup1.index(5))

# 15. Write a Python program to find the length of a tuple.

tup1 = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tup1)
print("Length of a tuple:", len(tup1))
