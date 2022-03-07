"""1. create the program of dictionary withh group of users, products, 
2. access those details
3. create the program of set & sets with different ways"""

#dictionary

dict = {"name": "anu","address": "watercolor","number": 12345}
print("dictionary", dict)
print("uers or keys", dict.keys())
print("values", dict.values())
print(type(dict))
print(dict['name'])
dict['aaa']=000
print(dict)
del dict


print("-----------------------------")

num1 = set([1,2,2,3,4])
num2 = set([4,5,6,6,7])
print("union:", num1 | num2)
print("intersection:", num1 & num2)
print("difference:", num1 - num2)

