# necessary functions defined here
from utilities import *

global leftMotorEncoderTicks
global rightMotorEncoderTicks

############ Robot Run Start From Here ####################

def main():
    count = 0
    leftp.start(0)
    rightp.start(0)
    time.sleep(1)

    forward()
    start_time = time.time()
    try:
        while True:

            sonar_distance = getSonarDistance()

            # if False:
            if sonar_distance < parameters.min_obstacle_distance:
                print("Obstacle Ahead!!!")
                GPIO.output(LED, 1)
                avoidObstacle()
            else:
                GPIO.output(LED, 0)
                # parameters.right_motor_dc, parameters.left_motor_dc, count = forwardAdjust(parameters.right_motor_dc, parameters.left_motor_dc, count)
                forward()

            leftMotorRPS, rightMotorRPS = sampleMotorEncoders()

    except KeyboardInterrupt:
        GPIO.cleanup()
        end_time = time.time()
        print "Time = " + str(end_time - start_time)
        pass

if __name__ == "__main__":
    main()
    GPIO.cleanup()

######################################################################
