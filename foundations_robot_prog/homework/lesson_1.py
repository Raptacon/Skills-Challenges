########################################
# LESSON 1 HOMEWORK:
# PYTHON BASICS
########################################

# Hello! In this homework, we will walk you through the basics
# of the Python programming language.

# To start, we'll go over basic data types and declaring variables.

# Look for "FOR YOU" as you go through the script - this signals that
# you need to do something. The *** will bound the area where you should
# write code

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

print("-----------------")
print(counter)
print("-----------------")

# ***
# FOR YOU: let's say we have four motors, and we want to be able to reference
# this in our code. Can you declare a "motor quantity" variable and print it?

print("-----------------")
# <your code here>
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

print("-----------------")
print(counter is 0)
print(counter > 1)
print(not (counter > 1))
print("-----------------")

# ***
# FOR YOU: can you check if you have four motors? How about more than 6?

print("-----------------")
# <your code here>
print("-----------------")

# ***

# - Integers (4; 0; -3) are whole numbers. We commonly use these for
# count quantities and identification numbers
# We can use common mathematical operators to update integers:
# "+" is addition
# "-" is subtraction
# "*" is multiplication
# "/" is division

print("-----------------")
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

print("-----------------")
# <your code here>
print("-----------------")

# Now say we want to give our robots away to other teams, two per team. Can you
# calculate how many teams we can give these robots to?

print("-----------------")
# <your code here>
print("-----------------")

# ***

# - Floats (5.6; 0.0; -3.14) are decimal numbers. We often use these
# to track physical values, like the number of feet a robot has travelled
# The same mathematical operators we used with integers can be used with floats.

print("-----------------")
print(5.5 + 3.5)
print(70 / 30)
print("-----------------")

# ***
# FOR YOU: suppose a robot arm sits 12.5 degrees above horizontal as its
# starting position, can you create a new variable for this?
# Then, suppose we want a set point for the arm that is three times this starting
# angle, can you calculate this angle and store it in a new variable?

print("-----------------")
# <your code here>
print("-----------------")

# ***

# - Strings ("Hello World"; '00454112') are alphanumeric characters. We
# often use these to print messages, provide names, and classify things

print("-----------------")
my_robot_name = "Green Bot"
print(my_robot_name)
print("-----------------")

# ***
# FOR YOU: can you print what you're most looking forward to learning
# in this robotics workshop?

print("-----------------")
# <your code here>
print("-----------------")

# ***

# Lists ([1, 2, 3]; ["a", "b", "c"]; [10, 10.123, "11"])
# let us store and iterate over multiple data elements.
# Any data element in a list can be of any data type, including
# another list! Data elements can be freely added or removed
# from lists

print("-----------------")
my_robots = ["Breadbox", "Green Bot"]
print(my_robots)
my_variables = [counter, my_robot_name, my_robots]
print(my_variables)
print(my_robots[0])
print(my_variables[2])
print("-----------------")

# ***
# FOR YOU: can you put all of the variables you have made into a list?
# Can you print the second element (index 1) of it?

print("-----------------")
# <your code here>
print("-----------------")

# ***

# Dictionaries ({1: "a", "b": 2}) let us map values to keys for quick,
# iterable access. Keys need to be data elements of a specific set of
# types (mostly we use integers and strings for keys). Values can be data
# elements of any any type, including another dictionary! 

print("-----------------")
my_variables_dict = {
    1: my_variables,
    2: counter,
    "my_robot_name": my_robot_name,
    "my_robots": my_robots
}
print(my_variables_dict)
print(my_variables_dict[2])
print(my_variables_dict["my_robot_name"])
print("-----------------")

# ***
# FOR YOU: can you put all of the variables you have made into a dicionary,
# using integers as keys? Can you print the value mapped to key 1?

print("-----------------")
# <your code here>
print("-----------------")

# ***

########################################
# CONDITIONAL CONTROL FLOW: IF-ELSE
########################################

# If-else blocks let us execute certain parts of code
# 
