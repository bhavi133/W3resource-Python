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
print("Intersection of two said sets using & operator:")
print(set3)

set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
print("\nOriginal Sets:")
print(set1)
print(set2)
set3 = set1.intersection(set2)
print("Intersection of two said sets using intersection():")
print(set3)
