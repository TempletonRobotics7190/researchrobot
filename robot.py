import wpilib


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.front_left_motor = wpilib.PWMSparkMax()
        self.front_right_motor = wpilib.PWMSparkMax()
        self.back_left_motor = wpilib.PWMSparkMax()
        self.back_right_motor = wpilib.PWMSparkMax()

        self.left_side = wpilib.MotorControllerGroup(self.front_left_motor, self.back_left_motor)
        self.right_side = wpilib.MotorControllerGroup(self.front_right_motor, self.back_right_motor)

        self.drive = wpilib.drive.DifferentialDrive(self.left_side, self.right_side)


wpilib.run(Robot)