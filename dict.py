# Python; dict is a collection key-value pairs
# Each key is connected to a value

# Simple dict

alien_0 = { 'color': 'green', 'points': 6}

print(alien_0['color'])
print(alien_0['points'])

# Dict stores alien's color and point

# Accessing values

alien_o = {'color': 'green', 'points':6}

new_points = alien_o['points']
print("Earned " + str(new_points) + " points!")

# Once the dict has been defined, the code'new_points'  pulls 
#  the value associated with the key 'points'. this value is then stored 
#  in the variable 'new_points'

# Add new key-value pairs

# Add a new key-value pair: key 'x_post' and value 0
alien_o = {'color': 'green', 'points':6}
print(alien_o)

alien_o['x_post'] = 0
alien_o['y_post'] = 26
print(alien_o) 


#  Modifying values

#  Change the value associated with the key 'color' to 'red'
# code 1
alien_o = {'color': 'green', 'points':6}
print("Alien is  " +  alien_o['color'] + ".")

alien_o['color'] = 'red'
print("Alien is now " + alien_o['color'] + ".")

#  Code 2
#  An if-elif-else chain determines how far the alien should move
#    to the right and stores the value in the variable 'x_inc'
#  If the alien's speed is 'medium', it moves two units to the right, etc.
#  As this is a medium speed alien, its position shifts two units to the right
alien_o = {'x_pos': 0, 'y_pos': 26, 'speed': 'med'}
print("Original x_post: " + str(alien_o['x_pos']))

if alien_o['speed'] =='slow':
    x_inc = 1
elif alien_o['speed'] == 'med':
    x_inc = 2
else:
    x_inc = 3

alien_o['x_pos'] = alien_o['x_pos'] + x_inc

print("New position: " + str(alien_o['x_pos']))

# Remove key-value pairs

# The 'del' line deletes the key 'points'
alien_o = {'color': 'green', 'points':6}
print(alien_o)

del alien_o['points']
print(alien_o)

#  Dict - Similar Objects

#  Store one kind of info abour many object
#  Each key is name and each value is language choice
#  Indent the next line one level i.e 4 spaces
#  Write the first key-value pair, followed by a comma
fav_lang = {
	'je': 'python',
	'sa':  'c',
	'ed':  'ruby',
	'ph':  'python',
}

#  For break up of a long print statement
#  Choose an appropriate point to break
#  Add a concatenation operator (+) at end of first line
#  Press ENTER and then TAB to align all subsequent lines
#  Closing parentesis on the last line of the block
print ("Sa's fav lang is  " + 
    fav_lang['sa'].title() +
    ".")

    



