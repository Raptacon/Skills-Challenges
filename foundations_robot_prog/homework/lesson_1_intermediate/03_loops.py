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
# FOR YOU: let's make our robot arm code better. Assume every loop
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
# <your code here>
print("-----------------")

# ***
