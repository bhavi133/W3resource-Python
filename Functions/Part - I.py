# 1. Write a Python function to find the Max of three numbers

def max_of_three(n1, n2, n3):
    if n1 > n2:
        return n1
    elif n2 > n3:
        return n2
    else:
        return n3

print(max_of_three(3, 6, -5))

# 2. Write a Python function to sum all the numbers in a list.

def sum_of_numbers(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    return sum

list1 = [8, 2, 3, 0, 7]
print(sum_of_numbers(list1))

# 3. Write a Python function to multiply all the numbers in a list.

def multiply_of_numbers(list1):
    total = 1
    for i in list1:
        total = total * i
    return total

list1 = [8, 2, 3, -1, 7]
print(multiply_of_numbers(list1))

# 4. Write a Python program to reverse a string.

def reverse(str1):
    string = ""
    for i in str1:
        string = i + string
    return string

str1 = "1234abcd"
print(reverse(str1))

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)

number = int(input("Input a number:"))
print(factorial(number))

# 6. Write a Python function to check whether a number falls in a given range.

def test_range(n, r1, r2):
    return n in range(r1, r2)

print(test_range(15, 10, 20))
print(test_range(5, 10, 20))
