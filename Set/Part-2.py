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
