def init():
    global min_obstacle_distance
    
    global left_motor_dc
    global right_motor_dc
    
    global turn_dc
    global lowest_dc

    global motorEncoderSampleTime

    global leftMotorEncoderBounceTime
    global rightMotorEncoderBounceTime
    
    min_obstacle_distance = 50
    
    left_motor_dc = 88
    right_motor_dc = 70
    
    turn_dc = 80
    lowest_dc = 70

    motorEncoderSampleTime = .5

    leftMotorEncoderBounceTime = 20
    rightMotorEncoderBounceTime = 20

