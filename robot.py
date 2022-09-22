import wpilib
import wpilib.drive
import ctre

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.back_left = ctre.WPI_VictorSPX(9)
        self.front_right = ctre.WPI_VictorSPX(10)
        self.back_right = ctre.WPI_VictorSPX(8)
        self.front_left = ctre.WPI_VictorSPX(7)

        left_side = wpilib.MotorControllerGroup(self.front_left, self.back_left)
        right_side = wpilib.MotorControllerGroup(self.front_right, self.back_right)
        self.myRobot = wpilib.drive.DifferentialDrive(left_side, right_side)

        self.stick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.myRobot.arcadeDrive(
            self.stick.getRawAxis(0), -self.stick.getRawAxis(1)
        )

    
wpilib.run(Robot)