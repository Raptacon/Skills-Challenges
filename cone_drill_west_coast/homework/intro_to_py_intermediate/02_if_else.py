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
# <your code here>
print("-----------------")

# ***
