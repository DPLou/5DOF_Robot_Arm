from Control_Robot_Class import *

robot = RobotArm()
robot.openHand()
robot.goto(90, 20, 180, 90)
robot.closeHand()
robot.goto(90, 90, 180, 90)
robot.goto(180, 90, 180, 90)
robot.openHand()




