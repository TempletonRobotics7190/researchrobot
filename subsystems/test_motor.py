import rev, commands2

class TestMotor(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.motor = rev.CANSparkMax(5, rev.CANSparkMax.MotorType.kBrushed)

    def start(self):
        self.motor.set(.5)
    
    def reverse(self):
        self.motor.set(-.5)
    
    def stop(self):
        self.motor.set(0)
    