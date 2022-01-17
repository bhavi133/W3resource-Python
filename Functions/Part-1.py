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

# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_test(str1):
    upper = 0
    lower = 0
    for i in str1:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("Number of upper case letters in a string : ", upper)
    print("Number of lower case letters in a string : ", lower)

str1 = 'The quick Brow Fox'
string_test(str1)

# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(list1):
    nums = []
    for i in list1:
        if i not in nums:
            nums.append(i)
    return nums

list1 = [1,2,3,3,3,3,4,5]
print(unique_list(list1))

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.

def is_prime(n):
    if n == 1:
        print(f"{n} is neither prime nor composite")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")

print(is_prime(1))

# 10. Write a Python program to print the even numbers from a given list.

def is_even(list1):
    result = [i for i in list1 if i % 2 == 0]
    return result

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(is_even(list1))

# 11. Write a Python function to check whether a number is perfect or not.

def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
            print(sum)
    return sum == n
print(perfect_number(10))
