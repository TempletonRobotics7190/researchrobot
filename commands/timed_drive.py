import wpilib, commands2

class TimedDrive(commands2.CommandBase):
    def __init__(self, forward_speed, rotation_speed,
     seconds, drive_train):
        super().__init__()
        self.forward_speed = forward_speed
        self.rotation_speed = rotation_speed
        self.seconds = seconds
        self.drive_train = drive_train
        self.timer = wpilib.Timer()
        self.addRequirements(drive_train)

    def initialize(self):
        self.timer.start()
    
    def execute(self):
        self.drive_train.move(self.forward_speed, self.rotation_speed)
    
    def end(self, interupted):
        self.drive_train.stop()
    
    def isFinished(self) -> bool:
        return self.timer.get() > self.seconds
