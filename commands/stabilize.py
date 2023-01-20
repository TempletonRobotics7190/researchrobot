import wpilib, commands2

class Stabilize(commands2.CommandBase):
    def __init__(self, drive_train, gyroscope):
        super().__init__()
        self.drive_train = drive_train
        self.addRequirements(drive_train)
        self.gyroscope = gyroscope

    def execute(self):
        gyroY = round(self.gyroscope.getGyroAngleY())
        gyroZ = round(self.gyroscope.getGyroAngleZ())

        goodnesspoint = 5
        movement = self._calc_movement(gyroY, goodnesspoint)
        rot = self._calc_movement(gyroZ, goodnesspoint)
        self.drive_train.move(movement, rot)
        
    def _calc_movement(self, angle, goodnesspoint):
        if angle > goodnesspoint :
            return -.6          
        if angle < -goodnesspoint:
            return .6

        return 0