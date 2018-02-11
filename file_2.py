#  Reading an entire file

#  rstrip() method removes any white space char from tht
#     right side of the string

with open('file_1.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#  Reading line by line
#  Purpose os to examine each line

filename = 'file_1.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#  Large Files

#  If we have a txt file that contains pi to 1m decimals, we
#    can create a single string containing all these digits
#  We don't need to change the program except to pass it a 
#    different file. We can also print just the first 50 decimals/

#  Write 
#     filename = 'pi_m-digits.txt'
#     with open(filename) as file object:
#         lines = file_object.readlines()
#     
#      pi_string = ' '
#      for line in lines:
#          pi_string += line.strip()
#
#      print(pi, string[:52] + "...")
#      print(len(pi_string))
#
#  Is your birthday contained in Pi?
#
#  Write
#   filename = 'pi_m-digits.txt'
#     
#   with open(filename) as file object:
#       lines = file_object.readlines()
#     
#   pi_string = ' '
#   for line in lines:
#       pi_string += line.strip()
#
#   birthday = input("Enter in mmddyy:")
#   if birthday in pi string:
#       print("Your birthday appears in the first million digits of pi")
#   else:
#       print("Your birthday doesn't appear in the first million digits of pi")

