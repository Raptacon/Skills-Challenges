# Internal imports
from typing import Tuple


class RobotConfig:
    default_start_pose: Tuple[float] = (0.0, 0.0, 0.0)
    # TODO: JD check that these modules are given in correct order
    # Give in front-left, front-right, back-left, back-right order
    swerve_module_channels: Tuple[int] = (50, 53, 56, 59)
    # TODO: JD if swerve_model_channelse need movement, move these cals too
    swerve_abs_encoder_calibrations: Tuple[float] = (
        83.496 / 360.0, 356.396 / 360.0, 50.098 / 360.0, 69.785 / 360.0
    )
    swerve_steer_pid: Tuple[float] = (0.3, 1, 0)
    # TODO: JD tune drive PID
    swerve_drive_pid: Tuple[float] = (0.0020645, 0, 0)
