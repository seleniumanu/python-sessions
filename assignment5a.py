"""7. Write a Python program to count the number of characters (character frequency) in a string.
Sample String :google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""

string="google.com"
for i in set(string):
    string1=string.count(i)
print(i,":", string1)

"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.
Sample String : 'ace2resource'
Expected Result : 'a2ce'
Sample String : 'a3'
Expected Result : 'a3w3'
Sample String : ' a'
Expected Result : Empty String"""

str='ace2resource'
str1=str[:2]+str[-2:] 
print(str1)  
str1= 'a3w3'
print(str1[0]+str1[-1])
str2='a'
if len(str2)<2:
    print("empty string")
else:
    print("not empty")

"""# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', 
except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'"""

line1='restart'
char=line1[0]
line1=line1.replace(char, '$')
line1=char+line1[1:]
print(line1)

"""#Write a Python program to get a single string from two given strings, 
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

s='abc'
s1='xyz'
s2=s1[:2]+s[2:]
s3=s[:2]+s1[2:]
print(s2, s3)



