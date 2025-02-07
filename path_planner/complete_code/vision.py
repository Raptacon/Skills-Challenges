from photonlibpy import PhotonCamera, PhotonPoseEstimator, PoseStrategy
from photonlibpy.targeting.photonTrackedTarget import PhotonTrackedTarget
from photonlibpy.targeting.photonPipelineResult import PhotonPipelineResult
from robotpy_apriltag import AprilTagField, AprilTagFieldLayout
from config import OperatorRobotConfig
from subsystems.drivetrain.drivetrain import SwerveDrivetrain

class Vision:
    def __init__(self, driveTrain : SwerveDrivetrain):
        self.cam = PhotonCamera("Sparky_Arducam_1")
        self.drive = driveTrain
        self.camPoseEst = PhotonPoseEstimator(
            AprilTagFieldLayout.loadField(AprilTagField.k2025Reefscape),
            PoseStrategy.AVERAGE_BEST_TARGETS,
            self.cam,
            OperatorRobotConfig.robotToCam,
        )

    def getLatestResult(self) -> PhotonPipelineResult:
        return self.cam.getLatestResult()
    
    def getCamEstimate(self):
        camEstPose = self.camPoseEst.update(self.getLatestResult())
        print(camEstPose == None)
        if camEstPose:
            self.drive.addVisionPoseEstimate(
                camEstPose.estimatedPose, camEstPose.timestampSeconds
            )

    def getBestTarget(self) -> PhotonTrackedTarget:
        bestTarget : PhotonTrackedTarget = None
        bestArea = 0

        results = self.cam.getAllUnreadResults()
        if len(results) > 0:
            result = results[-1]
            for target in result.getTargets():
                if target.getArea() >= bestArea:
                    bestTarget = target
        return bestTarget
    
    def getTargetData(self, target : PhotonTrackedTarget):
        targetID = target.getFiducialId()
        targetYaw = target.getYaw()
        targetPitch = target.getPitch()
        targetSkew = target.getSkew()
        targetArea = target.getArea()

        return targetID, targetYaw, targetPitch, targetSkew, targetArea