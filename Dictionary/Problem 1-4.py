# 1. Write a Python program to sort (ascending and descending) a dictionary by value.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(dict1.items())
sort_dict1 = sorted(dict1.items(), key= lambda item: item[1])
print(dict(sort_dict1))
sort_dict1 = sorted(dict1.items(), key= lambda item: item[1], reverse=True)
print(dict(sort_dict1))

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
