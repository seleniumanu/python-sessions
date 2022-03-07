#write a Python program to print the following string in a specific format.
	What is Python?
		Python is .....
	What is the Usage of Python?
		It is used ....   

print("What is Python?\n    it's a programing language\nWhat is the Usage of Python?\n    it is used for web,app development,data science")

# Write a Python program to get the Python version you are using
import sys
print("python version", sys.version)

#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name=input("enter first name:")
last_name=input("enter last name:")
print(last_name + " " + first_name)
first_name="anuradha" [::-1]
print(first_name)

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

list=input("enter numbers")
list1=list.split(" ")
tuple=tuple(list1)
print(list1)
print(tuple)

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n=int(input("enter n value:"))
temp=int("%s" % n)
temp1=int("%s%s" % (n,n))
temp2=int("%s%s%s" % (n,n,n))
print(temp+temp1+temp2)

#Write a Python program to calculate the length of a string.

str=(input("enter the string:"))
count=0
for s in str:
	count=count+1
print(count)
print(len(str))
