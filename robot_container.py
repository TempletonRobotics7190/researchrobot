
import commands2, commands2.button, wpilib

import subsystems, commands


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

        # self.example_pneumatics = subsystems.ExamplePneumatics()

        # Other
        self.gyroscope = wpilib.ADIS16448_IMU()
        

        self.configureButtonBindings()

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created via the button
        factories on commands2.button.CommandGenericHID or one of its
        subclasses (commands2.button.CommandJoystick or command2.button.CommandXboxController).
        """
        command_joystick = commands2.button.CommandJoystick(0)
        back_button = commands2.button.JoystickButton(command_joystick, 1)
        # back_button.whenHeld(commands2.StartEndCommand(
        #     self.example_pneumatics.release,
        #     self.example_pneumatics.retract
        # ))

     
    def getAutonomousCommand(self):
        return commands.Stabilize(self.drive_train, self.gyroscope)