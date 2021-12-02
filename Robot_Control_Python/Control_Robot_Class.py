import pyfirmata
import time
from math import cos, sin, radians


class RobotArm(object):
    theta0 = 90.0
    theta1 = 90.0
    theta2 = 90.0
    theta3 = 90.0
    theta4 = 65

    board = None
    servo0 = None
    servo1 = None
    servo2 = None
    servo3 = None
    servo4 = None

    timeout = 0.015

    def __init__(self):
        # print("in __init__")
        self.board = pyfirmata.Arduino('COM5')

        self.board.servo_config(9, angle=self.theta0)
        self.servo0 = self.board.get_pin('d:9:s')
        self.servo0.write(self.theta0)

        self.board.servo_config(6, angle=self.theta1)
        self.servo1 = self.board.get_pin('d:6:s')
        self.servo1.write(self.theta1)

        self.board.servo_config(5, angle=self.theta2)
        self.servo2 = self.board.get_pin('d:5:s')
        self.servo2.write(self.theta2)

        self.board.servo_config(3, angle=self.theta3)
        self.servo3 = self.board.get_pin('d:3:s')
        self.servo3.write(self.theta3)

        self.board.servo_config(11, angle=self.theta4)
        self.servo4 = self.board.get_pin('d:11:s')
        self.servo4.write(self.theta4)

    def __del__(self):
        # print("in __del__")
        self.goto(90, 90, 90, 90)
        self.closeHand()
        self.board.exit()

    def set0(self, theta0_desired):
        theta0_desired = max(theta0_desired, 0.0)
        theta0_desired = min(theta0_desired, 180.0)
        while abs(self.theta0 - theta0_desired) > 0.1:
            if self.theta0 <= theta0_desired:
                self.theta0 = self.theta0 + 1.0
            elif self.theta0 > theta0_desired:
                self.theta0 = self.theta0 - 1.0

            self.servo0.write(self.theta0)
            time.sleep(self.timeout)
        # print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2) + "," + str(self.theta3))

    def set1(self, theta1_desired):
        theta1_desired = max(theta1_desired, 0.0)
        theta1_desired = min(theta1_desired, 180.0)
        while abs(self.theta1 - theta1_desired) > 0.1:
            if self.theta1 <= theta1_desired:
                self.theta1 = self.theta1 + 1.0
            elif self.theta1 > theta1_desired:
                self.theta1 = self.theta1 - 1.0

            self.servo1.write(self.theta1)
            time.sleep(self.timeout)
        # print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2) + "," + str(self.theta3))

    def set2(self, theta2_desired):
        theta2_desired = max(theta2_desired, 0.0)
        theta2_desired = min(theta2_desired, 180.0)
        while abs(self.theta2 - theta2_desired) > 0.1:
            if self.theta2 <= theta2_desired:
                self.theta2 = self.theta2 + 1.0
            elif self.theta2 > theta2_desired:
                self.theta2 = self.theta2 - 1.0

            self.servo2.write(self.theta2)
            time.sleep(self.timeout)
        # print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2) + "," + str(self.theta3))

    def set3(self, theta3_desired):
        theta3_desired = max(theta3_desired, 0.0)
        theta3_desired = min(theta3_desired, 180.0)
        while abs(self.theta3 - theta3_desired) > 0.1:
            if self.theta3 <= theta3_desired:
                self.theta3 = self.theta3 + 1.0
            elif self.theta3 > theta3_desired:
                self.theta3 = self.theta3 - 1.0

            self.servo3.write(self.theta3)
            time.sleep(self.timeout)
        # print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2) + "," + str(self.theta3))

    def set4(self, theta4_desired):
        theta4_desired = max(theta4_desired, 30.0)
        theta4_desired = min(theta4_desired, 130.0)
        while abs(self.theta4 - theta4_desired) > 0.1:
            if self.theta4 <= theta4_desired:
                self.theta4 = self.theta4 + 1.0
            elif self.theta4 > theta4_desired:
                self.theta4 = self.theta4 - 1.0

            self.servo4.write(self.theta4)
            time.sleep(self.timeout)

    def goto(self, theta0_desired, theta1_desired, theta2_desired, theta3_desired):
        self.set0(theta0_desired)
        self.set1(theta1_desired)
        self.set2(theta2_desired)
        self.set3(theta3_desired)

        # print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2) + "," + str(self.theta3))
        time.sleep(self.timeout)

    def openHand(self):
        self.set4(30.0)

    def closeHand(self):
        self.set4(90)

    def fk(self, q1, q2, q3):   # TODO: fk is not calculated properly (offset must be configured).
        l1 = 4  # cm
        l2 = 7  # cm
        l3 = 9  # cm
        q1 = radians(q1 - 90)
        q2 = radians(q2 - 90)
        q3 = radians(q3 - 90)
        x = (l2 * sin(q2) + l3 * sin(q2 + q3)) * cos(q1)
        y = (l2 * sin(q2) + l3 * sin(q2 + q3)) * sin(q1)
        z = l1 + (l2 * cos(q2) + l3 * cos(q2 + q3))
        coord = [round(x, 4), round(y, 4), round(z, 4)]
        print("Coordinate TCP: ", coord)
        return coord
