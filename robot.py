import wpilib, commands2

from robot_container import RobotContainer


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        self.container = RobotContainer()
        self.autonomous_command = self.container.getAutonomousCommand()

    def autonomousInit(self):
        self.autonomous_command.schedule()

    def teleopInit(self):
        self.autonomous_command.cancel()

if __name__ == "__main__":
    wpilib.run(Robot)