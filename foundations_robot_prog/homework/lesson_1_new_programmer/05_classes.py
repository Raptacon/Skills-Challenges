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

# We'll make a mechanism class with a constructor (__init__) method
# that takes current position angle (in degrees) for the robot. Set the mechanism's
# current position by setting the object's current position attribute to be
# the given current position argument value (replace the first "None" to do this).
# Also, replace the second "None" to set the mechanism's starting speed to 0.

# Now, we'll make a new method within the class to rotate the mechanism to the goal
# position. This method takes the goal position (in degrees) and the movement speed
# (in degrees per second) as arguments, along with the seconds to try moving set
# with a default value.

# To implment the movement logic within the loop, update the mechanism's speed
# to be the given movement speed by replacing the third "None" with the\
# speed argument value. Update the mechanism's current position angle by setting
# its current position attribute to be itself plus the mechanism's speed attribute.
# You'll need to use the "self." syntax for both of these.

# Now, determine if the arm has reached the goal position by comparing the
# current position angle attribute to the given goal position angle argument using "<"
# operator. If we reach the goal position, we'll tell Python to stop moving the mech.
# After the loop completes, set the mechanism's speed to 0 by replacing the last "None"
# - we don't want to break it!

# We won't return anything here because we actively updated the position attribute
# within the class itself - classes combine data with logic.

# To confirm tjhe class works, replace the "0" within "Mechanism" with
# the current position of 37.5 degrees. Then, replace the next two 0s with 
# a goal position of 12.5 degrees and a movement speed of -15 degrees per second,
# in that order. Note how we access the mechamism's data attributes in the
# print statements

# If playing around with this, ensure current position is greater than goal
# position and speed is a negative value.

print("--Your Code: Classes--")


class Mechanism():
    def __init__(self, mech_current_position_angle):
        self.mech_current_position_angle = None
        self.mech_speed = None

    def rotate_mechanism(
        self,
        mech_goal_position_angle,
        mech_move_speed,
        seconds_to_try_moving=20
    ):
        # "range" is a special Python function that generates a sequence of
        # integers up to the given integer
        for second in range(seconds_to_try_moving):
            self.mech_speed = None
            self.mech_current_position_angle = None
            mech_reached_goal_position = None

            if mech_reached_goal_position:
                # "break" is a special keyword that tells Python to stop looping
                break

        self.mech_speed = None


arm_mechamism = Mechanism(0)
arm_mechamism.rotate_mechanism(0, 0)

print(arm_mechamism.mech_current_position_angle)
print(arm_mechamism.mech_speed)

print("-----------------")

# ***
