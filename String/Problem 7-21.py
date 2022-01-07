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

# 11. Write a Python program to remove the characters which have odd index values of a given string.

def odd_values_string(str1):
    string = ""
    for i in range(len(str1)):
        if i % 2 == 0:
            string = string + str1[i]
    return string

print(odd_values_string('abcdef'))
print(odd_values_string('python'))

# 12. Write a Python program to count the occurrences of each word in a given sentence.

def word_count(text):
    dict1 = {}
    text = text.split()
    print(text)
    for i in text:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

print(word_count('the quick brown fox jumps over the lazy dog.'))

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases. 

input1 = input("What's your favourite language? ")
print("My favourite language is ", input1.upper())
print("My favourite language is ", input1.lower())

# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

def unique_words(list1):
    words = [i for i in list1.split(",")]
    return "".join(sorted(list(words)))

list1 = input("Input comma seperated sequence of words:")
print(unique_words(list1))

# 15. Write a Python function to create the HTML string with tags around the word(s).

def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

# 16. Write a Python function to insert a string in the middle of a string.

def insert_string_middle(str1, word):
    result = str1[0:2] + word + str1[2:]
    return result

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
print(insert_string_middle('<<>>', 'HTML'))

# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

def insert_end(string):
    if len(string) > 2:
        return string[-2:] * 4
    else:
        return string

print(insert_end("python"))
print(insert_end("exercises"))
print(insert_end("py"))

# 18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.

def first_three(str1):
    if len(str1) > 3:
        return str1[0:3]
    else:
        return str1

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))

# 19. Write a Python program to get the last part of a string before a specified character.

str1 = "https://www.w3resource.com/python-exercises/string"
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])

# 20. Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_string(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]
    else:
        return str1

print(reverse_string('abcd'))
print(reverse_string('python'))

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def to_uppercase(str1):
    upper_case = 0
    for i in str1[0:4]:
        if i.upper() == i:
            upper_case += 1
    if upper_case >= 2:
        return str1.upper()
    else:
        return str1

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))


