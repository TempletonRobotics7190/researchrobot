import wpilib


class Sensor:
    def __init__(self, port):
        self.counter = wpilib.Counter(port)
        self.counter.setMaxPeriod(1.0)
        self.counter.setSemiPeriodMode(True)
        self.counter.reset()
    
    def get_distance(self):
        cm = 0
    
        if self.counter.get() < 1:
            print("LidarLite: waiting for distance measurement")
            return 0
        
        cm = (self.counter.getPeriod() * 1000000.0 / 10.0) - 3 
        return cm
    