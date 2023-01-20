import wpilib,commands2

class ExamplePneumatics(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.solenoid = wpilib.Solenoid(0,wpilib.PneumaticsModuleType.CTREPCM,7)
    
    def release(self):
        self.solenoid.set(True)
    
    def retract(self):
        self.solenoid.set(False)