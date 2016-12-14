def init():
    global min_obstacle_distance
    
    global left_motor_dc
    global right_motor_dc
    
    global turn_dc
    global lowest_dc
    
    global measurement_interval
    
    global yawRateThreshold
    global yawRateFactor
    
    min_obstacle_distance = 40
    
    left_motor_dc = 100
    right_motor_dc = 77.3
    
    turn_dc = 75
    lowest_dc = 70
    
    measurement_interval = 0.015
    
    yawRateThreshold = 0.05
    yawRateFactor = 2
