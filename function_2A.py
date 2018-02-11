# Passing a List

#  List of names stored in parameter names
#  Function loops thru list and prints a greeting to each user
#  Define a list of users and then pass the list usernames to greet_users in function call
def greet_users(names):
    """Print a greeting to each user in list"""
    for name in names:
        msg = "Hi, " + name.title() + "!"
        print(msg)

usernames = ['t', 'd', 'h']
greet_users(usernames)

#  Modifying List in function

#  Any changes made to a list inside the function's body are permanent
#  Two functions. First function handle printing the designs. Second function summarize 
#     the prints
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design and then move each design to completed_models after
    printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simulate creating a 3D print from design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models printed"""
    print("\nThe following models printed")
    for completed_model in completed_models:
    	print(completed_model)
 #  Set up a list of unprinted designs and an empty list that hold the completed models
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
#  Call the print_models() and pass it the two lists
#  Call show_completed models () and pass it the list of completed models
#  If we need to print more designs later, we can simply call print_models()
#  if we realize that the printing code needs to be modified , we change the code once
#     and our changes will will take place everywhere the function is called
#  Code demonstrates that every function should have a specific job 
#  If the function is doing too many tasks, split the code into two functions
print_models( unprinted_designs, completed_models)
show_completed_models(completed_models)

#  Preventing a function from Modifying a List

#  As in the previous example, if we want to keep the original list of unprinted designs
#     then pass to the function a copy of the list.
#  The slice [:] makes a copy of the list to send to the function like this:
#     'function_name(list_name[:])'
#  If we do not want to to empty the list of unprinted designs, we call print_models() as:
print_models(unprinted_designs[:], completed_models)
   	