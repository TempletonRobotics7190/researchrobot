import wpilib, commands2
from commands.timed_drive import TimedDrive

class Autonomous(commands2.SequentialCommandGroup):
    def __init__(self, drive_train):
        self.drive_train = drive_train
        self.addRequirements(drive_train)

        super().__init__([TimedDrive(0.5, 0, 2, drive_train)])

    def execute(self):
        pass

    def isFinished(self):
        pass

    def end(self, interrupted):
        pass
            
        
        