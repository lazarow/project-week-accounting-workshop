# PYTHON BASICS WORKSHOP

# ---------------------------------------
# 🗒️ Hello Python & Variables
# ---------------------------------------

# Print statement
print("Hello, Python!")

# Variables
name = "Alice"
age = 25
height = 5.6

# Type checking
print(type(name), type(age), type(height))

# ➕ Exercise 1:
# Define your own name, age, and city, then print them.

# ---------------------------------------
# 🗒️ Data Types, Type Casting & Operators
# ---------------------------------------

# Arithmetic Operators
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Comparison Operators
print("x > y:", x > y)
print("x == y:", x == y)
print("x != y:", x != y)

# Logical Operators
print("x > 5 and y < 5:", x > 5 and y < 5)
print("x > 5 or y > 5:", x > 5 or y > 5)
print("not(x > 5):", not(x > 5))

# Type Casting
age = 25
text = " years old"

# This will cause an error:
# print("Age: " + age + text)

# Fix it with type casting:
print("Age: " + str(age) + text)

# Convert string to int
num_str = "100"
num = int(num_str)
print("Converted:", num + 50)

# ➕ Exercise 2:
# Create 2 numbers and print:
# - their sum
# - whether the first is greater
# - a sentence using both in a string (use str())

# ---------------------------------------
# 🗒️ Lists & Tuples
# ---------------------------------------

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("date")

colors = ("red", "green", "blue")

# ➕ Exercise 3:
# Create a list of your 3 favorite movies and print the second one.

# ---------------------------------------
# 🗒️ Dictionaries & Sets
# ---------------------------------------

# Dictionary
person = {"name": "Bob", "age": 30}
print(person["name"])

# Set (unique elements)
numbers = {1, 2, 3, 2}
print(numbers)

# ➕ Exercise 4:
# Create a dictionary with your name, age, and hobby.

# ---------------------------------------
# 🗒️ Conditions & Loops
# ---------------------------------------

# If statements
score = 85
if score > 90:
    print("A")
elif score > 75:
    print("B")
else:
    print("C")

# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1

# ➕ Exercise 5:
# Loop through numbers 1–5 and print "even" or "odd".

# ---------------------------------------
# 🗒️ Functions
# ---------------------------------------

# Function definition
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# ➕ Exercise 6:
# Write a function to calculate the square of a number.

# ---------------------------------------
# 🗒️ Input & Modules
# ---------------------------------------

# User input
name_input = input("Enter your name: ")
print("Hi", name_input)

import math
print("Square root of 16 is:", math.sqrt(16))

# ---------------------------------------
# 🗒️ Practical Tasks
# ---------------------------------------

# Try-except
# 1. 🎟️ Ticket Price Calculator
# Write a program that:
# - Asks the user for their age.
# - Calculates the ticket price (base price = 20 PLN).
# - Applies a 50% discount if under 18, or 30% discount if 65 or older.
# - Prints the final ticket price.
# Hint: Use the `int(input())` function to get the user's age.

# 2. ⚖️ BMI Calculator
# Write a program that:
# - Asks the user for their weight in kilograms and height in meters.
# - Calculates and prints their BMI using the formula: BMI = weight / height².
# - Rounds the result to 2 decimal places.
# Hint: Use the `round(bmi, 2)` function, where bmi is the result of the BMI calculation.
# Hint: Use the `float(input())` function to get the user's weight and height.

# 3. 💱 Currency Converter
# Write a program that:
# - Asks the user for an amount in euros (EUR).
# - Converts it to Polish złoty (PLN) using a fixed exchange rate (e.g., 1 EUR = 4.5 PLN).
# - Prints the result in PLN.
# Hints are the same as in the previous task.

# 4. 🛒 Shopping Total & Change
# Write a program that:
# - Asks the user for the price of two products.
# - Calculates the total cost.
# - Asks how much money was paid.
# - Calculates and displays the change to be returned.
# Hints are the same as in the previous task.

# 5. 💧 Daily Hydration Tracker
# Write a program that:
# - Asks the user how much water, juice, and coffee they drank today (in milliliters).
# - Calculates the total fluid intake.
# - Checks if the total is at least 2000 ml.
# - Displays a message based on whether the user is well hydrated or not.
# Hints are the same as in the previous task.
