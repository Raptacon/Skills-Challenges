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
        # FOR YOU (4.4)

        aa.DiffDriveStraight(drivetrain, speed).withTimeout(1),
        commands2.cmd.waitSeconds(1),
        aa.DiffDriveStraight(drivetrain, -1 * speed).withTimeout(1)

        # ***

    )

# ***
# FOR YOU (4.7)

def drive_donut_routine(drivetrain, speed):
    return commands2.cmd.sequence(
        aa.DiffDriveDonuts(drivetrain, speed).withTimeout(1),
        commands2.cmd.waitSeconds(1),
        aa.DiffDriveDonuts(drivetrain, -1 * speed).withTimeout(1)
    )

# ***

# ***
# FOR YOU (4.9)

def combined_drive_routine(drivetrain, speed):
    return commands2.cmd.sequence(
        drive_straight_routine(drivetrain, speed),
        commands2.cmd.waitSeconds(1),
        drive_donut_routine(drivetrain, speed)
    )

# ***
