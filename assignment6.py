"""1. create the program of number data type builtin functions

2. string, list, tuple, dictionary, set - builtin functions"""
import math
import random
print(math.ceil(26.23))
print(math.sqrt(4))
print(random.choice([3,47,5,0,8]))
print(max(8,3,5,4,6))
print(min(0,4,6,8,1,5))
print(abs(-34))
print(math.floor(48.07))

#strings
str = "program for strings"
print("string:", str)
print("upper:", str.upper())
print("lower:", str.lower())
print("count:",str.count('o'))
print("length:",len(str))
print(str.isalnum())
print(str.isalpha())

#List

list =['aaa',111,222,'bbb','ccc']
print(list[3])
list.pop(3)
list.append(999)
print(list)
list.remove('aaa')
print(list)
list.insert(1,'rrr')
print(list)

#Tuple

tuple = (2,3,'do','to','so',1)
s = tuple[1:4]
print(tuple)
print(s)