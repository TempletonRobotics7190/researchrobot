
import wpilib, commands2
from robot_container import RobotContainer


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        self.autonomousCommand = None

        self.container = RobotContainer()

  
    def autonomousInit(self):
        self.autonomousCommand = self.container.getAutonomousCommand()

        # schedule the autonomous command (example)
        if self.autonomousCommand is not None:
            self.autonomousCommand.schedule()
        else:
            print("no auto command?")
   
    def teleopInit(self):
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    
wpilib.run(Robot)