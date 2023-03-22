from motor import Motor

class MotorControllerGroup:
    def __init__(self, listofmotor:list[Motor], listofmotors=None):
        self.motors = listofmotors

    def set_speed(self, speed):
        for motor in self.motors:
            motor.set_speed(speed)

    def speedup(self):
        for bob in self.motors:
            bob.speed_up()

    def slow_down(self):
        for jill in self.motors:
            jill.slow_down()

    def add_Motor(self, motor:Motor): #: says what kind of variable the 1 is
        self.motors.append(motor) # append adds a value to the end of a list (whatever is in the parenthesis)

