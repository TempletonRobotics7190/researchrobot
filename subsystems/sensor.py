import wpilib, commands2

class Sensor(commands2.SubsystemBase):
    def __init__(self, port):
        super().__init__(self)
        self.counter = wpilib.Counter(port)
        self.counter.setMaxPeriod(1.0)
        self.counter.setSemiPeriodMode(True)
        self.counter.reset()
    
    def getDistance(self):
        cm = 0
    
        if self.counter.get() < 1:
            print("LidarLite: waiting for distance measurement")
            return 0
        
        cm = (self.counter.getPeriod() * 1000000.0 / 10.0) - 3 
        return cm
    