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
