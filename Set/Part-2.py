# 11. Write a Python program to create a shallow copy of sets.

set1 = {"green", "blue", "yellow", "red"}
print("Original Set:")
print(set1)
print("\nCopy of set1:")
set2 = set1.copy()
print(set2)

# 12. Write a Python program to remove all elements from a given set.

set1 = {"green", "blue", "yellow", "red"}
print("Original Set Elements:")
print(set1)
print("\nAfter removing all elements of the said set:")
print(set1.clear())

# 13. Write a Python program to use of frozensets.

set1 = frozenset([1, 2, 3, 4, 5])
set2 = frozenset([3, 4, 5, 6, 7])
print(set1.isdisjoint(set2))
print(set1.difference(set2))
print(set1.union(set2))

# 14. Write a Python program to find maximum and the minimum value in a set.

set1 = {5, 10, 3, 15, 2, 20}
print("Original Set Elements:")
print(set1)
print("Maximum value of the said set:")
print(max(set1))
print("Minimum value of the said set:")
print(min(set1))

# 15. Write a Python program to find the length of a set.

def length(set1):
    ctr = 0
    for i in set1:
        ctr += 1
    return ctr

set1 = {5, 10, 3, 15, 2, 20}
print("Length of the said set:", length(set1))

# 16. Write a Python program to check if a given value is present in a set or not.

set1 = {5, 10, 3, 15, 2, 9}
print("Original Set: ", set1, "\n")
print("Test if 6 exists in a set:", 6 in set1)
print("Test if 3 exists in a set:", 3 in set1)
print("Test if 9 exists in a set:", 9 in set1)

# 17. Write a Python program to check if two given sets have no elements in common.

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
set3 = {8}
print("Original Sets:")
print(set1)
print(set2)
print(set3)
print("\nConfirm two given sets have no element(s) in common:")
print("\nCompare set1 and set2:", set1.isdisjoint(set2))
print("Compare set2 and set3:", set2.isdisjoint(set3))
print("Compare set3 and set1:", set3.isdisjoint(set1))
