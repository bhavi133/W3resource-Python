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

# 51. Write a Python program to print all permutations with given repetition number of characters of a given string.

from itertools import product

def all_repeat(str1, rno):
  chars = list(str1)
  result = []
  for i in product(chars, repeat=rno):
    result.append(i)
  return result

print(all_repeat('xyz', 3))
print(all_repeat('xyz', 2))
print(all_repeat('abcd', 4))

# 52. Write a Python program to find the first repeated character in a given string.

def first_repeated_char(str1):
    for i, j in enumerate(str1):
        print(i, j)
        if str1[0:i+1].count(j) > 1:
            return j
    return None

print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcd"))

# 53. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.

def first_repeated_char_smallest_distance(str1):
    temp = {}
    for ch in str1:
        if ch in temp:
            return ch, str1.index(ch)
        else:
            temp[ch] = 0
    return None

print(first_repeated_char_smallest_distance("abcabc"))
print(first_repeated_char_smallest_distance("abcb"))
print(first_repeated_char_smallest_distance("abcc"))
print(first_repeated_char_smallest_distance("abcxxy"))
print(first_repeated_char_smallest_distance("abc"))))


# 54.Write a Python program to find the first repeated word in a given string.

def first_repeated_word(str1):
    temp = set()
    for word in str1.split():
        if word in temp:
            return word
        else:
            temp.add(word)
    return None

print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc ab ca ab bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))

# 55.Write a Python program to remove spaces from a given string

def remove_spaces(str1):
    str1 = str1.replace(' ', '')
    return str1

print(remove_spaces("w 3 res ou r ce"))
print(remove_spaces("a b c"))
