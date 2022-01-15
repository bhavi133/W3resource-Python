# 1. Write a Python program to create a set.

set1 = set(range(1, 6))
print(set1)
print(type(set1))

set2 = {1,2,3,'foo','bar'}
print(set2)
print(type(set2))

# 2. Write a Python program to iteration over sets.

set1 = set("w3resource")
for i in set1:
    print(i, end=" ")

# 3. Write a Python program to add member(s) in a set.

set1 = {1, 2}
print(set1)

set1.add(3)
print(set1)

set1.update({4, 5})
print(set1)

# 4. Write a Python program to remove item(s) from a given set.

set1 = {1, 2, 3, 4, 5}
print(set1)

set1.remove(2)
print(set1)

set1.discard(3)
print(set1)

set1.pop()
print(set1)

# 5. Write a Python program to remove an item from a set if it is present in the set.

set1 = {1, 2, 3, 4, 5}
n = int(input("Input a number:"))
if n in set1:
    set1.discard(n)
    print(set1)
else:
    print(set1)

# 6. Write a Python program to create an intersection of sets.

set1 = {"green", "blue"}
set2 = {"blue", "yellow"}
print("Original Sets:")
print(set1)
print(set2)
set3 = set1 & set2
print("Intersection of two said sets using '&' operator:")
print(set3)
print("\n")
set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
print("Original Sets:")
print(set1)
print(set2)
set3 = set1.intersection(set2)
print("Intersection of two said sets using intersection():")
print(set3)

# 7. Write a Python program to create a union of sets.

set1 = {"green", "blue"}
set2 = {"blue", "yellow"}
print("Original Sets:")
print(set1)
print(set2)
set3 = set1 | set2
print("Union of two said sets using '|' operator:")
print(set3)
print("\n")
set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
print("Original Sets:")
print(set1)
print(set2)
set3 = set1.union(set2)
print("Union of two said sets using union():")
print(set3)

# 8. Write a Python program to create set difference.

set1 = {"green", "blue"}
set2 = {"blue", "yellow"}
print("Original Sets:")
print(set1)
print(set2)
diff1 = set1.difference(set2)
print("Difference of set1 - set2 using '-' operator:")
print(diff1)
diff2 = set2.difference(set1)
print("Difference of set2 - set1 using '-' operator:")
print(diff2)
print("\n")
set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
print("Original Sets:")
print(set1)
print(set2)
diff1 = set1.difference(set2)
print("Difference of set1 - set2 using difference():")
print(diff1)
diff2 = set2.difference(set1)
print("Difference of set2 - set1 using difference():")
print(diff2)

# 9. Write a Python program to create a symmetric difference.

set1 = {"green", "blue"}
set2 = {"blue", "yellow"}
print("Original Sets:")
print(set1)
print(set2)
diff1 = set1.symmetric_difference(set2)
print("Symmetric difference of set1 - set2:")
print(diff1)
diff2 = set2.symmetric_difference(set1)
print("Symmetric difference of set2 - set1:")
print(diff2)
print("\n")
set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
print("\nOriginal Sets:")
print(set1)
print(set2)
diff1 = set1.symmetric_difference(set2)
print("Symmetric difference of set1 - set2:")
print(diff1)
diff2 = set2.symmetric_difference(set1)
print("Symmetric difference of set2 - set1:")
print(diff2)

# 10. Write a Python program to check if a set is a subset of another set.

set1 = {"green", "blue"}
set2 = {"blue", "yellow"}
set3 = {"blue"}
print("Original Sets:")
print(set1)
print(set2)
print(set3)
print("\n")
print("Check if a set is a subset of another set, using comparison operators:")
print("\n")
print("If set1 is subset of set2")
print(set1 <= set2)
print("If set2 is subset of set1")
print(set2 <= set1)
print("If set2 is subset of set3")
print(set2 <= set3)
print("If set3 is subset of set2")
print(set3 <= set2)
print("If set1 is subset of set3")
print(set1 <= set3)
print("If set3 is subset of set1")
print(set3 <= set1)
print("\n")
print("Check if a set is a subset of another set, using issubset():")
print("\n")
print("If set1 is subset of set2")
print(set1.issubset(set2))
print("If set2 is subset of set1")
print(set2.issubset(set1))
print("If set2 is subset of set3")
print(set2.issubset(set3))
print("If set3 is subset of set2")
print(set3.issubset(set2))
print("If set1 is subset of set3")
print(set1.issubset(set3))
print("If set3 is subset of set1")
print(set3.issubset(set1))
