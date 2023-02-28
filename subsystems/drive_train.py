import commands2, rev, wpilib, wpilib.drive, constants

class DriveTrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.front_right = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushed)
        self.back_left = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushed)
        self.back_right = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushed)
        self.front_left = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushed)

        left_side = wpilib.MotorControllerGroup(self.front_left, self.back_left)
        right_side = wpilib.MotorControllerGroup(self.front_right, self.back_right)
        self.drive = wpilib.drive.DifferentialDrive(left_side, right_side)

    def move(self, forward_speed, rotation_speed):
        self.drive.arcadeDrive(rotation_speed, -forward_speed)
    
