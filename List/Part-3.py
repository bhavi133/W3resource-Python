# 41. Write a Python program to create multiple lists.

dic = {}
for i in range(1, 21):
     dic[str(i)] = []
print(dic)

# 42. Write a Python program to find missing and additional values in two lists.

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print("Missing values in second list :  ", ','.join(set(list1).difference(set(list2))))                                                                        
print("Additional values in second list : ", ','.join(set(list2).difference(set(list1))))
