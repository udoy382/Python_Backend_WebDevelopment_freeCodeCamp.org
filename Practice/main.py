# Hello World in Python :

"""
print("Hello World!")
print('Hello World! 2')
print("Udoy is 18")
print("Saifur Rahman Udoy", 436)
"""

# Variables in Python :

"""
name = 'Udoy'
age = 18

print(name)
print(age)

print(name + " is a good boy")
print(name + ' is', age)
print(name, 'is', age)
"""

# Strings in Python :

'''
name = "Udoy"
name2 = 'Saifur Rahman Udoy'
name3 = """
This is another string
this is multiline string or comment
"""

print("Hi,\nHow are you")

print(name)
# print(name[0])
# print(name.upper())
# print(name.lower())
# print(name.islower())
# print(name.isupper())
# print(len(name))
# print(name.index("o"))
# print(name.replace("o", "0"))

# print(name2)
# print(name3)
'''

# Numbers in Python :

"""
number = 20
number2 = 30


print(number)
print(number + number2)

cng = str(number)

print(436)
print(22 + 99)
print(5 + 2.22)
print(5 - 2)
print(10 * 5)
print(100 / 10)
print(20 % 6)

# print(20 + cng) #This is showes an error ~

print(abs(-5))
print(max(4, 2))
print(min(22, 21, 34, 12))
print(round(3.5))
print(bin(324))

from math import *

print(sqrt(100))
"""

# Getting User's Input :

"""
name = input("Input Your Name : ")
age = int(input("Input Your Age : "))

# print("Your name is " + name + " and your are " + age + " years old") #before creating age to integer
print("Your name is " + name + " and your are ", age, " years old")
"""

# Word Replacement Exercises :

"""
sentence = input("Enter your sentence : ")
print("Your sentence is : " + sentence)

word1 = input("Enter the word to replace : ")
word2 = input("Enter the word to replace it with : ")

print(sentence.replace(word1, word2))
"""

# List in Python :

"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
country = ["united States of America", "Ghana", "Bangladesh", "Pakistan", "New Zealand"]
make_list = list(("Udoy", "Sara", "Mariyam", "Nawal Khan"))

name = "Udoy"
number = 436

print(list1)
print(country)
print(make_list)

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print(list1[6])
print(list1[7])
print(list1[8])
print(list1[9])

print(country[0])
print(country[1])
print(country[2])

# print(country[2:])
# print(country[1:4])
# print(country[-2])

# country[0] = 'United Kingdom'
# country[4] = 'canada'
# print(country)

# print(type(country))
# print(type(name))
# print(type(number))
# print(type(make_list))

# print(len(country))
# print(len(list1))
"""

# List Methods :

"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 3, 4]
list2 = ['banana', 'apple', 'orange', 'mango', 'cheese', 'papaya']
list3 = list2.copy()

# list1.extend(list2)
# list2.append("cherry")
# list2.insert(1, 'cheese')
# list2.remove("orange")
# list2.clear()
# list1.sort()
# list2.sort()
# list2.reverse()
# list2.pop()
# list2.pop(1)
# list2.remove('banana')
# del list2[0]
# del list2 // This shows an error caused we deleted the variable than we printed it

print(list1)
print(list2)
# print(list2.index('papaya'))
# print(list2.count('cheese'))
print(list3)
"""

# Tuples in Python :

"""
three_numbers = (1, 2, 3, 1)
strings = ('home', 'land', 'earth')
boo = (True, False, True)
all_types = (11, "Hello", True, 3.3)
all_types2 = tuple((11, "Hello", True, 3.3))

print(three_numbers)
print(strings)
print(boo)
print(all_types)
print(all_types2)

print(three_numbers[0])
# three_numbers[1] = 23
# print(three_numbers)

print(len(three_numbers))
print(type(three_numbers))
print(type(all_types2))
print(type(three_numbers[2]))
"""

# Function in Python :

"""
def greetings_function(name, age):
    print("Welcome " + name + ". Your age " + str(age) + " years old")
    # print("Welcome " + str(name))

    # print('Welcome ' + names[0])

# greetings_function("Udoy", 18)
# greetings_function("Udoy", "Sara")
# greetings_function(name = "Udoy", age = 18)

name = input("Enter your name: ")
age = input("Enter your age: ")

greetings_function(name, age)
"""

# The Return Keyword in Python :

"""
def add_numbers(num1, num2):
    print("Hello, world!")
    return num1 + num2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# print(add_numbers(2, 3))
print(add_numbers(num1, num2))
"""


# IF Statements in Python :

