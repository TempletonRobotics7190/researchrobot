import commands2, ctre, wpilib, wpilib.drive

class DriveTrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.front_right = ctre.WPI_VictorSPX(1)
        self.back_left = ctre.WPI_VictorSPX(2)
        self.back_right = ctre.WPI_VictorSPX(3)
        self.front_left = ctre.WPI_VictorSPX(4)

        left_side = wpilib.MotorControllerGroup(self.front_left, self.back_left)
        right_side = wpilib.MotorControllerGroup(self.front_right, self.back_right)
        self.drive = wpilib.drive.DifferentialDrive(left_side, right_side)

    def move(self, forward_speed, rotation_speed):
        self.drive.arcadeDrive(rotation_speed, -forward_speed)
    
