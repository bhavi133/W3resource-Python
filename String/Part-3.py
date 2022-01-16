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

# 22. Write a Python program to sort a string lexicographically.

def lexicographic_sort(str1):
    return sorted(sorted(str1), key=str.upper)

print(lexicographic_sort('w3resource'))
print(lexicographic_sort('quickbrown'))

# 23. Write a Python program to remove a newline in Python.

str1 = 'Python Exercises\n'
print(str1)
print(str1.rstrip())

# 24. Write a Python program to check whether a string starts with specified characters.

string = "w3resource.com"
print(string.startswith("w3r"))

# 25. Write a Python program to display formatted text (width=50) as output.

import textwrap

sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print(textwrap.fill(sample_text, width=50))

# 26. Write a Python program to remove existing indentation from all of the lines in a given text.

import textwrap

sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print(textwrap.dedent(sample_text))

# 27. Write a Python program to add a prefix text to all of the lines in a string.

import textwrap

sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)
final_result = textwrap.indent(wrapped, '> ')
print(final_result)

# 28. Write a Python program to set the indentation of the first line.

import textwrap

sample_text = '''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))

# 29. Write a Python program to print the following floating numbers upto 2 decimal places.

x = 3.1415926
y = 12.9999
print("Original Number: ", x)
print(f"Formatted Number: {x:.2f}")
print("Original Number: ", y)
print(f"Formatted Number: {y:.2f}")

# 30. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.

x = 3.1415926
y = -12.9999
print("Original Number:", x)
print(f"Formatted Number with sign: {x:+.2f}")
print("Original Number:", y)
print(f"Formatted Number with sign: {y:+.2f}")
