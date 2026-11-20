#DAY1 PRACTICE
""""
Problem 1: Personal Information
Write a Python program that stores and displays your personal information.

Requirements:
- Store your name, age, university name, and department in variables.
- Use appropriate data types.
- Display each piece of information on a separate line.
"""



"""
name=str("Samia")
age=int(23)
universityname=str("AIUB")
department=str("cs")

print("name: ",name)

print("age: ",age)

print("universityname: ",universityname)

print("department: ",department)

"""



"""
Problem 2: Shopping Bill Calculator
You went shopping and bought:
- 2 shirts, each costing 850 BDT.
- 1 pair of shoes costing 2,500 BDT.
Write a program to calculate and display the total shopping cost.
"""

"""
shirt=850
shoes=2500
total_cost=2*shirt+shoes


print("total Shopping Cost : ",total_cost,"BDT" )
"""



"""
Problem 3: Student Grade Calculator
A student received the following marks:
- Mathematics: 85
- English: 78
- Computer Science: 92
Write a program to:
1. Store the marks in variables.
2. Calculate the total marks.
3. Calculate the average marks.
4. Display both results.
"""
"""
Mathematics=85
English=78
Computer_Science=92

total_marks=Mathematics+English+Computer_Science
average_marks=total_marks/3
print("total marks: ",total_marks)
print("average marks: ",average_marks)
"""




"""

Problem 4: Temperature Converter
Write a program that converts temperature from Celsius to Fahrenheit.

Formula:
\[
F = (C \times 9/5) + 32
\]

Use 35°C as your input value.
"""
"""
celsius=35
fahrenheit=celsius* 9/5+32

print("Celsius temperature : ",celsius,"°C")
print("fahrenheit temperature : ",fahrenheit,"F")
"""


"""
Problem 5: Online Shopping Discount
A customer purchases a product worth 5,000 BDT.

The shop offers a 15% discount.

Write a program to calculate:
1. Original price.
2. Discount amount.
3. Final price after discount.
"""
"""
product_price=5000
discount_price=15
original_price=5000
discount_amount=product_price*discount_price/100
final_price=original_price-discount_amount

print("original price :",original_price)
print("discount price :",discount_amount-)
print("final price :",final_price)
"""



"""
Problem 10: Mobile Recharge Calculator
A customer recharges their mobile account.

Ask the user to enter the recharge amount.

Calculate:
- The recharge amount.
- A 5% bonus amount.
- The final balance after adding the bonus.
"""

recharge_amount = float(input("Enter recharge amount: "))

bonus_amount = recharge_amount * 5 / 100

final_balance = recharge_amount + bonus_amount

print("Recharge Amount:", recharge_amount)
print("Bonus Amount:", bonus_amount)
print("Final Balance:", final_balance)
#practice file updated