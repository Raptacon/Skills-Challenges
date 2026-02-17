import wpilib
from wpilib import SmartDashboard, Field2d
import ntcore
import photonlibpy
from robotpy_apriltag import AprilTagFieldLayout, AprilTagField
from typing import Callable
import wpimath
from wpimath.geometry import Pose2d, Rotation2d
import math
import rev

nt = ntcore.NetworkTableInstance.getDefault()


class MyRobot(wpilib.TimedRobot):
    def robotInit(self): 
        self.counter = nt.getTable("MyRobot").getEntry("Counter")
        self.counter.setInteger(0)
        self.networkTargetX = nt.getTable("MyRobot").getEntry("targetX")
        field = AprilTagFieldLayout.loadField(AprilTagField.kDefaultField)
        kRobotToCam = wpimath.geometry.Transform3d(
            wpimath.geometry.Translation3d(0.0, 0.0, 0.0),
            wpimath.geometry.Rotation3d.fromDegrees(0.0, 0.0, 0.0),
        )
        self.camPoseEst = photonlibpy.PhotonPoseEstimator(field,kRobotToCam,)
        print(nt.getTopics())
        self.camera = photonlibpy.PhotonCamera("Arducam_OV9281_USB_Camera")
        self.target_pose = wpimath.geometry.Pose3d(
            wpimath.geometry.Translation3d(4.625594, 4.034663, 1.8288),
            wpimath.geometry.Rotation3d.fromDegrees(0.0, 0.0, 0.0),
        )
        self.tag_pose = wpimath.geometry.Pose3d(
            wpimath.geometry.Translation3d(5.23, 4.03, 1.12),
            wpimath.geometry.Rotation3d.fromDegrees(0.0, 0.0, 0.0),
        )
        self.field = Field2d()
        SmartDashboard.putData("Field", self.field)
        self.field.getObject("Target").setPose(
            Pose2d(4.655, 4.019, 0.0)
        )



    def teleopPeriodic(self):
        self.counter.setInteger(self.counter.getInteger(0) + 1)
        
        results = self.camera.getAllUnreadResults()
        if len(results) > 0: 
            result = results[-1]  # take the most recent result the camera had
            camEstPose = self.camPoseEst.estimateCoprocMultiTagPose(result)
            if camEstPose is None:
                camEstPose = self.camPoseEst.estimateLowestAmbiguityPose(result)
            if camEstPose is not None:
                target_pose = self.target_pose - camEstPose.estimatedPose
                self.networkTargetX.setFloat(target_pose.X())
