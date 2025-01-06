# Internal imports
from constants import SparkMaxConstants

# Third-party imports
import rev


def configureSparkMaxCanRates(
    config: rev.SparkMaxConfig,
    faultRateMs: int = SparkMaxConstants.faultRateMs,
    motorTelmRateMs: int = SparkMaxConstants.motorTelmRateMs,
    motorPosRateMs: int = SparkMaxConstants.motorPosRateMs,
    analogRateMs: int = SparkMaxConstants.analogRateMs,
    altEncoderRateMs: int = SparkMaxConstants.altEncoderRateMs,
    dutyCycleEncRateMs: int = SparkMaxConstants.dutyCycleEncRateMs,
    dutyCycleEncVelRateMs: int = SparkMaxConstants.dutyCycleEncVelRateMs
) -> None:
    """
    """
    config.signals.faultsPeriodMs(faultRateMs)
    config.signals.primaryEncoderPositionPeriodMs(motorPosRateMs)
    config.signals.analogPositionPeriodMs(analogRateMs)
    config.signals.motorTemperaturePeriodMs(motorTelmRateMs)
    config.signals.absoluteEncoderPositionPeriodMs(dutyCycleEncRateMs)
    config.signals.absoluteEncoderVelocityPeriodMs(dutyCycleEncVelRateMs)
    config.signals.externalOrAltEncoderPosition(altEncoderRateMs)
