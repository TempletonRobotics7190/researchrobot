import wpilib, commands2

class Shoot(commands2.SequentialCommandGroup):
    def __init__(self, shooter, belt):
        super().__init__()
        self.shooter = shooter
        self.belt = belt
        self.addRequirements(shooter)
        self.addRequirements(belt)
        self.timer = wpilib.Timer()
        self.timer.start()
    
    def initialize(self):
        self.timer.reset()
    
    def execute(self):
        self.shooter.start()
        if self.timer.get() > 2:
            self.belt.start()
        
    def end(self, _):
        self.shooter.stop()
        self.belt.stop()
            
    
