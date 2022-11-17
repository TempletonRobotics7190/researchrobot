import wpilib, wpilib.drive, ctre, commands2

class Intake(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.motor = wpilib.PWMSparkMax(2)
    
    def start(self):
        self.motor.set(0.5)
    
    def stop(self):
        self.motor.set(0)