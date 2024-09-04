########################################
# INTRO TO PYTHON HOMEWORK:
# PYTHON BASICS
########################################

# Hello! In this homework, we will walk you through the basics
# of the Python programming language.

# To start, we'll go over basic data types and declaring variables.

# Look for "FOR YOU" and <your code here> as you go through the script -
# this signals that you need to do something. The *** will bound the area
# where you should looks for places to write code

# You can run this code in your terminal by changing your working directory
# to the folder containing this script and then running the following:
# python lesson_1.py

# A more thorough intro to Python can be found at
# https://python101.pythonlibrary.org/part_i.html

########################################
# VARIABLE DECLARATION & DATA TYPES
########################################

# Variables are things that we track and work with in Python
# For example, say we want to count the number of times we lift up
# a robot arm. To do this, we need to create a counter variable.
# We'll update this variable each time the robot arm moves up.

# Variables are created using the synatx <variable name> = <variable value>,
# like with

counter = 0

# Now that the counter variable is created, we can work with it in Python.
# The print() function comes with Python and lets us see the value of a variable.

print("--Example: Variable Declaration--")
print(counter)
print("-----------------")

# ***
# FOR YOU: let's say we have four motors, and we want to be able to reference
# this in our code. Can you declare a "motor quantity" variable and print it?

print("--Your Code: Variable Declaration--")
motor_quantity = 4
print(motor_quantity)
print("-----------------")

# ***

# Now, let's discuss different data types that variables can have.
# Python is a "dynamically typed" language, meaning that you don't
# need to explicitly say what the type of a variable is - Python
# will infer the type based on the value you pass it. Any value can
# be passed to any variable, so the type of a variable can change at will.
# This is very freeing, but with this freedom can come trouble.

# Let's go through a handful of common data types we will work with:

# - Booleans (True; False) track whether something is true or false.
# We commonly work with Booleans when comparing two variables to one
# another and when using "if" statements. For example:

print("--Example: Booleans--")
# Check for equality
print(counter == 0)
# Check for value greater than
print(counter > 1)
# Check for value less than and flip the value
print(not (counter < 1))
print("-----------------")

# ***
# FOR YOU: can you check if you have four motors? How about more than 6?

print("--Your Code: Booleans--")
print(motor_quantity == 4)
print(motor_quantity > 6)
print("-----------------")

# ***

# - Integers (4; 0; -3) are whole numbers. We commonly use these for
# count quantities and identification numbers
# We can use common mathematical operators to update integers:
# "+" is addition
# "-" is subtraction
# "*" is multiplication
# "/" is division

print("--Example: Integers--")
counter = counter + 1
print(counter)
print(counter - 2)
print(counter * 3)
print("-----------------")

# ***
# FOR YOU: suppose we originally build two robots, and we later build
# four more. Can you create a variable for the number of robots we have,
# starting with two, and then modify the variable by adding the
# four new robots to it? Use print statements to see how the variable changes.

print("--Your Code: Integers Part 1--")
num_robots = 2
print(num_robots)
num_robots = num_robots + 4
print(num_robots)
print("-----------------")

# Now say we want to give our robots away to other teams, two per team. Can you
# calculate how many teams we can give these robots to?

print("--Your Code: Integers Part 2--")
teams_getting_robots = num_robots / 2
print(teams_getting_robots)
print("-----------------")

# ***

# - Floats (5.6; 0.0; -3.14) are decimal numbers. We often use these
# to track physical values, like the number of feet a robot has travelled
# The same mathematical operators we used with integers can be used with floats.

print("--Example: Floats--")
print(5.5 + 3.5)
print(70 / 30)
print("-----------------")

# ***
# FOR YOU: suppose a robot arm sits 12.5 degrees above horizontal as its
# starting position, can you create a new variable for this?
# Then, suppose we want a set point for the arm that is three times this starting
# angle, can you calculate this angle and store it in a new variable?

print("--Your Code: Floats--")
starting_position = 12.5
setpoint_position = starting_position * 3
print(setpoint_position)
print("-----------------")

# ***

# - Strings ("Hello World"; '00454112') are alphanumeric characters. We
# often use these to print messages, provide names, and classify things

print("--Example: Strings--")
my_robot_name = "Green Bot"
print(my_robot_name)
print("-----------------")

# ***
# FOR YOU: can you print what you're most looking forward to learning
# in this robotics workshop?

print("--Your Code: Strings--")
print("I'm looking forward to making robots dance!")
print("-----------------")

# ***

# Lists ([1, 2, 3]; ["a", "b", "c"]; [10, 10.123, "11"])
# let us store and iterate over multiple data elements.
# Any data element in a list can be of any data type, including
# another list! Data elements can be freely added or removed
# from lists

print("--Example: Lists--")
my_robots = ["Breadbox", "Green Bot"]
print(my_robots)
my_variables = [counter, my_robot_name, my_robots]
print(my_variables)
# Access the first element (index 0)
print(my_robots[0])
# Access the third element (index 2)
print(my_variables[2])
print("-----------------")

