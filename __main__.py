# Import required libraries

import RTIMU
import time
import socket

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

    forward()
    #time.sleep(0.1)

    # acc_x, acc_y, yaw, yawrate = mpuRead(imu)
    # adjusting at start
    # forwardAdjust(yaw, yawrate)
    
    try:
        while True:

            # Give Trigger pulse
            GPIO.output(TRIG, 1)
            time.sleep(.00001)
            GPIO.output(TRIG, 0)

            # Wait for device to send sound
            while GPIO.input(ECHO) == 0:
                pass

            start = time.time()
            # Wait for echo
            while GPIO.input(ECHO) == 1:
                pass
            stop = time.time()

            dist = (stop - start) * 17000;
            print(dist)

            acc_x, acc_y, yaw, yawrate = mpuRead(imu)
            #print(acc_x, acc_y, yaw, yawrate)
	    if False:
            # if dist < min_obstacle_distance:
                print("Obstacle Ahead!!!")
                GPIO.output(LED, 1)
                turnRight()
            else:
                GPIO.output(LED, 0)
                parameters.right_motor_dc, parameters.left_motor_dc, count = forwardAdjust(yaw, yawrate, parameters.right_motor_dc, parameters.left_motor_dc, count)
                forward()

            #time.sleep(measurement_interval)

    except KeyboardInterrupt:
        GPIO.cleanup()
        pass


if __name__ == "__main__":
    main()
    GPIO.cleanup()

######################################################################
