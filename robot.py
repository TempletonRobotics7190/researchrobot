import wpilib, commands2, commands2.button

from robot_container import RobotContainer



class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        self.container = RobotContainer()
        self.autonomous_command = self.container.getAutonomousCommand()
        super().robotInit()

    def autonomousInit(self):
        self.autonomous_command.schedule()
        super().autonomousInit()

    def teleopInit(self):
        self.autonomous_command.cancel()
        super().teleopInit()

        

        



if __name__ == "__main__":
    wpilib.run(Robot)