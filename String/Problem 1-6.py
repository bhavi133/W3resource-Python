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
