
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
