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
