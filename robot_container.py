import wpilib, constants, commands2
import commands, subsystems

class RobotContainer:
    def __init__(self):
        self.joystick = wpilib.Joystick(0)

        # The robot's subsystems
        self.drive_train = subsystems.DriveTrain()

        # Autonomous routine
        self.autonomous = commands.Autonomous(self.drive_train)

        self.configureButtonBindings()

        # set up default drive command
        self.drive_train.setDefaultCommand(
            commands.JoystickDrive(self.joystick, self.drive_train)
        )

    def configureButtonBindings(self):
        pass
        # commands2.button.JoystickButton(self.joystick, 1).whenPressed(
        #     GrabHatch(self.hatch)
        # )

        # commands2.button.JoystickButton(self.driverController, 2).whenPressed(
        #     ReleaseHatch(self.hatch)
        # )

        # commands2.button.JoystickButton(self.driverController, 3).whenHeld(
        #     HalveDriveSpeed(self.drive)
        # )

    def getAutonomousCommand(self):
        return self.autonomous