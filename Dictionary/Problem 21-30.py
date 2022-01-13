# 21. Write a Python program to create a dictionary from a string.

def frequency(string):
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

string = 'w3resource'
print(frequency(string))

# 22. Write a Python program to count the values associated with key in a dictionary. 

student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))

# 23. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.

dict1 = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
         'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
         'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

for j in dict1.values():
    print(j[4])

# 24. Write a Python program to drop empty items from a given dictionary.

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
print(dict1)
print("New Dictionary after dropping empty items:")
dict1 = {key:val for (key, val) in dict1.items() if val is not None}
print(dict1)
