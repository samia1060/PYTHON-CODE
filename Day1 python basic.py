
# DAY 01: PYTHON BASICS
# Topics: Variables, Data Types, Operators,
# Type Conversion, Input & Basic Practice



# 1. VARIABLES & DATA TYPES

name = "tonny khan"
age = 23
price = -25.55
age2 = age
old = True
tree = False
sale = None

print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(tree))
print(type(sale))


# 2. BASIC VARIABLE OPERATIONS

a = 500
b = 300

diff = a - b
print("Difference:", diff)


# 3. ARITHMETIC OPERATORS

a = 5
b = 3

print("Addition:", a + b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 4. RELATIONAL OPERATORS

a = 50
b = 20

print(a == b)
print(a != b)
print(a <= b)
print(a >= b)


# 5. ASSIGNMENT OPERATORS

num = 10
num **= 2

print("Num:", num)


# 6. LOGICAL OPERATORS

a = 50
b = 30

print(not False)
print(not (a > b))

val1 = True
val2 = False

print("AND Operator:", val1 and val2)
print("OR Operator:", val1 or val2)

print("AND Operator:", (a == b) and (a > b))


# 7. TYPE CONVERSION & CASTING

a = float("2")
b = 4.25

print(a + b)
print(type(a))

a = 3.15
a = str(a)

print(type(a))


# 8. USER INPUT

# name = input("Enter your name: ")
# print(name)


# 9. INPUT WITH DATA TYPES

"""
name = str(input("Enter name: "))
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print(type(name), name)
print(type(age), age)
print(type(marks), marks)
"""



# PRACTICE PROBLEMS


# PRACTICE 1
# Input 2 numbers and print their sum.

"""
a = int(input("Enter number 1: "))
b = float(input("Enter number 2: "))

print("Sum:", a + b)
"""


# PRACTICE 2
# Input the side of a square and print its area.

"""
side = float(input("Enter square side: "))

print("Area:", side * side)
"""


# PRACTICE 3
# Input 2 floating-point numbers and print their average.

"""
semester1 = float(input("Enter 1st CGPA: "))
semester2 = float(input("Enter 2nd CGPA: "))

print("Average CGPA:", (semester1 + semester2) / 2)
"""


# PRACTICE 4
# Input 2 integers, a and b.
# Print True if a is greater than or equal to b.
# Otherwise, print False.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(a >= b)
