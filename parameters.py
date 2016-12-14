def init():
    global min_obstacle_distance
    
    global left_motor_dc
    global right_motor_dc
    
    global turn_dc
    global lowest_dc
    
    global measurement_interval
    
    global yawRateThreshold
    global yawRateFactor

    global yawErrorFactor
    global yawErrorDerivativeFactor

    global referenceQPose 
    referenceQPose = (0.99705213, 0.0035882, -0.01229929, -0.07083318)
    
    min_obstacle_distance = 40
    
    left_motor_dc = 100
    right_motor_dc = 77.3
    
    turn_dc = 75
    lowest_dc = 70
    
    measurement_interval = 0.015
    
    yawDiffThreshold = 0.01745
    yawDiffFactor = 5

    yawRateThreshold = 0.05
    yawRateFactor = 2

    yawErrorFactor = 0.1
    yawErrorDerivativeFactor = 0.001
