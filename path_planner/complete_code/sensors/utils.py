# Internal imports
from constants import SparkMaxConstants

# Third-party imports
import rev


def configureSparkMaxCanRates(
    config: rev.SparkMaxConfig,
    drive_motor_flag: bool,
    faultRateMs: int = SparkMaxConstants.faultRateMs,
    motorPosRateMs: int = SparkMaxConstants.motorPosRateMs,
    appliedOutputRateMs: int = SparkMaxConstants.appliedOutputRateMs
) -> None:
    """
    """
    (
        config.signals
        # Fixed settings
        .absoluteEncoderPositionAlwaysOn(False)
        .absoluteEncoderVelocityAlwaysOn(False)
        .analogPositionAlwaysOn(False)
        .analogVelocityAlwaysOn(False)
        .analogVoltageAlwaysOn(False)
        .externalOrAltEncoderPositionAlwaysOn(False)
        .externalOrAltEncoderVelocityAlwaysOn(False)
        .primaryEncoderPositionAlwaysOn(True)
        .IAccumulationAlwaysOn(False)

        # Input settings
        .primaryEncoderVelocityAlwaysOn(drive_motor_flag)
        .primaryEncoderPositionPeriodMs(motorPosRateMs)
        .appliedOutputPeriodMs(appliedOutputRateMs)
        .faultsPeriodMs(faultRateMs)
    )
