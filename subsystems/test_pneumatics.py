import wpilib, commands2

class TestPneumatics(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.solenoid1 = wpilib.Solenoid(7,wpilib.PneumaticsModuleType.REVPH,8)
        self.solenoid2 = wpilib.Solenoid(7,wpilib.PneumaticsModuleType.REVPH,9)

    def open1(self):
        self.solenoid1.set(True)
    
    def close1(self):
        self.solenoid1.set(False)
            
    def open2(self):
        self.solenoid2.set(True)
    
    def close2(self):
        self.solenoid2.set(False)