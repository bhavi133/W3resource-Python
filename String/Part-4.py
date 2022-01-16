# 31. Write a Python program to print the following floating numbers with no decimal places.

x = 3.1415926
y = -12.9999
print("Original Number:", x)
print(f"Formatted Number with no decimal places: {x:.0f}")
print("Original Number:", y)
print(f"Formatted Number with no decimal places: {y:.0f}")

# 32. Write a Python program to print the following integers with zeros on the left of specified width.

x = 3
y = 123
print("\nOriginal Number: ", x)
print(f"Formatted Number(left padding, width 2): {x:0>2d}")
print("Original Number: ", y)
print(f"Formatted Number(left padding, width 2): {y:0>6d}")

# 33. Write a Python program to print the following integers with '*' on the right of specified width.

x = 3
y = 123
print("\nOriginal Number: ", x)
print(f"Formatted Number(right padding, width 2): {x:*<2d}")
print("Original Number: ", y)
print(f"Formatted Number(right padding, width 2): {y:*<6d}")

# 34. Write a Python program to display a number with a comma separator. Go to the editor

x = 3000000
y = 30000000
print("Original Number: ", x)
print(f"Formatted Number with comma separator: {x:,}")
print("Original Number: ", y)
print(f"Formatted Number with comma separator: {y:,}")

# 35. Write a Python program to format a number with a percentage.

x = 0.25
y = -0.25
print("Original Number: ", x)
print(f"Formatted Number with percentage: {x:.2%}")
print("Original Number: ", y)
print(f"Formatted Number with percentage: {y:.2%}")

# 36. Write a Python program to display a number in left, right and center aligned of width 10.

x = 22
print("Original Number: ", x)
print(f"Left aligned (width 10)   : {x:< 10d}")
print(f"Right aligned (width 10)  : {x:10d}")
print(f"Center aligned (width 10) : {x:^10d}")

# 37. Write a Python program to count occurrences of a substring in a string.

def substring(str1, sub_str1):
    return str1.count(sub_str1)

str1 = 'the quick brown fox jumps over the lazy dog.'
sub_str1 = 'the'
print(substring(str1, sub_str1))

# 38. Write a Python program to reverse a string.

def reverse_string(str1):
    string = ""
    for i in str1:
        string = i + string
    return string

print(reverse_string("abcdef"))
print(reverse_string("Python Exercises."))

# 39. Write a Python program to reverse words in a string.

def reverse_string_words(str1):
    str1 = str1.split()
    string = ""
    for i in str1:
        string = i + " " + string
    return string

print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))

# 40. Write a Python program to strip a set of characters from a string.

def strip_chars(str1, chars):
    words = []
    chars = list(chars)
    for i in str1:
        if i not in chars:
            words.append(i)
    return "".join(words)


print("Original String: ")
print("The quick brown fox jumps over the lazy dog.")
chars = "aeiou"
print(f"After stripping {chars}")
print(strip_chars("The quick brown fox jumps over the lazy dog.", chars))
