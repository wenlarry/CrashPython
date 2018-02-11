# All the following codes require 'prompt'

# User choose when to quit

prompt = "\nTell me something, and I will repeat"
prompt += "\nEnter 'quit' to end "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Using break to exit Loop

# Calling break as sson as user enters 'quit'
prompt = "\nPl enter your loved city"
prompt += "\n(Enter 'quit' when done}"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to visit " + city.title() + "!")

# Using a flag

# For more complex programs where many different events can cause the program to stop
# Define one variable that determines whether or not the program is active
# The flag is 'active'.
# As long as the active variable remains True, the loop will continue running

prompt = "\nTell me something, and I will repeat"
prompt += "\nEnter 'quit' to end "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False  
	else:
		print(message)

# Filling a dict with User Input

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
	# Prompt for person's name and response
	name = input("\nWhat's your name ?")
	response = input("Which mountain would you like to climb ?")

	# Store the respnse in the dict
	response[name] = response

	# find out if anyone else is taking the poll
	repeat = input("would you like another person to respond ? (yes/no)")
	if repeat == 'no':
		polling_active = False

	# Polling is complete. Show Results
	print("\n--- Poll Results ---")
	for name , response in responses.items():
		print(name + "would like to climb " + response + ".")




