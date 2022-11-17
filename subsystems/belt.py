import wpilib, wpilib.drive, ctre, commands2

class Belt(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.motor = wpilib.PWMSparkMax(3)
    
    def start(self):
        self.motor.set(0.4)
    
    def stop(self):
        self.motor.set(0)