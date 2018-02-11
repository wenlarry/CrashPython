
#  Checking for special items

toppings = ['mushrooms', 'peppers', 'cheese']

for topping in toppings:
    if topping == 'peppers':
        print("Sorry, no peppers now!")
    else:
        print("Add  " + topping + ".")

print("\nPizza Ready!")


#  Checking that list is not empty

#  Quick Check
#  When the name of a list is used in an if statement,
#    Python returns True if the list is contains at 
#     least one item; an empty list evaluates to False
#  If the conditional test fails, we print a message
#     "a plain pizza ?"
toppings = []

if toppings:
    for topping in toppings:
        print("Add "+ topping +".")
    print("\n Pizza Ready!")
else:
    print("A plain pizza?")


# Multiple Lists

#  Note unusual reuest 'fries'
#  loop thru the list of requested toppings and check
#    whether if each requested topping is in the list of
#    basic toppings
#  If it is, we add that topping
#  If not, the else block will run
basic_toppings = ['mushrooms', 'peppers', 'pepperoni', 'cheese', ]
requested_toppings = ['fries', 'mushrooms', 'cheese']

for requested_topping in requested_toppings:
    if requested_topping in basic_toppings:
        print("Add " + requested_topping + ".")
    else:
        print("Sorry, NO " + requested_topping + ".")

print("\n Pizza Ready!")





