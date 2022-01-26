# 1. Write a Python program to sum all the items in a list.

def sum_list(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum

list1 = [1,2,-8]
print(sum_list(list1))

# 2. Write a Python program to multiply all the items in a list.

def multiply_list(list1):
    tot = 1
    for i in list1:
        tot *= i
    return tot

list1 = [1, 2, -8]
print(multiply_list(list1))

# 3. Write a Python program to get the largest number from a list.

def max_num_in_list(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max

list1 = [1, 2, -8, 0]
print(max_num_in_list(list1))

# 4. Write a Python program to get the smallest number from a list.

def max_num_in_list(list1):
    min = list1[0]
    for i in list1:
        if i <= min:
            min = i
    return min

list1 = [1, 2, -8, 0]
print(max_num_in_list(list1))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def match_words(list1):
    ctr = 0
    for i in list1:
        if len(i) > 2 and i[0] == i[-1]:
            ctr += 1
    return ctr

list1 = ['abc', 'xyz', 'aba', '1221']
print(match_words(list1))

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def func1(n):
    return n[-1]

def func2(list1):
    list2 = [i for i in sorted(list1, key=func1)]
    return list2

list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(func2(list1))

# 7. Write a Python program to remove duplicates from a list.

def remove_duplicates(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    return unique

nums = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(remove_duplicates(nums))

# 8. Write a Python program to check a list is empty or not.

list1 = []
if len(list1) < 1:
    print("List is empty")
else:
    print("List is not empty")

# 9. Write a Python program to clone or copy a list

list1 = [10, 22, 44, 23, 4]
print(list1)
list2 = list1
print(list2)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def long_words(str1, n):
    list1 = [i for i in str1.split() if len(i) > n]
    return list1

str1 = "The quick brown fox jumps over the lazy dog"
print(long_words(str1, 3))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

def common_data(l1, l2):
    for i in l1:
        if i in l2:
            return True
    else:
        return False

print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

colors = ['red', 'green', 'white', 'black', 'pink', 'yellow']
colors = [j for i, j in enumerate(colors) if i not in (0, 3, 4)]
print(colors)

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

arr = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(arr)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

nums = [7, 8, 120, 25, 44, 20, 27]
result = [i for i in nums if i % 2 == 1]
print(result)

# 15. Write a Python program to shuffle and print a specified list.

from random import shuffle

colors = ['red', 'green', 'white', 'black', 'pink', 'yellow']
shuffle(colors)
print(colors)

# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

l1 = [i**2 for i in range(1, 31)]
print(l1[:5])
print(l1[-5:])

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

l1 = [i**2 for i in range(1, 31)]
print(l1[5:])

# 18. Write a Python program to generate all permutations of a list in Python.

from itertools import permutations

colors = ['red', 'white', 'black']
colors = list(permutations(colors))
print(colors)
