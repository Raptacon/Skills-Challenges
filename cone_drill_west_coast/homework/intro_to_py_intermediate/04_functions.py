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
# and the speed (in degrees per second). Now, within the function,
# use a while loop to continually add the speed to the current position
# attribute until the current position falls below the goal position. 

# To confirm your function works, call the function two separate times
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
# <your code here>
print("-----------------")

# ***
