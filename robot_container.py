
import commands2, commands2.button, wpilib

import subsystems, commands, constants


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        # Subsystems
        self.drive_train = subsystems.DriveTrain()
        self.drive_train.setDefaultCommand(commands.JoystickDrive(self.drive_train))

        self.test_motor = subsystems.TestMotor()

        self.test_pneumatics = None
        if constants.USE_PNEUMATICS:
            self.test_pneumatics = subsystems.TestPneumatics()
        
        # Other
        #self.gyroscope = wpilib.ADIS16448_IMU()

        self.configureButtonBindings()

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created via the button
        factories on commands2.button.CommandGenericHID or one of its
        subclasses (commands2.button.CommandJoystick or command2.button.CommandXboxController).
        """
        
        command_joystick = commands2.button.CommandJoystick(0)
        side_button = commands2.button.JoystickButton(command_joystick, 2)
        back_button = commands2.button.JoystickButton(command_joystick, 1)

        button_five = commands2.button.JoystickButton(command_joystick, 5)
        button_three = commands2.button.JoystickButton(command_joystick, 3)
        button_five.whenHeld(commands2.StartEndCommand(
            self.test_motor.start,
            self.test_motor.stop
        ))
        button_three.whenHeld(commands2.StartEndCommand(
            self.test_motor.reverse,
            self.test_motor.stop
        ))
        if constants.USE_PNEUMATICS:
            back_button.whenHeld(commands2.StartEndCommand(
                self.test_pneumatics.close1,
                self.test_pneumatics.open1
            ))
            side_button.whenHeld(commands2.StartEndCommand(
                self.test_pneumatics.close2,
                self.test_pneumatics.open2
            ))
        

     
    def getAutonomousCommand(self):
        return None
        # return commands2.SequentialCommandGroup([commands.Stabilize(self.drive_train, self.gyroscope)])

#Andrew was here lmao so was ALEX