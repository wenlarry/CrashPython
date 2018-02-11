#  Storing Data

#  JSON module allows dumping of simple Python data structures
#     into a file and load the data from that file the next time
#     the program runs
#  json.dump() function takes a piece of data to store and a file
#     object it can use to store the data
import json

numbers = [2,3,5,7,11]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

print(numbers)

#  Write a program that uses json.load() to read the list back into
#     memory
import json

filename+ 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)

#  Saving and Reading User generated data
import json

username = input("What's your name ?")

filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)
	print ("We'll remember you always " + username + "!")

#  Greet  user whose name has been stored
import json

filename = 'username.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back " + username + "!")

#  Combining two programs. When someone runs this code, we want to retrieve
#    username from memory, if possible. We start with a try block to recover
#    username. If the file username.json doesn't exist, we've the except
#    block prompt for a username and store it in username.json for next time
import json

#  Load the username if it has been stored before
#  Otherwise, prompt for the username and store it
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What's your name ?")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you always " + username + "!")
else:
	print("Welcome back " + username + "!")

