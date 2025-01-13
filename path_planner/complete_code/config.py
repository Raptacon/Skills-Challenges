# Internal imports
from typing import Tuple


class RobotConfig:
    default_start_pose: Tuple[float] = (0.0, 0.0, 0.0)
    # Give in front-left, front-right, back-left, back-right order
    swerve_module_channels: Tuple[int] = (50, 53, 56, 59)
    swerve_abs_encoder_calibrations: Tuple[float] = (
        276.1524 / 360.0, 352.96884 / 360.0, 323.1738 / 360.0, 289.77552 / 360.0
    )
    # 83.496 356.396 50.098 69.785
    #swerve_steer_pid: Tuple[float] = (0.3, 1, 0)
    swerve_steer_pid: Tuple[float] = (0.01, 0, 0)
    # TODO: JD tune drive PID
    swerve_drive_pid: Tuple[float] = (0.0020645, 0, 0)
