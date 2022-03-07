#sring insert

list= '[[]]<<>>'
list1=list[0:2]+'Python'+list[2:]
print(list1)

#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
str= '{{}}'
str1= str[0:2]+'PHP'+str[2:]
print(str1)

#https://www.python.org/python-exercises
#Write a Python program to get the last part of a string before a specified character
string = "https://www.python.org/python-exercises"
print(string[12:])
string1="https://www.python.org/python"
print(string1[:19])

string2="google.com"
for i in set(string2):
    string3=(string2.count(i))
print(i, string3)

#Write a Python program to remove a newline in Python
import re
line=["an\nu","ra\ndha","water\ncolor\n","tam\npa"]
new=[]
for j in line:
    new.append(j.replace("\n", ""))
print("new list", new) 

#Write a Python program to check whether a string starts with specified characters
line1="datastructurequality"
line2=line1[:4]+line1[-7:-2]+line1[4:13]
print(line2)















     
