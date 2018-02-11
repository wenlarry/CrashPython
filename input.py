# input() function with prompt

# Code 1
name = input("pls enter your name: ") 
print("Hi, " + name + "!")

# Code 2 
prompt = " If you tell us who you are, we can personalize the message"
prompt += "\nWhat's your name ? "

name = input(prompt)
print("\nHi, " + name + "!")

# Use int() for numerical input
age = input("How Old? ")

# Code 3
height = input("How tall ?, in cm? ")
height = int(height)

if height >= 36:
	print("\nYou are tall enough!")
else:
	print("\nYou'll be able to ride, when older")

# Modulo Operator

4 % 3
5 % 3
7 % 3

# Code = 4
number = input("Enter a number, and we tell you it's odd or even")
number = int(number)

if number % 2 == 0:
    print("\nThe number  " + str(number) + " is even")
else: 
	print("\nThe number " + str(number) + " is odd")

	
