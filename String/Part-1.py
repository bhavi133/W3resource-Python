# 1. Write a Python program to calculate the length of a string

def length_function(string):
    count = 0
    for char in string:
        count += 1
    return count

string = "w3resource"
print(length_function(string))

# 2. Write a Python program to count the number of characters (character frequency) in a string

def frequency(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

string = 'google.com'
print(frequency(string))

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def string_both_ends(string):
    if len(string) >= 2:
        return string[0:2] + string[-2:]
    else:
        return ""

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

string = 'restart'
print(change_char(string))

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def chars_mix_up(string1, string2):
    a = string1[0:2], string2[2:]
    b = string2[0:2], string1[2:]
    print("".join(b), "".join(a))

string1, string2 = 'abc', 'xyz'
chars_mix_up(string1, string2)

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 

def add_string(string):
    if len(string) > 2:
        if string[-3:] != "ing":
            return string + "" + "ing"
        else:
            return string + "" + "ly"
    else:
        return string

print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def not_poor(str1):
    str_not = str1.find('not')
    str_poor = str1.find('poor')
    if str_poor > str_not and str_not > 0 and str_poor > 0:
        str1 = str1.replace(str1[str_not:(str_poor + 4)], 'good')
        return str1
    else:
        return str1

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one. 

def find_longest_word(words_list):
    word = sorted(words_list, reverse=True, key=len)
    return len(word[0]), word[0]

result = find_longest_word(["PHP", "Exercises", "Backend"])
print("Longest word: ", result[1])
print("Length of the longest word: ", result[0])

# 9. Write a Python program to remove the nth index character from a nonempty string.

def remove_char(str1, n):
    return str1[0:n] + str1[n+1:]

print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))

# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 

def change_string(string):
    return string[-1] + string[1:-1] + string[0]

print(change_string('abcd'))
print(change_string('12345'))
