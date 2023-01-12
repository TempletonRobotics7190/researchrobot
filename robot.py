
import wpilib
import wpilib.drive
import ctre
import sensor

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.front_right = ctre.WPI_VictorSPX(1)
        self.back_left = ctre.WPI_VictorSPX(2)
        self.back_right = ctre.WPI_VictorSPX(3)
        self.front_left = ctre.WPI_VictorSPX(4)

        left_side = wpilib.MotorControllerGroup(self.front_left, self.back_left)
        right_side = wpilib.MotorControllerGroup(self.front_right, self.back_right)
        self.drive = wpilib.drive.DifferentialDrive(left_side, right_side)

        self.stick = wpilib.Joystick(0)
        self.sensor = sensor.Sensor(0)

        self.timer = wpilib.Timer()
        self.timer.start()

    def teleopPeriodic(self):
        self.drive.arcadeDrive(
            self.stick.getRawAxis(0), -self.stick.getRawAxis(1)
        )
    
        
    def autonomousInit(self):
        self.timer.reset()

    def autonomousPeriodic(self):
        if self.sensor.get_distance() > 100:
            self.drive.arcadeDrive(-.3, -0.5)
        else:
            self.drive.arcadeDrive(0 , 0)
        
       
wpilib.run(MyRobot)