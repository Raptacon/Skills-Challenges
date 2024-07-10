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
        commands2.cmd.deadline(
            commands2.cmd.waitSeconds(1), aa.DiffDriveStraight(drivetrain, speed)
        ),
        commands2.cmd.waitSeconds(1),
        commands2.cmd.deadline(
            commands2.cmd.waitSeconds(1), aa.DiffDriveStraight(drivetrain, -1 * speed)
        )
    )


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


def combined_drive_routine(drivetrain, speed):
    return commands2.cmd.sequence(
        drive_straight_routine(drivetrain, speed),
        commands2.cmd.waitSeconds(1),
        drive_donut_routine(drivetrain, speed)
    )


# ***
# FOR YOU: you can use command composition functions here to create your routine.
# Available compositions functions can be found at
# https://robotpy.readthedocs.io/projects/commands-v2/en/latest/commands2.cmd/functions.html

# We've included the routines from Lesson 5 so you have examples readily available
# for reference. Remember to use and pass in the proper arguments - a routine function
# needs to take in as arguments each of the arguments of its component actions.

# <your code here>

# ***
