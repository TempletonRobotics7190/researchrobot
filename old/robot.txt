import wpilib
import wpilib.drive
import ctre
import sensors

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.front_right = ctre.WPI_VictorSPX(1)
        self.back_left = ctre.WPI_VictorSPX(2)
        self.back_right = ctre.WPI_VictorSPX(3)
        self.front_left = ctre.WPI_VictorSPX(4)

        left_side = wpilib.MotorControllerGroup(self.front_left, self.back_left)
        right_side = wpilib.MotorControllerGroup(self.front_right, self.back_right)
        self.drive = wpilib.drive.DifferentialDrive(left_side, right_side)

        self.stick = wpilib.Joystick(0)

        self.laser_sensor = sensors.LaserSensor(0)
        self.gyro = wpilib.ADIS16448_IMU()

        self.timer = wpilib.Timer()
        self.timer.start()

        self.dashboard = wpilib.SmartDashboard
        self.auto_chooser = wpilib.SendableChooser()
        self.auto_chooser.setDefaultOption("default Auto", "default")
        self.auto_chooser.addOption("My Auto", "Custom")
        self.dashboard.putData("Auto choices", self.auto_chooser)
        self.auto_selected = None
    
    def robotPeriodic(self):
        self.dashboard.putNumber("Gyroscope Y Axis", round(self.gyro.getGyroAngleY()))
        self.dashboard.putNumber("Laser Sensor Distance", round(self.laser_sensor.get_distance()))

    def teleopPeriodic(self):
        self.drive.arcadeDrive(
            self.stick.getRawAxis(0), -self.stick.getRawAxis(1)
        )
    
    def autonomousInit(self):
        self.timer.reset()
        self.auto_selected = self.auto_chooser.getSelected()

    def autonomousPeriodic(self):
        if self.auto_selected == "default":
            if self.laser_sensor.get_distance() > 100:
                self.drive.arcadeDrive(.3, 0.5)
            else:
                self.drive.arcadeDrive(0 , 0)
        else:
            self.drive.arcadeDrive(0.0, -.5)
        
       
wpilib.run(Robot)