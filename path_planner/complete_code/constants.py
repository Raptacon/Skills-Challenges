"""
Collection of numeric constants that define physical properties of the robot
"""

# Native imports
import math

#############################
# SENSORS ###################
#############################


class SparkMaxConstants:
    faultRateMs: int = 50,
    motorTelmRateMs: int = 50,
    motorPosRateMs: int = 50,
    analogRateMs: int = 1833,
    altEncoderRateMs: int = 1050,
    dutyCycleEncRateMs: int = 2150,
    dutyCycleEncVelRateMs: int = 3150


#############################
# SWERVE ###################
#############################


class SwerveDriveConsts:
    moduleFrontLeftX: float = -0.3302
    moduleFrontLeftY: float = 0.3556
    moduleFrontRightX: float = 0.3302
    moduleFrontRightY: float = 0.3556
    moduleBackLeftX: float = -0.3302
    moduleBackLeftY: float = -0.3556
    moduleBackRightX: float = 0.3302
    moduleBackRightY: float = -0.3556

    maxTranslationMPS: float = 4.14528


class SwerveModuleMk4iConsts:
    """ https://github.com/SwerveDriveSpecialties/swerve-lib/blob/develop/src/main/java/com/swervedrivespecialties/swervelib/ctre/Falcon500DriveControllerFactoryBuilder.java """
    kNominalVoltage: float = 12.0
    kDriveCurrentLimit: float = 20.0
    kSteerCurrentLimit: float = 20.0
    kTicksPerRotation: int = 1
    kCanStatusFrameHz: int = 10


class SwerveModuleMk4iL1Consts(SwerveModuleMk4iConsts):
    """
    https://github.com/SwerveDriveSpecialties/swerve-lib/blob/f6f4de65808d468ed01cc5ca39bf322383838fcd/src/main/java/com/swervedrivespecialties/swervelib/SdsModuleConfigurations.java#L19
    Order: wheelDiameter, driveDreuction, driveInverted, steerReduction, steerInverted
    """
    wheelDiameter: float = 0.10033
    driveReduction: float = (14.0 / 50.0) * (25.0 / 19.0) * (15.0 / 45.0)
    steerReduction: float = (15.0 / 32.0) * (10.0 / 60.0)
    
    drivePositionConversionFactor : float = math.pi * wheelDiameter * driveReduction / SwerveModuleMk4iConsts.kTicksPerRotation
    driveVelocityConversionFactor: float = drivePositionConversionFactor * 10.0
    steerPositionConversionFactor: float = 2.0 * math.pi / SwerveModuleMk4iConsts.kTicksPerRotation * steerReduction
    steerVelocityConversionFactor: float = steerPositionConversionFactor * 10.0

    moduleType: str = "Mk4L1"


class SwerveModuleMk4iL2Consts(SwerveModuleMk4iConsts):
    """
    https://github.com/SwerveDriveSpecialties/swerve-lib/blob/f6f4de65808d468ed01cc5ca39bf322383838fcd/src/main/java/com/swervedrivespecialties/swervelib/SdsModuleConfigurations.java#L19
    Order: wheelDiameter, driveDreuction, driveInverted, steerReduction, steerInverted
    """
    wheelDiameter: float = 0.10033
    driveReduction: float = (14.0 / 50.0) * (27.0 / 17.0) * (15.0 / 45.0)
    steerReduction: float = (14.0 / 50.0) * (10.0 / 60.0)

    drivePositionConversionFactor : float = math.pi * wheelDiameter * driveReduction / SwerveModuleMk4iConsts.kTicksPerRotation
    driveVelocityConversionFactor: float = drivePositionConversionFactor * 10.0
    steerPositionConversionFactor: float = 2.0 * math.pi / SwerveModuleMk4iConsts.kTicksPerRotation * steerReduction
    steerVelocityConversionFactor: float = steerPositionConversionFactor * 10.0

    moduleType: str = "Mk4I_L2"
