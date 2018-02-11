#  Using multiple elif blocks

age = 12

if age <4:
	price = 0
elif age < 18:
	price = 4
elif age < 65:
	price = 8
else:
	price = 4

print("Admission is $" + str(price) + ".") 

# Testing multiple conditions

toppings = ['mushrooms', 'cheese']

if 'mushrooms' in toppings:
	print("Add mushrooms!")
if 'pepperoni' in toppings:
	print("Add pepperoni!")
if 'cheese' in toppings:
	print("Add cheese!")

print("\n Pizza Done !")

# Testing multiple conditions(one test passes)

#  This code would not work properly if we used an 
#    if-wlif-else block beacuse the code stops after
#    one test passes
toppings = ['mushrooms', 'cheese']

if 'mushrooms' in toppings:
	print("Add mushrooms!")
elif 'pepperoni' in toppings:
	print("Add pepperoni!")
elif 'cheese' in toppings:
	print("Add cheese!")

print("\n Pizza Done !")

# If we want only one block of code to run, use an
#   if-elif-else chain. If more than one block of
#   code  to run, use a series of if statements

	