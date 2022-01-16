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

# 56. Write a Python program to find the second most repeated word in a given string.

def word_count(str1):
    str1 = str1.split()
    dict1 = {}
    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    counts = sorted(dict1.items(), key=lambda x : x[1])
    return counts[-2]

print(word_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))

# 57. Write a Python program to remove spaces from a given string.

def remove_spaces(str1):
    str1 = str1.replace(' ', '')
    return str1

print(remove_spaces("w 3 res ou r ce"))
print(remove_spaces("a b c"))

# 58. Write a Python program to capitalize first and last letters of each word of a given string.

def capitalize_first_last_letters(str1):
    str1 = str1.title()
    str1 = str1.split()
    result = ""
    for word in str1:
        result = result + word[:-1] + word[-1].upper() + " "
    return result[:-1]

print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))

# 59. Write a Python program to remove duplicate characters of a given string.

from collections import OrderedDict

def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))

print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))

# 60. Write a Python program to compute sum of digits of a given string.

def sum_digits_string(str1):
    sum = 0
    for i in str1:
        if i.isdigit():
            sum = sum + int(i)
    return sum

print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))
