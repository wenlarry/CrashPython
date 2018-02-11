#  Exceptions

#  Python uses objects 'exceptions' to manage errors that arise during a program's
#    execution
#  Exceptions are handled with try-except blocks. A try-except block ask Python to
#     do something, but it also tell Python what to do if an exception is raised
#  When we use try-except blocks, the programs will continue. Instead of tracebacks.
#     we get friendly error messages

#  Error - getting a traceback
#  print(5/0) 

#  Using try-except blocks
try:
	print(5/0)
except ZeroDivisionError:
	print("Can't divide by zero")

#  Using exceptions to prevent crashes

#  Happens often in programs prompting users' inputs
#  Programs respond to invalid inputs by prompting for more valid inputs than crashing
#  This program does nothing to handle errors...it crashes

#print("Give two numbers for division")
#print("Enter 'q' to quit")

#while True:
    #first_number = input("\nFirst Num:")
    #if first_number =='q':
    	#break
    #second_number = input("Second Num:")
    #if second_number =='q':
    	#break
   # answer = int(first_number) / int(second_number)
   # print(answer)

#  The else block

#  Making the block more error resistant by wrapping the line that may produce errors in
#     a try-except block. Any code that depends on the try block executing successfully
#     goes into the else block
#  Print a friendly statement
#  In anticipating likely errors, we can write robust programs even when we encounter 
#     invalid data
print("Give two numbers for division")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Num:")
    if first_number =='q':
    	break
    second_number = input("Second Num:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        print(answer)

	



