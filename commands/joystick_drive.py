import commands2, wpilib

class JoystickDrive(commands2.CommandBase):
    def __init__(self, drive_train):
        super().__init__()
        self.drive_train = drive_train
        self.joystick = wpilib.Joystick(0)
        self.addRequirements(drive_train)

    def execute(self):
        self.drive_train.move(
            -self.joystick.getRawAxis(1), self.joystick.getRawAxis(0)
        )
   
