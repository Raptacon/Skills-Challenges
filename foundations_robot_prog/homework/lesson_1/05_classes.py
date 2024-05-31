########################################
# CLASSES
########################################

# Classes are the foundation of much modern programming, and
# robot programming is no exception. In a nutshell, classes
# bring data elements and code logic together into one structure.
# They allow us to track the state of some part of our program and
# modify it directly. They also allow us to readily extend code.

print("--Example: Classes--")

# The "class" keyword creates the class
class GrowingNumber():
    # Here, these "def" keywords create methods. Methods are similar
    # to functions, except they are called directly from an object
    # created using this class and can access and modify class data.
    # Methods can also take arguments

    # The __init__ special method is the constructor of the class. Every time a
    # new object is created using this class, the code in this method will
    # be executed.

    # The first "argument" to a typical method is "self." self allows us
    # to access the data and other methods within the class. When calling
    # these methods, we do not pass any data elements for self - in effect,
    # the __init__ method below has zero real arguments
    def __init__(self):
        # self.growing_number is an attribute of this class. It behaves
        # similarly to a typical variable
        self.growing_number = 1
    
    def grow_number(self, growth_rate, end_threshold):
        """
        We can provide docstrings here too
        """
        # Now, instead of making growing_number a variable, we make
        # it an attribute and save it within our class
        while self.growing_number < end_threshold:
            self.growing_number = self.growing_number * growth_rate

    def reset_number(self):
        # We can set the number back to its starting value with a
        # specific method. Note that the constructor method is only
        # called once
        self.growing_number = 1

# growing_number is now an object of custom type GrowingNumber
# When we create this object, the code in the __init__ method runs
growing_number = GrowingNumber()
print(growing_number.growing_number)
# By calling this method, the data within growing_number will be updated.
# This data can be accessed from the object using dot syntax
growing_number.grow_number(2, 5)
print(growing_number.growing_number)
# We can update the data multiple times
growing_number.grow_number(3, 60)
print(growing_number.growing_number)
# We can reset the number to start from square one
growing_number.reset_number()
print(growing_number.growing_number)
growing_number.grow_number(4, 100)
print(growing_number.growing_number)

print("-----------------")

# ***
# FOR YOU: let's wrap up this homework by converting our mechanism rotation
# code into a class.

# Create a mechanism class. Give it an __init__ method with an argument
# for the current postion (also - don't forget the self!).
# Make an attribute within the class for the current position, and set it
# equal to the argument value

# Now, create a new method within the class to rotate the mechanism to the goal
# position. Let this method take the goal position (in degrees) and the speed
# (in degrees per second) as arguments. Here, use a while loop to continually
# add the speed to the current position attribute until the current position
# falls below the goal position. 

# To confirm your class works, create a new object using the class and
# store it in a variable. When creating this object, pass it 37.5 as the current
# position value - this will look like Mechanism(37.5).
# Call your rotation method using the following arguments
# goal position: 25; speed: -5.5
# Then, print out the value of the current position attribute within the object.
# After that, call the rotation method again with the following arguments
# goal position: 12.5; speed: -2.5
# and print the new current position

# If playing around with this, ensure current position is greater than goal
# position and speed is a negative value. Otherwise, the code will run forever
# until you terminate the program.

# Note: you can force a Python program to stop running by pressing Ctrl+C
# in your terminal. You can force close the whole terminal by pressing the
# trash icon

print("--Your Code: Classes--")
# <your code here>
print("-----------------")

# ***