"""
a = 4
b = 3
c = "Udoy"
d = "Sara"
e = True

boy = True
girl = True

value = int(input("Enter a value: "))

if a > b:
    print(f"{a} is greater than {b}")


if c == d:
    print("C is equal to D")
else:
    print("C is not equal to D")


if e == True:
    print("E is True")
elif e == False:
    print("E is False")
else:
    print("A is none of the two")


if boy == True or girl == False:
    print("OR")
else:
    print("Not OR")


if boy == True and girl == False:
    print("AND")
else:
    print("Not AND")


if type(value) = str:
    print(value, " is a string")
else:
    print(value, " is not a string")
"""

# Building An Even Number Checker Program : 

"""
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
"""

# Dictionaries in Python : 

"""
my_dict = {
    'name': 'Udoy',
    'age': 18,
    'is_tall': False,
    'nationality': 'Bangladeshi',
    'qulification': 'College',
    'friends': ['Hamim', 'Mahi', 'Raihan', 'Nabil', 'Nadim', 'Moinul']
}

x = my_dict['name']
print(x)

print(my_dict)
print(len(my_dict))
print(my_dict['name'])
print(my_dict['is_tall'])
print(my_dict['friends'])
print(type(my_dict))
"""

# While Loops in Python :

"""
i = 1
while i < 6 or i == 6:
    print(i)
    i += 1

i = 1
while i < 10:
    print(i + 1)
    i += 1
"""

# For Loops in Python :

"""
myList = ['ji', 'ju', 'jo']

myDict = {
    'name': 'Udoy',
    'age': 18,
    'is_tall': False,
    'nationality': 'Bangladeshi',
    'qulification': 'College',
    'friends': ['Hamim', 'Mahi', 'Raihan', 'Nabil', 'Nadim', 'Moinul']
}

# for letter in 'Hello':
#     print(letter)


# for values in myList:
#     if values == 'ju':
#         break
#     print(values)

# for values in myDict:
#     print(values)


for x in range(14):
    print(x)

else:
    print("Finished Looping!")
"""

# 2D Lists and Nested Loops in Python : 

"""
my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(my_list)
print(type(my_list))
print(my_list[0])
print(my_list[0][1])
print(my_list[1])
print(my_list[1][2])
print(my_list[2])


for lists in my_list:
    for row in lists:
        print(row)
    print(my_list)
"""


# Comments in Python :

"""
# print("Hello")
print("This is for simple print!")

# This is a single line comment

'''
Or This is a multi 
line 
comment
'''
"""

# Building A Basic Calculator : 

"""
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter operator: ')


if op == '+':
    print(f'The addition is {num1 + num2}')
elif op == '-':
    print(f'The subtraction is {num1 - num2}')
elif op == '*':
    print(f'The multiplication is {num1 * num2}')
elif op == '/':
    print(f'The division is {num1 / num2}')
else:
    print('Invalid operator')
"""

# Try Except in Python : 

"""
try:
    x = int(input('Input an integer: '))
    print(x)
# except:
#     print('Value not an integer')

except ValueError:
    print('Value not an integer')
else:
    print('Nothing went wrong')
finally:
    print('Try except finished')
"""

# Reading Files : 

"""
coun_file = open ('Practice/countries.txt', 'r')

# print(coun_file.readable())
# print(coun_file.readlines())
# print(coun_file.read())

# print(coun_file.readline())
# print(coun_file.readline())
# print(coun_file.readline())

# print(coun_file.readlines()[2])

for files in coun_file.readlines():
    print(files)

coun_file.close()
"""

# Writing Files : 
"""
'''
# coun_file = open ('Practice/countries.txt', 'w')
coun_file = open ('Practice/countries.txt', 'a')

coun_file.write('\nThis is a new line')

coun_file.close()
'''
'''
coun_file = open ('Practice/test.py', 'w')

coun_file.write('print(\'This is a new line\')')

coun_file.close()
'''
"""

# Classes And Objects in Python : 

"""
'''
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# name = input('Enter your name: ')
# age = input('Enter your age: ')

# p1 = Person('Udoy', 18)
# p1 = Person(name, age)
p1 = Person('Sara', 15)


print(p1.name)
print(p1.age)

# del p1
# print(p1)
"""

# Inheritance in Python : 

"""
from inheritance import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)
"""

# Python Shell : 


# Building A simple Login and SignUp System : 
"""
print('Create account now')
username = input("Enter your username: ")
password = input("Enter your password: ")

print("Your account has been created successfully")
print("Login Now!")

username2 = input("Enter your username: ")
password2 = input("Enter your password: ")

if username == username2 and password == password2:
    print('Logged in successfully')
else:
    print('Invalid credentials')
"""

# `Module` & `pip` in Python :

import modules

modules.say_hi()