# 41. Write a Python program to count repeated characters in a string.

import collections

str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for i in str1:
    d[i] = d[i] + 1

for i in sorted(d, key=d.get, reverse=True):
  if d[i] > 1:
      print(f"{i} {d[i]}")

# 42. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.

area = 1256.66
volume = 1254.725
decimal = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimal))
decimal = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimal))

# 43. Write a Python program to print the index of the character in a string.

string = "w3resource"
for i, j in enumerate(string):
    print(f"Current character {j} position at {i}")

# 44. Write a Python program to check whether a string contains all letters of the alphabet.

import string

alphabet = set(string.ascii_lowercase)
print(alphabet)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)


# 45. Write a Python program to convert a given string into a list of words.

str1 = 'the quick brown fox jumps over the lazy dog'
print(str1.split(" "))
str1 = 'the-quick-brown-fox-jumps-over-the-lazy-dog'
print(str1.split("-"))

# 46. Write a Python program to lowercase first n characters in a string.

str1 = "W3RESOURCE.COM"
print(str1[0:4].lower() + str1[4:])

# 47. Write a Python program to swap comma and dot in a string

amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)

# 48. Write a Python program to count and display the vowels of a given text.

def display_vowel(str1):
    vowels = list('aeiouAEIOU')
    result = []
    for i in str1:
        if i in vowels:
            result.append(i)
    print(len(result))
    print(result)

display_vowel('w3resource')

# 49. Write a Python program to split a string on the last occurrence of the delimiter.

str1 = "w,3,r,e,s,o,u,r,c,e"
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 3))
print(str1.rsplit(',', 5))

# 50. Write a Python program to find the first non-repeating character in given string

def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for i in str1:
        if i in ctr:
            ctr[i] += 1
        else:
            ctr[i] = 1
            char_order.append(i)
    print(char_order)
    for i in char_order:
        if ctr[i] == 1:
            return i
    return None

print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))
