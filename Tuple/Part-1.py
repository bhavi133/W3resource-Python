# 1. Write a Python program to create a tuple.

tup1 = tuple(range(1, 6))
print(tup1)
print(type(tup1))

tup2 = 1, 2, 3, 4, 5
print(tup2)
print(type(tup2))

# 2. Write a Python program to create a tuple with different data types. 

tup1 = (1, 2.0, "Red", True)
print(tup1)

# 3. Write a Python program to create a tuple with numbers and print one item.

tup1 = 5, 10, 15, 20, 25
print(tup1)
tup1 = 5,
print(tup1)

# 4. Write a Python program to unpack a tuple in several variables.

tup1 = (2, 3, 5)
a, b, c = tup1
print(a)
print(b)
print(c)

# 5. Write a Python program to add an item in a tuple.

tup1 = (1, 2, 3, 4)
print(tup1)
tup1 = tup1 + (5,)
print(tup1)

tup1 = (1, 2, 3, 4)
print(tup1)
tup1 = tup1[0:2] + (0, 5) + tup1[2:]
print(tup1)

tup1 = (1, 2, 3, 4)
print(tup1)
list1 = list(tup1)
list1.append(5)
print(tuple(list1))

# 6. Write a Python program to convert a tuple to a string.

tup1 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print("".join(tup1))

tup1 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
string = ""
for i in tup1:
    string = string + i
print(string)

# 7. Write a Python program to get the 4th element and 4th element from last of a tuple.

tup1 = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tup1)
print(tup1[3])
print(tup1[-4])
