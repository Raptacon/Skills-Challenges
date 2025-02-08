from photonlibpy import PhotonCamera, PhotonPoseEstimator, PoseStrategy
from photonlibpy.targeting.photonTrackedTarget import PhotonTrackedTarget
from photonlibpy.targeting.photonPipelineResult import PhotonPipelineResult
from wpimath.geometry import Pose2d
from robotpy_apriltag import AprilTagField, AprilTagFieldLayout
from config import OperatorRobotConfig
from subsystems.drivetrain.drivetrain import SwerveDrivetrain

class Vision:
    def __init__(self, driveTrain : SwerveDrivetrain):
        self.cam = PhotonCamera("Sparky_Arducam_1")
        self.drive = driveTrain
        self.camPoseEst = PhotonPoseEstimator(
            AprilTagFieldLayout.loadField(AprilTagField.k2025Reefscape),
            PoseStrategy.MULTI_TAG_PNP_ON_COPROCESSOR,
            self.cam,
            OperatorRobotConfig.robotToCam,
        )

    def getResults(self) -> list[PhotonPipelineResult]:
        return self.cam.getAllUnreadResults()
    
    def getCamEstimate(self):
        bestPipeline = self.cam.getLatestResult()
        camEstPose = self.camPoseEst.update(bestPipeline)
        if camEstPose != None:
            self.drive.addVisionPoseEstimate(
                camEstPose.estimatedPose.toPose2d(), camEstPose.timestampSeconds
            )

    def getBestPipeline(self) -> PhotonPipelineResult:
        bestTarget : PhotonPipelineResult = None
        bestArea = 0
        results = self.cam.getAllUnreadResults()
        if len(results) > 0:
            for result in results:
                if result.hasTargets():
                    if(result.getBestTarget().getArea() > bestArea):
                        bestTarget = result
        return bestTarget
    
    def getTargetData(self, target : PhotonTrackedTarget):
        targetID = target.getFiducialId()
        targetYaw = target.getYaw()
        targetPitch = target.getPitch()
        targetSkew = target.getSkew()
        targetArea = target.getArea()

        return targetID, targetYaw, targetPitch, targetSkew, targetArea