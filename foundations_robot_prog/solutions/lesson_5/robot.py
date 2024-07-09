import commands2
import phoenix5
import wpilib

from commands.autonomous_routines import (
    rescale_motor_output,
    drive_straight_routine
)
from commands.tank_drive import TankDrive
from subsystems.drivetrain import WestCoastDrivetrain

####################################################################################
# Welcome to Lesson 5! Now that you have a good grasp of how to program a West
# Coast robot to be driven using an Xbox controller, we're going to introduce
# you to operating the robot autonomously. Autonomous operation means that the
# robot performs actions without any human input. FRC matches often start with 15
# seconds where robots run completely autonomously, so having good capabilities
# in this area is a major advantage toward winning games.

# Fundamentally, every autonomous routine can be represented as a mapping from
# match time to actuator inputs. Mathematically, this would look like
# f: t -> {inputs}. If we defined such a function for all time points in the
# period and had a perfect understanding of the physical system, then we could
# run the same routine repeatedly and have the robot perform the same actions
# exactly the same way every time. In reality, however, we do not have a perfect
# physical understanding. This means every individual routine run will
# be slightly different due to deviations between what we know and what reality
# is. To correct for this, we often use sensors to collect information about the
# physical world and define goal states that we want our robot to reach. Thus,
# a more complete autonomous routine mapping function would look like
# f: {t, sensors, state} -> {inputs, state}, where the mapping also includes
# control mechanisms that help us transition from the current state to the goal.

# We won't cover sensors, states, and control theory here in this lesson,
# though you will have the opportunity to learn more about these in the future
# if you so desire. For this lesson, we'll stick to a basic time-to-input
# representation and have the robot perform some simple actions.

# The recommended completion path for this lesson is as follows:
# 1. Write all of the code in commands/autonomous_actions.py
# 2. Write the method in subsystems/drivetrain.py
# 3. Write the first code block in commands/autonomous_routines.py,
#    then come back here and use it. Use the method you wrote in step 2
#    here and rescale the input speed here as well. Sim test and deploy your code.
# 4. Write the second code block in commands/autonomous_routines.py,
#    then come back here and use it. Sim test and deploy your code.
# 5. Write the third code block in commands/autonomous_routines.py,
#    then come back here and use it. Sim test and deploy your code.

# Look for "FOR YOU" within the code - this signals that you have something to do 
####################################################################################

# ***
# FOR YOU: once you've completed blocks 2 and/or 3 in
# commands/autonomous_routines.py, import your routine functions here.
# The code will be analogous to the following:

# from folder.file_name_no_extention import (function1, function2)

from commands.autonomous_routines import (
    drive_donut_routine,
    combined_drive_routine
)

# ***


class WestCoastRobot(commands2.TimedCommandRobot):
    """
    Robot with West Coast drivetrain subsystem. Uses differential drive for
    mobility. 
    """
    def robotInit(self):
        """
        Robot initializer - sets up drivetrain subsystem and component motors
        """
        # Easy access to TimedCommandRobot functionality
        super().__init__()

        # Four drive motors instantiated with the appropriate ports
        right_front_motor = phoenix5.WPI_TalonFX(31)
        right_back_motor = phoenix5.WPI_TalonFX(30)
        left_front_motor = phoenix5.WPI_TalonFX(21)
        left_back_motor = phoenix5.WPI_TalonFX(20)

        # Motors on each side of the robot collected to provide common instructions
        self.left_drive_motors = wpilib.MotorControllerGroup(left_front_motor, left_back_motor)
        self.right_drive_motors = wpilib.MotorControllerGroup(right_front_motor, right_back_motor)

        # Xbox controller interface with command framework functionality
        self.driver_controller = commands2.button.CommandXboxController(0)

        # West Coast Drivetrain subsystem
        self.drivetrain = WestCoastDrivetrain(self.left_drive_motors, self.right_drive_motors)

    def disabledInit(self):
        """
        Beginning setup and one-time component shutdown upon entering 
        the disabled state
        """
        pass

    def disabledPeriodic(self):
        """
        Continual robot shutdown procedures
        """
        pass

    def autonomousInit(self):
        """
        Autonomous routine initialization
        """
        # ***
        # FOR YOU: once you've updated subsystems/drivetrain.py, you'll need
        # to call the drivetrain instance attribute's .setDeadband() method to
        # set the overall drivetrain's deadband to be zero.

        # The code will be analogous to the following:
        # self.subsystem.setParameter(-1)

        self.drivetrain.setDeadband(0)

        # ***

        # ***
        # FOR YOU: we wrote the motor percentage rescale calculation for you,
        # now you'll need to use it. We want the motors to operate at 25% speed
        # (0.25 as a float). The motors have a minimum output percentage of 4%
        # (0.04 as a float) and a maximum output percentage of 100% (1 as a float).

        # Set a speed variable to be the result of a rescale_motor_output() call.
        # Pass the function the desired speed percentage, minimum output precentage,
        # and maximum output percentage as described above.

        # Your code will be analogous to the following:
        # value = some_function(input1, input2, input3)

        speed = rescale_motor_output(0.25, 0.04, 1)

        # ***

        # ***
        # FOR YOU: once you have an autonomous routine in place, you can use
        # use it here. Because we don't have any clock-specific adjustments to
        # the routine, we will use it in the initialization call instead of
        # the periodic call.

        # In the backend, the robot executor runs a scheduler that determines
        # which commands to run on a given clock tick. Before, we changed the
        # default command of the drivetrain subsytem, which automatically scheduled
        # that command. Now, we need to explicitly schedule our autonomous routine
        # commands. Once the command completes, it will be removed from the schedule.

        # We recommend that you start by calling the drive straight routine
        # and scheduling it. Then, you should delete that code and replace it by
        # calling the spin-in-place routine and scheduling it. Finally, you should
        # delete that code and replace it by calling the complete drive routine
        # that does both. For each routine call, you will pass it the drivetrain
        # instance attribute of this robot class and the speed variable you
        # created above.

        # One routine call and schedule will be analogous to the following:
        # some_routine(self.subsystem, drive_parameter).putOnSchedule()

        if False:
            drive_straight_routine(self.drivetrain, speed).schedule()
            drive_donut_routine(self.drivetrain, speed).schedule()
        combined_drive_routine(self.drivetrain, speed).schedule()

        # ***


    def autonomousPeriodic(self):
        """
        Autonomous routine execution
        """
        pass

    def teleopInit(self):
        """
        Set up operations for the teleoperated period
        """
        # We want driving to be smooth, so we set the drivetrain deadband back
        # to its default value
        self.drivetrain.setDeadband(0.02)

        # We set up a manual tank drive so we can reposition the robot easily
        self.drivetrain.setDefaultCommand(
            TankDrive(
                lambda: self.driver_controller.getLeftY(),
                lambda: self.driver_controller.getRightY(),
                self.drivetrain
            )
        )

    def teleopPeriodic(self):
        """
        Run driver operations on every clock tick
        """
        pass

    def testInit(self):
        """
        Debug code
        """
        pass

    def testPeriodic(self):
        """
        Debug code
        """
        pass


if __name__ == "__main__":
    wpilib.run(WestCoastRobot)
