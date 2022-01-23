# 12. Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(str1):
    left_position = 0
    right_position = len(str1) - 1
    while right_position >= left_position:
        if not str1[left_position] == str1[right_position]:
            return False
        left_position += 1
        right_position -= 1
    else:
        return True

print(is_palindrome('aza'))

def is_palindrome(str1):
    return str1 == str1[::-1]

print(is_palindrome('aza'))

# 13. Write a Python function to check whether a string is a pangram or not.

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram('The quick brown fox jumps over the lazy dog'))

# 14. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

str1 = "green-red-yellow-black-white"
str1 = str1.split('-')
str2 = sorted(str1)
print("-".join(str2))

# 15. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def printValues():
    list1 = [i**2 for i in range(1, 31)]
    return list1

print(printValues())

# 16. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"

print(hello())

# 17. Write a Python program to execute a string containing Python code.

str1 = 'print("Hello World!")'
code = """
def sum(x, y):
    return x + y

print('The sum of 2 and 3 is: ', sum(2, 3))
"""
exec(str1)
exec(code)

# 18. Write a Python program to access a function inside a function

def make_adder(x):
    def adder(y):
        return x + y
    return adder

result = make_adder(5)
print(result(3))

# 19. Write a Python program to detect the number of local variables declared in a function.

def abc():
    x = 1
    y = 2.0
    str1= "w3resource"
    val = True
    print("Hello World!")

print(abc.__code__.co_nlocals)

# 20. Write a Python program to find the repeated items of a list.

list1 = [1, 2, 2, 3, 3, 4, 4, 4]
unique = []
for i in list1:
    if list1.count(i) > 1:
        unique.append(i)
print(list(set(unique)))

def repeated_items(list1):
    dict1 = {}
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    list2 = []
    for i, j in dict1.items():
        if dict1[i] > 1:
            list2.append(i)
    return list2

list1 = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]
print(repeated_items(list1))

# 21. Write a Python function to write the fibonacci sequence.

def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fibonacci(15)

# 22. Write a Python program to create a dictionary from a string.

def frequency(string):
    string = string.split()
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

string = 'the quick brown fox jumps over the lazy dog'
print(frequency(string))
