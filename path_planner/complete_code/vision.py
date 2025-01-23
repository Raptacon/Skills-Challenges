from photonlibpy import PhotonCamera, PhotonPoseEstimator, PoseStrategy
from robotpy_apriltag import AprilTagField, AprilTagFieldLayout
from config import OperatorRobotConfig
from subsystems.drivetrain.drivetrain import SwerveDrivetrain

class Vision:
    def __init__(self, driveTrain : SwerveDrivetrain):
        self.cam = PhotonCamera("cam1")
        self.drive = driveTrain
        self.camPoseEst = PhotonPoseEstimator(
            AprilTagFieldLayout.loadField(AprilTagField.kDefaultField),
            PoseStrategy.LOWEST_AMBIGUITY,
            self.cam,
            OperatorRobotConfig.robotToCam,
        )

    def getCamEstimate(self):
        camEstPose = self.camPoseEst.update()
        if camEstPose:
            self.drive.addVisionPoseEstimate(
                camEstPose.estimatedPose, camEstPose.timestampSeconds
            )