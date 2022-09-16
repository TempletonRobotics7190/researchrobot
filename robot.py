import wpilib
import wpilib.drive


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.front_left_motor = wpilib.PWMSparkMax(1)
        self.front_right_motor = wpilib.PWMSparkMax(2)
        self.back_left_motor = wpilib.PWMSparkMax(0)
        self.back_right_motor = wpilib.PWMSparkMax(3)

        self.left_side = wpilib.MotorControllerGroup(self.front_left_motor, self.back_left_motor)
        self.right_side = wpilib.MotorControllerGroup(self.front_right_motor, self.back_right_motor)

        self.drive = wpilib.drive.DifferentialDrive(self.left_side, self.right_side)
        self.stick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(-self.stick.getRawAxis(0), self.stick.getRawAxis(1))

wpilib.run(Robot)