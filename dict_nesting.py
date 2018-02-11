#  Nesting - Store a set of dictionaries in a list or a list of 
#     items as a value in a dictionary. A power feature !

#  An empty list for storing aliens

#  At range() returns a set of numbers that teills Python how many
#      times we want the lop to repeat. Each time the loop runs we
#      create a new alien
#  Append each new alien to the list aliens
aliens = []

# 30 green aliens
for alien_no in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens created
print("Total no of aliens: " + str(len(aliens)))

#  code 2
#  use for loop and if statement to change color, etc
#  Modify first 3 aliens only
#  If statement to ensure that we're onlly modifying green aliens
aliens = []

for alien_no in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens [0:3]:
    if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10

#  show first five aliens
for alien in aliens[0:5]:
     print(alien)
print("...")

#  List in Dict

#  Begin with a dict that holds info about pizza ordered
#  One key in the dict is 'crust' and the associated value is
#    'thick'
#  Next key 'toppings' with its values
#  Summarize order
#  To print the toppings, we write a for loop 
#  To access the list of toppings , use the key 'toppings'
#  Python grabs the list of toppongs from the dict

# Info about ordered pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese'],
}
# Summarize
print("Ordered a  " + pizza['crust'] + "- crust pizza " +
    " with the following toppings:")

for topping in pizza['toppings']:
    print("\t"  + topping) 

# Code 2

#  Value associated with each name is now a list
#  Use the variable langs to hold each value from the dict
#    as each value is a list
#  Inside the main dict loop, we use another for loop to run
#    thru each person's list of fav_lang     
fav_lang ={
    'je':['python', 'r'],
    'sa':['c'],
    'ed':['r','go'],
    'ph':['python', 'ruby'],    
}
for name, langs in fav_lang.items():
    print("\n" + name.title() + "'s fav lang are:")
    for lang in langs:
        print("\t " + lang.title())

#  Dict in Dict

#  Define a dict called users with two keys: one each for the
#    user names. Value associated with each key is a dict.
#  Loop thru the users dict. Python stores each key in the 
#    variable username and the dict associated with each username
#     goes into the variable user_info.
#  Print the username
#  Accessing the inner dict. The variable user_info has 3 keys
#     ('first;, 'second', 'location')
#  Use each key to generate full name and location for each person
users = {
    ' aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location':'princeton',
        },
    'mcurie':{
         'first': 'marie',
         'last': 'curie',
         'location': 'paris',
         },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    




