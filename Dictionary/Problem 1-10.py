# 1. Write a Python program to sort (ascending and descending) a dictionary by value.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(dict1.items())
sorted_dict1 = sorted(dict1.items(), key= lambda item: item[1])
print('Dictionary in ascending order by value:', dict(sorted_dict1))
sorted_dict1 = sorted(dict1.items(), key= lambda item: item[1], reverse=True)
print('Dictionary in descending order by value:', dict(sorted_dict1))

# 2. Write a Python program to add a key to a dictionary

dict1 = {0:10, 1:20}
print(dict1)
dict1.update({2:30})
print(dict1)

# 3. Write a Python program to concatenate following dictionaries to create a new one.

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50,6:60}
dict4 = {}
for i in (dict1, dict2, dict3):
    dict4.update(i)
print(dict4)

# 4. Write a Python program to check whether a given key already exists in a dictionary.

def is_key_present(dict1, k):
    if k in dict1:
        print("The key is present in a dictionary")
    else:
        print("The key is not present in a dictionary")

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
is_key_present(dict1, 5)
is_key_present(dict1, 9)

# 5. Write a Python program to iterate over dictionaries using for loops.

dict1 = {'x': 10, 'y': 20, 'z': 30}
for key, val in dict1.items():
    print(key, val)

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

def generate_dict(n):
    result = {x:x*x for x in range(1, n+1)}
    return result

print(generate_dict(5))

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

def generate_dict():
    result = {x:x**2 for x in range(1, 16)}
    return result

print(generate_dict())

# 8. Write a Python script to merge two Python dictionaries

dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}
dict3 = {}
for i in (dict1, dict2):
    dict3.update(i)
print(dict3)

# 9. Write a Python program to iterate over dictionaries using for loops.

dict1 = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in dict1.items():
     print(color_key, 'corresponds to ', dict1[color_key])

# 10. Write a Python program to sum all the items in a dictionary.

def sum_function(dict1):
    sum = 0
    for i in dict1.values():
        sum += i
    return sum

dict1 = {'data1':100,'data2':-54,'data3':247}
print(sum_function(dict1))


