#  Classes are foundations of object-oriented programming
#  They represent real world things that we model eg cars
#  Use a class to make objects, that are instances of dogs
#  A class defines the behavior of a whole category objects
#  Classes can inherit from each other i.e.write a class that
#   extends the functionality of an existing class

#  Creating and using a class

#  Information on the dog is stored in attributes (i.e var) and 
#     the behavior is represented by functions
#  Functions part of a class are methods

#  The self parameter is required in the method definition and 
#     must come first before other parameters. It must be included
#     in the definition because when Python calls this _init_()
#     method , the method will automatically pass the self arg
#  When we make an instance of Dog, Python will call the _init-_ ()
#     method from the Dog class. We pass Dog(), a name and age as
#     args; self is passed automatically

#   Any var prefixed with self is available as to every method in the
#      class and we also will be able to access these var thru any 
#      instance created from the class. Var that are accessible thru
#      instances  are attributes
class Dog ():
    """Model a dog"""
    def __init__ (self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age 

    def sit(self):
        """ Simulate sitting"""
        print(self.name.title() + " is sitting")

    def roll_over(self):
    	"""Simulate rolling over"""
    	print(self.name.title() + "rolled over")

#  Making an Instance from a Class

my_dog = Dog('z', 4) 

#  Accessing Attributes

#  Access the attributes of an instance by writing 'my_dog.name'

print("My dog's name is  " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years")

#  Calling Methods 

#  After an instance is created from the class Dog, we can use the
#     dot notation to call any method defined in Dog

my_dog.sit()
my_dog.roll_over()

#  Creating multiple Instances

my_dog = Dog('zeus', 4)
your_dog = Dog('a', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str (my_dog.age) + " years")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print(" Your dog is " + str(your_dog.age) + " years ")
your_dog.sit()










