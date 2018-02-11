# While loop in action

current_number =1
while current_number <= 6:
    print(current_number) 
    current_number += 1

# Use continue in loop

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
	    continue

print(current_number)

# Avoiding Infinite Loop

x = 1
while  x <= 5:
	print(x)
	x += 1

# If (x += 1) is omitted the loop runs forever
# If stuck in infinite loop; press CTRL-C

# Moving Items from one list to another

# Start with users that need to be verified
# Creat an empty list for confirmed users
unconfirmed_users = ['al', 'br', 'ca']
confirmed_users = []

# Verify each user until no more unconfirmed users
# Move each verified user into list of confirmed users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

print("Verifying user: " + current_user.title())
    
confirmed_users.append(current_user) 

# Display all confirmed user
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


# Removing instances of specific values from list

pets =['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

	
