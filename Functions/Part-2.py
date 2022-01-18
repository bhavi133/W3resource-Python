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
