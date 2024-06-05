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
    # The + operator is "overloaded" to also be a string concatenation operator
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
# FOR YOU: let's make our robot arm code from the if-else script better.
# We're going to lower our arm until it reaches a goal position.
# Assume that every turn of a loop equates to 1 second in robot time, and
# let's say our arm is currently moving up at half a degree per second.

# Set the current arm position angle to be 37.5 degrees by replacing the
# first "None". Can you set the goal arm position to be 12.5 degrees by
# replacing the second "None"?

# Now, we need to tell Python how many robot seconds it should try lowering the
# arm to the goal position. Fill in the seconds of moving list with integers
# 1 through 5. This tells Python we want to try lowering the arm every second
# for 5 seconds.

# Let's move our arm. Replace the third "None" with -15 to tell the robot we
# want to move the arm down 15 degrees each second. Then, update the
# current position angle by setting the variable to itself plus the arm speed
# (you can refer to the counter example from the "variables and types" section for help).
# Finally, determine if the arm has reached the goal position by comparing the
# current position angle variable to the goal position angle variable using "<"
# operator. If we reach the goal position, we'll tell Python to stop moving the arm.
# After the loop completes, set the arm speed to 0 - we don't want to break the arm!

print("--Your Code: Loops--")
arm_speed = 0.5
arm_current_position_angle = None
arm_goal_position_angle = None
arm_reached_goal_position = False

seconds_to_try_moving = []

# We run the code indented within the "for" loop for every second in the list
for second in seconds_to_try_moving:
    arm_speed = None
    arm_current_position_angle = None
    arm_reached_goal_position = None

    if arm_reached_goal_position:
        # "break" is a special keyword that tells Python to stop looping
        break

arm_speed = None

print(arm_current_position_angle)
print(arm_speed)
print(arm_reached_goal_position)
print("-----------------")

# ***
