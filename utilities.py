# defines and setups the GPIO pins
from GPIO_pinouts import *

# necessary parameters defined here
import parameters
import time
# INITIALIZATION OF PARAMETER
parameters.init()

# FUNCTIONS

######### Motor Functions ####################

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


####### Motor Encoder Functions ###############

def leftMotorEncoderCallBack(channel):
    global leftMotorEncoderTicks
    global leftTimeLog
    leftMotorEncoderTicks += 1
    leftTimeLog.append(time.time())
    #print "left time log appended"

def rightMotorEncoderCallBack(channel):
    global rightMotorEncoderTicks
    global rightTimeLog
    rightMotorEncoderTicks += 1
    rightTimeLog.append(time.time())
    #print "right time log appended"

def sampleMotorEncoders():
    global leftMotorEncoderTicks
    global rightMotorEncoderTicks

    global leftTimeLog
    global rightTimeLog

    leftTimeLog = []
    rightTimeLog = []
    
    leftMotorEncoderTicks = 0
    rightMotorEncoderTicks = 0
    
    
    start_time = time.time()

    # problem possible with variable access (from GPIO_pinouts)
    # setting up for counting pulses
    GPIO.add_event_detect(leftMotorEncoderOut, GPIO.FALLING, callback=leftMotorEncoderCallBack, \
                          bouncetime=parameters.leftMotorEncoderBounceTime)

    GPIO.add_event_detect(rightMotorEncoderOut, GPIO.FALLING, callback=rightMotorEncoderCallBack,\
                          bouncetime=parameters.rightMotorEncoderBounceTime)

    time.sleep(parameters.motorEncoderSampleTime)

    # stop counting pulses
    GPIO.remove_event_detect(leftMotorEncoderOut)
    GPIO.remove_event_detect(rightMotorEncoderOut)

    end_time = time.time()
    duration = end_time - start_time

    leftRPS = (float(leftMotorEncoderTicks)/20)/duration
    rightRPS = (float(rightMotorEncoderTicks)/20)/duration

    # max and min difference between consecutive pulses
    result = [leftTimeLog[i+1] - leftTimeLog[i] for i in range(len(leftTimeLog) - 1)]
    leftTimeLog = result
    result = [rightTimeLog[i+1] - rightTimeLog[i] for i in range(len(rightTimeLog) - 1)]
    rightTimeLog = result
    '''
    print "MaxDiff Left= " + str(max(leftTimeLog))
    print "MinDiff Left= " + str(min(leftTimeLog))
    print "avgDiff Left= " + str(sum(leftTimeLog)/len(leftTimeLog))
    print "MaxDiff Right= " + str(max(rightTimeLog))
    print "MinDiff Right= " + str(min(rightTimeLog))
    print "avgDiff Right= " + str(sum(rightTimeLog)/len(rightTimeLog))
    '''
    #leftRPS = float(1.0/(20*sum(leftTimeLog)/len(leftTimeLog)))
    #rightRPS = float(1.0/(20*sum(rightTimeLog)/len(rightTimeLog)))

    return leftRPS, rightRPS

####### Robot Functions #######################

def forward():
    leftMotorForward(parameters.left_motor_dc)
    rightMotorForward(parameters.right_motor_dc)
    #turnLeft()
    #time.sleep(0.2)
    #turnRight()
    #time.sleep(0.25)
    #stop()
    #time.sleep(0.0000002)

def backward():
    leftMotorBackward(parameters.left_motor_dc)
    rightMotorBackward(parameters.right_motor_dc)

def stop():
    leftMotorStop()
    rightMotorStop()

def turnLeft():
    leftMotorStop()
    rightMotorForward(parameters.turn_dc)

def turnRight():
    rightMotorStop()
    leftMotorForward(parameters.turn_dc)
    
def rightRotate():
    stop()
    time.sleep(0.2)
    turnRight()
    time.sleep(0.98)
    #turnLeft()
    #time.sleep(0.03)
    stop()
    time.sleep(0.1)

def leftRotate():
    stop()
    time.sleep(0.2)
    turnLeft()
    time.sleep(1.02)
    #turnRight()
    #time.sleep(0.05)
    stop()
    time.sleep(0.1)

def forwardAdjust(right_motor_dc, left_motor_dc, count):
    print("R_DC = " + str(right_motor_dc) + " L_DC = " + str(left_motor_dc))
    # Forward Moving Adjustment based on duty cycle
    count += 1
    if count % 3 == 0:
        right_motor_dc += 0.76
    elif count % 1 == 0:
        right_motor_dc -= 0.38
    return right_motor_dc, left_motor_dc, count

def adjustSpeed (right_speed, left_speed):
    speedDiff = right_speed - left_speed
    if speedDiff < -0.015:
        parameters.right_motor_dc += 0.1
    elif speedDiff > 0.015:
         parameters.right_motor_dc -= 0.1
    parameters.right_motor_dc = min(parameters.right_motor_dc, 99.8)
    parameters.right_motor_dc = max(parameters.right_motor_dc, 50) 
    
def avoidObstacle():
    '''
    #  --------->
    rightRotate()
    forward()
    time.sleep(1.5)

    # ^
    # |
    # |
    leftRotate()
    forward()
    time.sleep(1.9)
    
    # <-----------
    leftRotate()
    forward()
    time.sleep(1.3)
    
    # ^
    # |
    # |
    rightRotate()
    forward()
    time.sleep(0.3)
    '''
    stop()
    time.sleep(1)
    backward()
    time.sleep(1)
    leftRotate()
    forward()
    time.sleep(1)
    stop()
    time.sleep(0.02)
    backward()
    time.sleep(0.04)
    rightRotate()
    forward()
    time.sleep(1)
    stop()
    time.sleep(0.02)
    backward()
    time.sleep(0.04)
    rightRotate()
    forward()
    time.sleep(1)
    stop()
    time.sleep(0.02)
    backward()
    time.sleep(0.04)
    leftRotate()
    
    
    

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

