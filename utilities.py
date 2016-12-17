# defines and setups the GPIO pins
from GPIO_pinouts import *

# necessary parameters defined here
import parameters
import time
# INITIALIZATION OF PARAMETER
parameters.init()

# FUNCTIONS


def leftMotorForward(dc=100):
    leftp.ChangeDutyCycle(dc)
    GPIO.output(leftStepPinForward, GPIO.HIGH)
    GPIO.output(leftStepPinBackward, GPIO.LOW)


def leftMotorStop():
    GPIO.output(leftStepPinForward, GPIO.LOW)
    GPIO.output(leftStepPinBackward, GPIO.LOW)


def leftMotorBackward(dc=100):
    leftp.ChangeDutyCycle(dc)
    GPIO.output(leftStepPinForward, GPIO.LOW)
    GPIO.output(leftStepPinBackward, GPIO.HIGH)


def rightMotorForward(dc=100):
    rightp.ChangeDutyCycle(dc)
    GPIO.output(rightStepPinForward, GPIO.HIGH)
    GPIO.output(rightStepPinBackward, GPIO.LOW)


def rightMotorStop():
    GPIO.output(rightStepPinForward, GPIO.LOW)
    GPIO.output(rightStepPinBackward, GPIO.LOW)


def rightMotorBackward(dc=100):
    rightp.ChangeDutyCycle(dc)
    GPIO.output(rightStepPinForward, GPIO.LOW)
    GPIO.output(rightStepPinBackward, GPIO.HIGH)


def forward():
    leftMotorForward(parameters.left_motor_dc)
    rightMotorForward(parameters.right_motor_dc)


def backward():
    leftMotorBackward(parameters.left_motor_dc)
    rightMotorBackward(parameters.right_motor_dc)

def turnLeft():
    leftMotorStop()
    rightMotorForward(parameters.turn_dc)

def turnRight():
    rightMotorStop()
    leftMotorForward(parameters.turn_dc)
    
def rightRotate():
    turnRight()
    time.sleep(0.58)

def leftRotate():
    turnLeft()
    time.sleep(0.5)

def forwardAdjust(right_motor_dc, left_motor_dc, count):
    print("R_DC = " + str(right_motor_dc) + " L_DC = " + str(left_motor_dc))
    # Forward Moving Adjustment based on duty cycle
    count += 1
    if count % 3 == 0:
        right_motor_dc += 0.76
    elif count % 1 == 0:
        right_motor_dc -= 0.38
    return right_motor_dc, left_motor_dc, count
    
def avoidObstacle():
    rightRotate()
    forward()
    time.sleep(2)
    leftRotate()
    forward()
    time.sleep(2)
    leftRotate()
    forward()
    time.sleep(2)
    rightRotate()
    forward()
    time.sleep(2)

def getSonarDistance():
    # Give Trigger pulse
    GPIO.output(TRIG, 1)
    time.sleep(.00001)
    GPIO.output(TRIG, 0)

    # Wait for device to send sound
    while GPIO.input(ECHO) == 0:
        pass

    sonar_echo_send_time = time.time()
    # Wait for echo
    while GPIO.input(ECHO) == 1:
        pass
    sonar_echo_recieve_time = time.time()

    dist = (sonar_echo_recieve_time - sonar_echo_send_time) * 17000;
    print(dist)
    return dist

