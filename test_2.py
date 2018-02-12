#  Testing a function

#  Testing that formatted_name() in test_1.py works
#  this is a program that uses the function in test_1.py
from test_1 import get_formatted_name

print("Enter 'q' to quit")
while True:
    first = input("\nPls give first name:")
    if first =='q':
       break
    last = input("Pls give last name:")
    if last =='q':
        break 
formatted_name = get_formatted_name(first, last)
print("\tNeat formatted name: " + formatted_name + '.')

