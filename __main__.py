# Import required libraries

import RTIMU
import time
import socket
import numpy as np

# necessary functions defined here
from utilities import *

##################### Starting communication with mpu via I2C ##########################

IMU_IP = "127.0.0.2"
IMU_PORT = 5005

SETTINGS_FILE = "RTIMULib"

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

if not imu.IMUInit():
    imu_sentence = "$IIXDR,IMU_FAILED_TO_INITIALIZE*7C"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(imu_sentence, (IMU_IP, IMU_PORT))

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)


###########################################################


############ Robot Run Start From Here ####################

def main():
    count = 0
    leftp.start(0)
    rightp.start(0)

    firstReadTime = time.time()
    yaw_values = list()
    while time.time() - firstReadTime < 2:
        acc_x, acc_y, yaw, yawrate = mpuRead(imu)
        yaw_values.append(yaw)
    ideal_yaw = np.mean(yaw_values)

    forward()

    # acc_x, acc_y, yaw, yawrate = mpuRead(imu)
    # adjusting at start
    # forwardAdjust(yaw, yawrate)

    past_yaw_error = 0.0
    past_mpuReadTime = None

    try:
        while True:
            measurement_start_time = time.time()

            '''
            sonar_distance = getSonarDistance()
            '''

            mpuReadTime = time.time()
            acc_x, acc_y, yaw, yawrate = mpuRead(imu)
            yaw_error = yaw - ideal_yaw

            if past_mpuReadTime == None:
                yaw_error_derivative = 0.0
            else:
                yaw_error_derivative = (yaw_error - past_yaw_error) / (mpuReadTime - past_mpuReadTime)

            if False:
                # if sonar_distance < min_obstacle_distance:
                print("Obstacle Ahead!!!")
                GPIO.output(LED, 1)
                turnRight()
            else:
                GPIO.output(LED, 0)
                # parameters.right_motor_dc, parameters.left_motor_dc, count = forwardAdjust(yaw, yawrate, parameters.right_motor_dc, parameters.left_motor_dc, count)
                forwardAdjust(yaw_error)
                # forwardAdjustPD(yaw_error, yaw_error_derivative)
                forward()

            past_yaw_error = yaw_error
            past_mpuReadTime = mpuReadTime

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
