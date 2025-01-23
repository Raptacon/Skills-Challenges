# Native imports
from typing import Tuple

# Internal imports
from constants import SwerveDriveConsts

# Third-party imports
from pathplannerlib.config import ModuleConfig, RobotConfig
from wpimath.geometry import Transform3d, Translation3d, Rotation3d

class OperatorRobotConfig:
    default_start_pose: Tuple[float] = (2, 7, 0.0) #(2.0, 7.0, 0.0) #(14.535, 1.0, 180.0)
    # Give in front-left, front-right, back-left, back-right order
    swerve_module_channels: Tuple[int] = (50, 53, 56, 59)
    swerve_abs_encoder_calibrations: Tuple[float] = (
        258.92568 / 360.0, 189.14076 / 360.0, 213.2226 / 360.0, 250.83972 / 360.0
    )
    swerve_steer_pid: Tuple[float] = (0.01, 0, 0)
    swerve_drive_pid: Tuple[float] = (0.1, 0, 0.1, 1 / 473)
    pathplanner_translation_pid: Tuple[float] = (5.0, 0.0, 0.0)
    pathplanner_rotation_pid: Tuple[float] = (5.0, 0.0, 0.0)

    robotToCam = Transform3d(
        Translation3d(0.5, 0.0, 0.5),
        Rotation3d.fromDegrees(0.0, -30.0, 0.0),
    )

