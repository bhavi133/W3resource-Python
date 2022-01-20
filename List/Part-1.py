# 1. Write a Python program to sum all the items in a list.

def sum_list(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum

list1 = [1,2,-8]
print(sum_list(list1))

# 2. Write a Python program to multiply all the items in a list.

def multiply_list(list1):
    tot = 1
    for i in list1:
        tot *= i
    return tot

list1 = [1, 2, -8]
print(multiply_list(list1))

# 3. Write a Python program to get the largest number from a list.

def max_num_in_list(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max

list1 = [1, 2, -8, 0]
print(max_num_in_list(list1))

# 4. Write a Python program to get the smallest number from a list.

def max_num_in_list(list1):
    min = list1[0]
    for i in list1:
        if i <= min:
            min = i
    return min

list1 = [1, 2, -8, 0]
print(max_num_in_list(list1))
