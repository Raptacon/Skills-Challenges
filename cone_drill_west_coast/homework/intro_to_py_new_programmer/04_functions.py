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

# Our takes three required arguments and one optional argument: the current position
# of the mechanism (in degrees), the goal position (in degrees),
# the speed (in degrees per second), and the seconds to try moving.

# Now, we'll build out the movement logic we had before within this function. 
# Update the current position angle by setting the variable to itself plus the mech
# speed. Determine if the mechamism has reached the goal position by comparing the
# current position angle variable to the goal position angle argument using "<"
# operator. If we reach the goal position, we'll tell Python to stop moving the mech.
# After the loop completes, set the mechanism speed to 0 - we don't want to break it!
# The function will return the final position of the mechanism - we can
# capture this value within a variable

# To confirm the function works, we'll try different argument sets. Move an arm
# by the replacing the first three placeholder zeros with the current position of
# 37.5, the goal position of 12.5, and the speed of -15, in that order.
# Move a shooter by replacing the second three placeholder zeros with the current
# position of 90, the goald position of 10 and the speed of -10, in that order
# In doing this, we are passing parameter values to the function and reusing
# the same code to do muliple things with the robot!

# If playing around with this, ensure current position is greater than goal
# position and speed is a negative value.

print("--Your Code: Functions--")


def move_mechanism_to_goal(
    mech_current_position_angle,
    mech_goal_position_angle,
    mech_speed,
    # optional arguments can be given a value when using a function, but
    # if no value is given it will use what we tell it after the "="
    seconds_to_try_moving = 20
):
    mech_reached_goal_position = False

    # "range" is a special Python function that generates a sequence of
    # integers up to the given integer
    for second in range(seconds_to_try_moving):
        mech_current_position_angle = None
        mech_reached_goal_position = None

        if mech_reached_goal_position:
            # "break" is a special keyword that tells Python to stop looping
            break

    mech_speed = None

    return mech_current_position_angle

move_arm = move_mechanism_to_goal(0, 0, 0)
print(move_arm)

move_shooter = move_mechanism_to_goal(0, 0, 0)
print(move_shooter)

print("-----------------")

# ***
