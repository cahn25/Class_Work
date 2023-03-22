from motor import Motor
from motor_controller import MotorControllerGroup

if __name__ == "__main__":
    motor1 = Motor()
    motor2 = Motor()
    motor3 = Motor()
    motor_group = MotorControllerGroup(motor1, motor2, motor3)