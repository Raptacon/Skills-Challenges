import commands2


class ArcadeDrive(commands2.Command):
    """
    Arcade drive is a type of differential drive where the driver gives a single
    robot speed and a turn angle instead of specifying the speed of each side.
    In computing, we call this an abstraction - instead of knowing a lot of
    internal details on how the code or mechanism works to operate it, a simpler
    interface is abtracted that requires only a couple of inputs which are easier
    to understand.

    The choice of arcade drive versus tank drive also has a lot of implications
    for the driver. Generally, arcade drive is considered to have a higher floor
    but a lower ceiling. It is easier to start driving the robot but the skill
    potential is reduced. Meanwhile, tank drive is generally harder to start
    with but provides finer control, making skillful maneuvers possible.
    """
    def __init__(self, speed_percentage, turn_angle_percentage, drivetrain):
        """
        This constructor method has three parameters: the percentage of the max
        speed of the robot, the percentage of the max turn rate of the robot,
        and the drivetrain subsystem this command should use to operate the
        robot. Command constructor methods typically take the operating
        inputs for the action to perform as a set of arguments and the
        drivetrain on which the action will be performed.

        One key point is that commands typically take callables as operating
        inputs rather than scalar values. This is because the inputs are
        often constantly changing over the course of a match, so we don't want
        to create our command with one fixed input from the start. The callable
        is often a function that returns the value of the opearting input at the
        time when it is called.
        """
        # We need this to do Command method calls directly off of "self"
        super().__init__()

        # ***
        # FOR YOU (3.2)

        self.speed_percentage = speed_percentage
        self.turn_angle_percentage = turn_angle_percentage
        self.drivetrain = drivetrain

        # ***

        # ***
        # FOR YOU (3.3)

        self.addRequirements(self.drivetrain)

        # ***

   

    def execute(self):
        """
        Now we're going to start overriding methods that exist in the parent
        Command class. Overriding means that the method has been inherited
        into the child class (in our case, ArcadeDrive) and is available to use,
        but we want to change the behavior of it.

        The execute method provides the logic for the action the robot should
        perform when this command is running. For example, the execute method
        for an arm might tell the lift motor to raise the arm 45 degrees and then
        tell the extention motor to extend the arm out by 1 foot. Execute methods
        often wrap around a specific interface provided by the subsystem and may
        include additional logic to perform a cohesive action.
        """

        # ***
        # FOR YOU (3.4)

        self.drivetrain.arcadeDrive(self.speed_percentage(), self.turn_angle_percentage())

        # ***

    def end(self, interrupted):
        """
        Now we override the "end" method. This method specifies what should
        happen when the command is done running. End methods often involve
        stopping actuators in the required subsystems. Some end methods may
        place the subsystems into a state where they can easily transition
        to a different command.

        The "interrupted" parameter denotes why the end method was called. If
        "interrupted" is True, then the command is being terminated because
        of an explicit cancellation or because of a failure. We don't use it
        in our version of the end method, but we still need to provide it
        because any code calling an end method from an object of type Command
        will pass it the Boolean as an argument. If we don't provide the parameter,
        "end" will raise an error. This is an important aspect of inheritance
        and method overrides.
        """
        # ***
        # FOR YOU (3.5)

        self.drivetrain.arcadeDrive(0, 0)

        # ***

    
    def isFinished(self):
        """
        This method determines whether the command should finish executing
        at a checkpoint where this method is called. By setting this to False,
        we tell the robot executor to keep running this command on the robot
        until we explicitly tell the executor to stop running it.
        """
        return False