# ***
# FOR YOU: can you put all of the variables you have made into a list?
# Can you print the second element (index 1) of it?

print("--Your Code: Lists--")
my_variables = [
    motor_quantity, num_robots, teams_getting_robots,
    starting_position, setpoint_position
]
print(my_variables)
print(my_variables[1])
print("-----------------")

# ***

# Dictionaries ({1: "a", "b": 2}) let us map values to keys for quick,
# iterable access. Keys need to be data elements of a specific set of
# types (mostly we use integers and strings for keys). Values can be data
# elements of any type, including another dictionary! 

print("--Example: Dictionaries--")
my_variables_dict = {
    1: my_variables,
    2: counter,
    "my_robot_name": my_robot_name,
    "my_robots": my_robots
}
print(my_variables_dict)
# Accessing the value mapped to key 2
print(my_variables_dict[2])
# Accessing the value mapped to key "my_robot_name"
print(my_variables_dict["my_robot_name"])
print("-----------------")

# ***
# FOR YOU: can you put all of the variables you have made into a dicionary,
# using integers as keys? Can you print the value mapped to key 1?

print("--Your Code: Dictionaries--")
my_variables_dict = {
    1: motor_quantity,
    2: num_robots,
    3: teams_getting_robots,
    4: starting_position,
    5: setpoint_position
}
print(my_variables_dict)
print(my_variables_dict[1])
print("-----------------")

# ***

########################################
# CONDITIONAL CONTROL FLOW: IF-ELSE
########################################

# If-else blocks let us execute certain parts of code
# based on Boolean variables and data elements

# Python requires programmers to use indents to signify
# that lines of code are part of the same block

print("--Example: Basic If-Else--")
i_am_a_robot = True
if i_am_a_robot:
    # This code will only execute if the Boolean "i_am_a_robot" is True
    print("I'm a robot!")
else:
    # This code will only execute if the Boolean "i_am_a_robot" is False
    print("I'm not a robot!")
print("-----------------")

# Python checks that the conditions are met (that the Booleans are True)
# going from top to bottom. If it finds a met condition, it will not
# check any of the remaining blocks in the if-else statement.

# Multiple conditions can be checked using elif statements. If no condition
# is met, then the else block will execute

print("--Example: If-Elif-Else--")
robots_i_have = 6
robots_i_want = 6
if robots_i_have > robots_i_want:
    print("I have more robots than want!")
elif robots_i_have == robots_i_want:
    print("I have exactly as many robots as I want!")
else:
    print("I have less robots than I want!")
print("-----------------")

# Generally, we want to avoid excessive branching, as it makes our code
# more complex. If we can get the job done using only if statements and not
# if-else statements, we should

print("--Example: Reducing Code Complexity--")
# This is our base variable value
statement_to_print = "I'm not a robot!"
i_am_a_robot = True

if i_am_a_robot:
    # This code will only execute if the Boolean "i_am_a_robot" is True
    statement_to_print = "I'm a robot!"

print(statement_to_print)
print("-----------------")

# ***
# FOR YOU: let's revisit our robot arm angle. Suppose we want to program a
# button to lower the arm at 15 degrees per second if the arm is in the raised
# position. Create a variable for arm speed (set to 0) and another variable
# for arm position (set to 37.5). Can you change the arm speed to -15
# if the arm position is greater than 35 degrees?

print("--Your Code: If-Else--")
arm_speed = 0
arm_position = 37.5
if arm_position > 35:
    arm_speed = -15
print(arm_speed)
print("-----------------")

# ***

########################################
# REPEATED CONTROL FLOW: LOOPS
########################################

# Loops allow us to perform operations multiple times and/or
# over multiple data elements. 

# "For" loops let us run a fixed number of operations

print("--Example: For Loop--")

statement_to_print = ""
words_to_print = ["I", "am", "a", "robot"]

for word in words_to_print:
    # This is a string concatenation operation
    statement_to_print = statement_to_print + " " + word
    print(statement_to_print)

print("-----------------")

# "While" loops let us run operations until a Boolean condition becomes
# False. Be careful here - if the condition never becomes False, the program
# will run forever!

print("--Example: While Loop--")

growing_number = 1
while growing_number < 100:
    # Every iteration, the variable is updated to itself multipled by 2
    growing_number = growing_number * 2
    print(growing_number)

print("-----------------")

# "While" loops are more common in robot programming - we keep running
# an operation until we tell the robot to do something different or
# the robot experiences a change in its state

# ***
# FOR YOU: let's make our robot arm code better using a while loop. Assume every loop
# iteration equates to 1 second in robot time. Create a variable for
# arm speed (set to 0 degrees per second) and another variable for
# arm position (set to 37.5 degrees).
# Can you continually set the arm speed to -15 degrees per second and update
# the arm position each iteration based on the arm speed until the arm position
# goes below 12.5 degrees? Can you set the arm speed back to 0 after this completes?
# Assume acceleration is instantaneous

