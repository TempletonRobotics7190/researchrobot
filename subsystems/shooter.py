import wpilib, wpilib.drive, ctre, commands2

class Shooter(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.big_motor = wpilib.Spark(0)
        self.small_motor = wpilib.Spark(1)
    
    def start(self):
        self.big_motor.set(-.55)
        self.small_motor.set(-.55)
    
    def stop(self):
        self.big_motor.set(0)
        self.small_motor.set(0)