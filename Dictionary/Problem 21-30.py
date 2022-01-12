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
