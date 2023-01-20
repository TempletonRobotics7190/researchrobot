import wpilib, commands2

class ExampleAuto(commands2.CommandBase):
    def __init__(self, drive_train):
        super().__init__()
        self.drive_train = drive_train
        self.addRequirements(drive_train)
    
    def execute(self) -> None:
        self.drive_train.move(.5, 0)