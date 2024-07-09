# ***
# Now that we have a set of autonomous action commands, we need to compose
# them into autonomous routines. Routines accomplish one or more goals without
# human input. For example, in the 2024 FRC game, autonomous routines would
# shoot a piece that was pre-loaded on the robot, then go acquire a piece from
# the ground, then position the robot for shooting, then shoot the piece, and
# so on until the autonomous period ended. A common theme is that autonomous
# routines involve performing a small set of similar actions multiple times
# from different positions.

# For this lesson, we'll start by building a routine to drive forward
# for a couple of seconds, stop, and then come back. Then, we'll extend that
# routine to spin in place in one direction, stop, then spin back in the opposite
# direction.

# To do this, we need to introduce a new aspect of the commands framework:
# command compositions. Command compositions allow you to build more complex
# commands by setting rules for how to run multiple simpler commands together.
# You can find available compositions on the following webpage:
# https://robotpy.readthedocs.io/projects/commands-v2/en/latest/commands2.cmd/functions.html

# You may notice that the compositions listed there are functions that return
# command objects rather than classes themselves. There is a class version of
# each composition, however we generally recommend using the simpler function
# interface unless you have an explicit reason to use a class.

# We're going to make usse of the following compositions here:
# commands2.cmd.deadline(): runs a set of commands until a designated deadline
# command completes. We'll use this and a wait command to run an action
# for a specified duration.
# commands2.cmd.sequence(): runs a given set of commands in the order they
# are provided as arguments. Our sequence will be: drive forward -> wait ->
# drive backward -> wait -> spin one way -> wait -> spin back.

# ***

import commands2

import commands.autonomous_actions as aa


def rescale_motor_output(desired_output, min_output, max_output):
    """
    Given a desired output percentage for a motor, rescale the percentage
    based on the maximum output percentage for the motor and the minimum
    output percentage (the deadband) for it. The rescaled input percentage
    will be sent to the motor and produce the desired output percentage.

    Args:
        desired_output: the output percentage we want the motor to be, with
            domain [-1, 1]
        min_output: the minimum output percentage allowed by the motor
        max_output: the maximum output percentage allowed by the motor

    Returns:
        The input percentage that will produce the desired output percentage
    """
    return (desired_output * (max_output - min_output)) + min_output


def drive_straight_routine(drivetrain, speed):
    """
    This function performs a sequence composition of straight driving
    actions and waiting actions. The resulting sequence command terminates
    when the final command given to it ends.

    Args:
        drivetrain: custom subsystem representing a drivetrain
        speed: the speed percentage, with domain [-1, 1], to drive the robot at

    Returns:
        composed sequence command that drives the robot forward, pauses,
            and finally drives the robot back
    """
    return commands2.cmd.sequence(
        # ***
        # FOR YOU: we're going to start by filling out the drive straight routine.
        # We've written the sequence command structure and told Python to return
        # the command it produces. You will need to pass the individual commands
        # that comprise the routine to the sequence call.

        # The routine will start by having the robot drive forward for 1 second.
        # Then, the robot will stop sending power to the motors for one second,
        # and finally the robot will drive backward for 1 second. In theory,
        # the robot should return to its original position.

        # Use command composition functions and the "drive straight" class you
        # wrote in the actions file to create comamnd objects for the
        # three steps described above. To run a single drive straight step,
        # you do a deadline composition with a wait command and your custom command.
        # To drive the robot backward, you'll need to multiply the speed given
        # in the args above by -1. Directly pass each composed command as separate
        # arguments to the sequence call - you do not need to assign them to
        # variables first.

        # You will need the following to do this:
        # commands2.cmd.deadline(): takes a deadline command object as its first
        # argument and takes one or more other command objects that will all run
        # together. When the deadline command finishes, all commands in the
        # composition finish.

        # commands2.cmd.waitSeconds(): creates a command object that does nothing
        # but runs for a specified number of seconds. Takes the duration in
        # seconds as its only argument.

        # aa.DiffDriveStraight(): your custom command that drives the robot
        # in a straight direction.

        # The code will be analagous to the following:
        # some_composition(wait_some_time(), actionCommand(input1, input2)),
        # wait_some_time(),
        # some_composition(wait_some_time(), actionCommand(input1, -1 * input2))

        commands2.cmd.deadline(
            commands2.cmd.waitSeconds(1), aa.DiffDriveStraight(drivetrain, speed)
        ),
        commands2.cmd.waitSeconds(1),
        commands2.cmd.deadline(
            commands2.cmd.waitSeconds(1), aa.DiffDriveStraight(drivetrain, -1 * speed)
        )

        # ***

    )

# ***
# FOR YOU: now, we're going to build out the spinning-in-place routine. The
# donut routine will be very similar to the drive straight routine, except it
# will use the other custom command class you wrote. We're going to let you
# write out the full function definition so you get practice writing functions
# in addition to classes.

# The requirements for this step are as follows:
# 1) Create a new function for the donut routine, taking a drivetrain subsystem and
#    a speed percentage as arguments.
# 2) Within this function, immediately return the result of a
#    commands2.cmd.sequence() composition call. Pass arguments to this sequence
#    call defined as follows:
#       a) Using a commands2.cmd.deadline() call, compose a deadline 1-second wait
#          command with your custom donut drive command. The wait command will need
#          commands2.cmd.waitSeconds() with 1 passed as its argument (for 1 second).
#          Your custom command will need to be passed the drivetrain and speed
#          percentage given above as arguments to its constructor.
#      b) Use a commands2.cmd.waitSeconds() call to make a command that does nothing
#         for 1 second.
#      c) Repeat step a) for the third command, but multiply the speed percentage
#         by -1 to make the robot spin the opposite direction.

# The code will be highly analogous to drive_straight_routine

def drive_donut_routine(drivetrain, speed):
    return commands2.cmd.sequence(
        commands2.cmd.deadline(
            commands2.cmd.waitSeconds(1), aa.DiffDriveDonuts(drivetrain, speed)
        ),
        commands2.cmd.waitSeconds(1),
        commands2.cmd.deadline(
            commands2.cmd.waitSeconds(1), aa.DiffDriveDonuts(drivetrain, -1 * speed)
        ),
    )

# ***

# ***
# FOR YOU: to finish, we'll combine the drive straight and spin-in-place routines
# together to make a complete routine. They will be separated by a one second
# wait.

# The requirements for this step are as follows:
# 1) Create a new function for the combined drive routine, taking a drivetrain
#    subsystem and a speed percentage as arguments.
# 2) Within this function, immediately return the result of a
#    commands2.cmd.sequence() composition call. Pass arguments to this sequence
#    call defined as follows:
#      a) Call drive_straight_routine(), defined above, to make the first command.
#         Pass it the drivetrain and speed percentage given above.
#      b) Use a commands2.cmd.waitSeconds() call to make a command that does nothing
#         for 1 second.
#      c) Call your donut route function to make the third command.
#         Pass it the drivetrain and speed percentage given above.

def combined_drive_routine(drivetrain, speed):
    return commands2.cmd.sequence(
        drive_straight_routine(drivetrain, speed),
        commands2.cmd.waitSeconds(1),
        drive_donut_routine(drivetrain, speed)
    )

# ***
