import wpilib, commands2
import constants

class Stabilize(commands2.CommandBase):
    def __init__(self, drive_train, gyroscope):
        super().__init__()
        self.drive_train = drive_train
        self.addRequirements(drive_train)
        self.gyroscope = gyroscope

    def execute(self):
        gyro_y = round(self.gyroscope.getGyroAngleY())
        gyro_z= round(self.gyroscope.getGyroAngleZ())

        forward_speed = self._calc_speed(gyro_y, 
        constants.STABILIZE_ACCURACY_RANGE_Y)

        rotation_speed = self._calc_speed(gyro_z, 
        constants.STABILIZE_ACCURACY_RANGE_Z)

        self.drive_train.move(forward_speed, rotation_speed)
        
    def _calc_speed(self, angle, accuracy_range):
        if angle > accuracy_range:
            return -.6          
        if angle < -accuracy_range:
            return .6

        return 0