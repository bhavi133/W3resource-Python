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
