# 16. Write a Python program to get a dictionary from an object's fields.

class dictObj(object):

     def __init__(self):
         self.x = 'red'
         self.y = 'blue'
         self.z = 'black'

     def display(self):
         pass

obj1 = dictObj()
print(obj1.__dict__)

# 17. Write a Python program to remove duplicates from dictionary.

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key, val in student_data.items():
    if val not in result.values():
        result[key] = val

print(result)

# 18. Write a Python program to check a dictionary is empty or not.

dict1 = {}
if not bool(dict1):
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

# 19. Write a Python program to combine two dictionary adding values for common keys.

from collections import Counter

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
dict3 = Counter(dict1) + Counter(dict2)
print(dict3)

# 20. Write a Python program to print all unique values in a dictionary.

dict1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique = set(x for i in dict1 for x in i.values())
print(unique)

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
