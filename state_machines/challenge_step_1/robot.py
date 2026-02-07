import wpilib
from wpilib import SmartDashboard, Field2d
import ntcore
import photonlibpy
from robotpy_apriltag import AprilTagFieldLayout, AprilTagField
from typing import Callable
import wpimath
from wpimath.geometry import Pose2d, Rotation2d
import math

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
        self.yawservo = wpilib.Servo(0)
        self.pitchservo = wpilib.Servo(1)
        self.yawservo_pos = 0.5
        self.pitchservo_pos = 0.5
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
        self.controller = wpilib.XboxController(0)
        self.x = 0.0
        self.y = 0.0
        self.heading = 0.0
        self.maxSpeed = 3.0      # m/s
        self.maxTurn = 2.5       # rad/s
        self.lastTime = wpilib.Timer.getFPGATimestamp()

    def teleopPeriodic(self):
        targetYaw = 0.0
        targetPitch = 0.0
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
                targetYaw = math.atan(target_pose.Y()/target_pose.X()) / 2 /math.pi
                
        #print(self.target_pose.Y())
        #print("x =" + str(self.target_pose.X()))
        #print("\n")

        #if abs(targetYaw) < 0.007: #eliminates overcorrection
        #   targetYaw = 0.0
        #if abs(targetPitch) < 0.007:
        #   targetPitch = 0.0
        
        self.yawservo_pos += targetYaw
        self.pitchservo_pos += targetPitch
        self.yawservo.set(self.yawservo_pos)
        self.pitchservo.set(self.pitchservo_pos)

        #field stuff
        #self.field.setRobotPose(self.odometry.getPose())

        # #controller stuff
        # now = wpilib.Timer.getFPGATimestamp()
        # dt = now - self.lastTime
        # self.lastTime = now

        # forward = -self.controller.getLeftY() * self.maxSpeed
        # turn = -self.controller.getRightX() * self.maxTurn

        # self.heading += turn * dt

        # self.x += forward * math.cos(self.heading) * dt
        # self.y += forward * math.sin(self.heading) * dt

        # self.field.setRobotPose(
        #     Pose2d(self.x, self.y, Rotation2d(self.heading))
        # )
