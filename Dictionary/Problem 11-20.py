# 11. Write a Python program to multiply all the items in a dictionary.

def multiply_function(dict1):
    ctr = 1
    for i in dict1.values():
        ctr = ctr * i
    return ctr

dict1 = {'data1':100,'data2':-54,'data3':247}
print(multiply_function(dict1))

# 12. Write a Python program to remove a key from a dictionary.

dict1 = {'a':1,'b':2,'c':3,'d':4}
del dict1['b']
print(dict1)

# 13. Write a Python program to map two lists into a dictionary.

list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]
dict1 = dict(zip(list1, list2))
print(dict1)

# 14. Write a Python program to sort a given dictionary by key.

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for i in sorted(color_dict):
    print(i, color_dict[i])

# 15. Write a Python program to get the maximum and minimum value in a dictionary.

dict1 = {'x':500, 'y':5874, 'z': 560}
key_max = max(dict1.keys(), key=(lambda x: dict1[x]))
key_min = min(dict1.keys(), key=(lambda x: dict1[x]))
print(dict1.keys())
print('Maximum value in a dictionary: ', dict1[key_max])
print('Minimum value in a dictionary: ', dict1[key_min])

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
