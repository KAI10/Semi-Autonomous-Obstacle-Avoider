# Import required libraries

import RTIMU
import time
import socket

# necessary functions defined here
from utilities import *

############ Robot Run Start From Here ####################

def main():
    count = 0
    leftp.start(0)
    rightp.start(0)
    time.sleep(1)
 
    forward()
    try:
        while True:
            '''
            sonar_distance = getSonarDistance()
            '''
            if False:
                # if sonar_distance < min_obstacle_distance:
                print("Obstacle Ahead!!!")
                GPIO.output(LED, 1)
                turnRight()
            else:
                GPIO.output(LED, 0)
                # parameters.right_motor_dc, parameters.left_motor_dc, count = forwardAdjust(parameters.right_motor_dc, parameters.left_motor_dc, count)
                forward()

    except KeyboardInterrupt:
        GPIO.cleanup()
        pass

if __name__ == "__main__":
    main()
    GPIO.cleanup()


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

######################################################################
