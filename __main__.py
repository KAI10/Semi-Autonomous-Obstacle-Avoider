# necessary functions defined here
from utilities import *
import threading

global leftMotorEncoderTicks
global rightMotorEncoderTicks

global leftTimeLog
global rightTimeLog

global currentMode

############ Robot Run Start From Here ####################

def mode_switch():
    global currentMode
    currentMode = "Auto"
    while True:
        command = raw_input()
        if command == 's':
            stop()
            GPIO.cleanup()
            exit()
        if command == 'm':
            currentMode = "Manual"
            stop()
        elif command == "a":
            currentMode = "Auto"
        elif currentMode == "Manual":
            if command == "i":
                forward()
            elif command == "k":
                backward()
            elif command == "j":
                leftRotate()
            elif command == "l":
                rightRotate()
        
        if currentMode == "Auto":
            time.sleep(0.5) 
        time.sleep(0.25)
        stop()    
    

def main():
    
    manual_thread = threading.Thread(target = mode_switch)
    manual_thread.start()
    
    #currentMode = "Auto"
    count = 0
    leftp.start(0)
    rightp.start(0)
    time.sleep(0.1)

    #forward()
    start_time = time.time()
    velocityList = []
    try:
        while True:
            if currentMode == "Auto":
                sonar_distance = getSonarDistance()
                #sonar_distance_2 = getSonarDistance()
                #sonar_distance = (sonar_distance_1 + sonar_distance_2)/2.0
                
                #leftMotorRPS, rightMotorRPS = sampleMotorEncoders()
                #velocityList.append((leftMotorRPS+rightMotorRPS))
                #if False:
                if sonar_distance < parameters.min_obstacle_distance and sonar_distance >= 10:
                    print("Obstacle Ahead!!!")
                    GPIO.output(LED, 1)
                    avoidObstacle()
                else:
                    GPIO.output(LED, 0)
                    # parameters.right_motor_dc, parameters.left_motor_dc, count = forwardAdjust(parameters.right_motor_dc, parameters.left_motor_dc, count)
                    forward()
                    #adjustSpeed(rightMotorRPS, leftMotorRPS)
                    #forward()
                    #time.sleep(0.8)
                    #rightRotate()
                    #forward()
                    #time.sleep(0.8)
                    #leftRotate()
                    #forward()
                    #time.sleep(2)
                    #leftRotate()
                    #forward()
                    #time.sleep(0.8)
                    #rightRotate()
                    #forward()
                    #time.sleep(0.8)
                    
                
                #print ""+str(leftMotorRPS) + " " + str(rightMotorRPS)
        else:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        end_time = time.time()
        avg_v = sum(velocityList)/len(velocityList)
        avg_v *= 3.1416*6.5
        print "Time = " + str(end_time - start_time)
        print "Dist = " + str((end_time - start_time)*avg_v)
        pass

if __name__ == "__main__":
    main()
    GPIO.cleanup()

######################################################################
