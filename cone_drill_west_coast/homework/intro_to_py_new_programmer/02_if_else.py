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
# button to lower the arm at 15 degrees per second if the arm is resting 
# in the raised position. Because it is resting, starting arm speed will be 0.

# Can you replace the first "None" with 37.5 degrees for the starting position
# of the arm? Then, can you tell Python the threshold angle above which
# we consider the arm raised by replacing the second "None" with 35 degrees?
# Use the angle and threshold variables, along with the ">" operator, to replace
# the third "None" with a Boolean saying our arm is in the raised position?

# Finally - can you change the arm speed to -15 (replace the fourth "None" to do so)
# if the arm is raised?

print("--Your Code: If-Else--")
arm_speed = 0
arm_position_angle = None
arm_positition_threshold = None

arm_is_in_raised_position = None

if arm_is_in_raised_position:
    arm_speed = None

print(arm_speed)
print("-----------------")

# ***