# Note: you can force a Python program to stop running by pressing Ctrl+C
# in your terminal. You can force close the whole terminal by pressing the
# trash icon

print("--Your Code: Loops--")
arm_speed = 0
arm_position = 37.5

while arm_position > 12.5:
    arm_speed = -15
    arm_position = arm_position + arm_speed

arm_speed = 0
print(arm_position)
print("-----------------")

# ***

########################################
# FUNCTIONS
########################################

# Functions allow us to readily use a block of code in multiple
# places. We pass a function a set of data elements called arguments -
# the function will use the values of those arguments when executing
# its code.

print("--Example: Function--")

# The "def" keyword creates the function
# growth_rate and end_threshold are both arguments
def growing_number(growth_rate, end_threshold):
    """
    This is a docstring. It's a special type of string that lets us
    describe what our function is doing at a high level. Docstrings
    help others (and yourself in a couple of months) know what your code
    is doing. The docstring for this function would look like:

    This function generates a series of numbers based on a constant
    growth multiplier. The series ends when the number grows beyond
    the given end threshold.

    Args:
        growth_rate: multiplier used to constantly grow the number
        end_threshold: when the growing number goes beyond this threshold,
            the series will stop
    
    Returns:
        each of the numbers in the growth series collected in a list
    """

    growing_number = 1
    growing_series = []

    # Keep growing until we pass the threshold
    while growing_number < end_threshold:
        # Every iteration, the variable is updated to itself
        # multipled by the grwoth rate
        growing_number = growing_number * growth_rate

        # This operation adds a new data element to the end of the list
        growing_series = growing_series + [growing_number]

    # The data element coming after the "return" key word will become available
    # after calling this function
    return growing_series

# Now we call (use) the function to run the code
# This series is identical to our earlier example while loop
multiples_of_two = growing_number(2, 100)
print(multiples_of_two)
# This one changes the multiplier and the threshold number.
# Notice how easily we can resuse the code in the function
multiples_of_three = growing_number(3, 300)
print(multiples_of_three)

print("-----------------")

# ***
# FOR YOU: we may want to rotate multiple mechanisms on our robot to
# a given position at a given speed. To enable this, we can convert
# our robot arm loop code into a more general mechanism rotation function.

# Create a function that takes three arguments: the current position
# of the mechanism (in degrees), the goal position (in degrees),
# and the speed (in degrees per second). Recreate your robot arm loop
# code within this function (be careful to ensure your indentation is correct).
# Replace 37.5 with the current position argument, 12.5 with the goal position
# argument, and -15 with the speed argument. At the end of the function, 
# return the new arm position.

# To confirm your function works, call the function three separate times
# with the following argument sets. Store each returned value in their own
# variables and print each variable, like we showed in the example.
# current position: 37.5; goal position: 12.5; speed: -15
# current position: 90; goal position: 10; speed: -10

# If playing around with this, ensure current position is greater than goal
# position and speed is a negative value. Otherwise, the code will run forever
# until you terminate the program.

# Note: you can force a Python program to stop running by pressing Ctrl+C
# in your terminal. You can force close the whole terminal by pressing the
# trash icon

print("--Your Code: Functions--")
def rotate_mechanism(current_position, goal_position, speed):
    arm_speed = 0
    arm_position = current_position

    while arm_position > goal_position:
        arm_speed = speed
        arm_position = arm_position + arm_speed

    arm_speed = 0
    
    return arm_position


def clean_rotate_mechanism(current_position, goal_position, speed):
    while current_position > goal_position:
        current_position = current_position + speed
    
    return current_position


new_position = rotate_mechanism(37.5, 12.5, -15)
print(new_position)
new_position = rotate_mechanism(90, 10, -10)
print(new_position)
new_position = clean_rotate_mechanism(37.5, 12.5, -15)
print(new_position)
new_position = clean_rotate_mechanism(90, 10, -10)
print(new_position)
print("-----------------")

# ***

########################################
# CLASSES
########################################

# Classes are the foundation of much modern programming, and
# robot programming is no exception. In a nutshell, classes
# bring data elements and code logic together into one structure.
# They allow us to track the state of some part of our program and
# modify it directly. They also allow us to readily extend code.

print("--Example: Class--")

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
    # the __init__ method below has zero real arguments. Note that __init__
    # methods can have real arguments if we choose to create them
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
# (in degrees per second) as arguments. Recreate the code you wrote in your
# function, but be sure to use self.<your current position attibute> instead
# of the standalone variable for the current position.

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

class Mechanism():
    def __init__(self, current_position):
        self.current_position = current_position

    def rotate(self, goal_position, speed):
        while self.current_position > goal_position:
            self.current_position = self.current_position + speed

mechanism = Mechanism(37.5)
print(mechanism.current_position)
mechanism.rotate(25, -5.5)
print(mechanism.current_position)
mechanism.rotate(12.5, -2.5)
print(mechanism.current_position)

print("-----------------")

# ***
