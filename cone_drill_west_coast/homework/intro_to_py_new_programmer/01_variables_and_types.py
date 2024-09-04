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
# python 01_variables_and_types.py

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
# this in our code. Can you replace the "None" below to tell Python
# we have four motors via the "motor_quantity" variable?

print("--Your Code: Variable Declaration--")
motor_quantity = None
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
# FOR YOU: can you check if you have four motors by replacing the first
# "None" below with the appropriate value? How about checking for more than 6 motors
# by replacing the second "None" and using the ">" operator?

print("--Your Code: Booleans--")
i_have_four_motors = motor_quantity == None
i_have_above_six_motors = None
print(i_have_four_motors)
print(i_have_above_six_motors)
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
# four more. Can you replace the first two "None"s below to represent,
# these values in Python? Can you then replace the third "None"
# with the right Python variables and the "+" operator
# to calculate the new number of robots?

print("--Your Code: Integers Part 1--")
number_of_robots = None
print(number_of_robots)

additional_robots = None
number_of_robots = None
print(number_of_robots)
print("-----------------")

# Now say we want to give our robots away to other teams, two per team. Can you
# use your number of robots variable and a division operation to calcualte 
# how many teams are getting robots?

print("--Your Code: Integers Part 2--")
number_of_teams_getting_robots = None
print(number_of_teams_getting_robots)
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
# starting position, can you replace the appropriate "None" for this?
# Then, suppose we want a set point for the arm that is three times this starting
# angle, can you calculate this angle using the starting angle variable and
# a multiplication operator?

print("--Your Code: Floats--")
robot_arm_starting_angle = None
new_set_point_angle = None
print(new_set_point_angle)
print("-----------------")

# ***

# - Strings ("Hello World"; '00454112') are alphanumeric characters. We
# often use these to print messages, provide names, and classify things

print("--Example: Strings--")
my_robot_name = "Green Bot"
print(my_robot_name)
print("-----------------")

# ***
# FOR YOU: can you replace the "<your code here>" line completely and
# print what you're most looking forward to learning in this robotics workshop?

print("--Your Code: Strings--")
# <your code here>
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
# FOR YOU: suppose we built three new robots in the offseason: 
# "SpiderBot", "Dover Rover", and "Conquerer". Can you delete the "None"
# from the names list below and fill it in with these robot names?
# Then, can you change the "0" index below to access and print
# the second name in the list? Note - the "0" index would access the
# first element, the "4" index would access the fifth element, etc.

print("--Your Code: Lists--")
names_of_new_robots = [None]
print(names_of_new_robots)

third_robot_name = names_of_new_robots[0]
print(third_robot_name)
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
# FOR YOU: you've made a lot of variables throughout this script.
# Can you change the "key" Nones (the ones before the colon) to
# integers 1, 2, and 3? Then, can you change the "value" Nones (the
# ones after the colon) each with a variable of your choice?

print("--Your Code: Dictionaries--")
your_variables_in_a_dict = {
    None: None,
    None: None,
    None: None
}
print(your_variables_in_a_dict)
print("-----------------")

# ***