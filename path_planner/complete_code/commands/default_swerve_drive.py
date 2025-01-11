# # Native imports
# from typing import Callable

# # Internal imports
# from subsystems.drivetrain.drivetrain import SwerveDrivetrain

# # Third-party imports
# import commands2

# class DefaultDrive(commands2.Command):
#     """
#     """
#     def __init__ (
#         self,
#         driveTrain: SwerveDrivetrain,
#         velocity_vector_x: Callable[[], float],
#         velocity_vector_y: Callable[[], float],
#         angular_velocity: Callable[[], float],
#         field: Callable[[], bool]
#     ) -> None:
#         """
#         """
#         super().__init__()

#         self.driveTrain = driveTrain
#         self.forward = forward
#         self.translation = translation
#         self.rotation = rotation
#         self.field = field
#         self.addRequirements(self.driveTrain)

#     def execute(self) -> None:
#         """
#         """
#         self.driveTrain.drive(self.forward(), self.translation(), self.rotation(), self.field())