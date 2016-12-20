import RPi.GPIO as GPIO

# Sonar PINS
LED = 40
TRIG = 36
ECHO = 38

# Left Motor PINS
leftSoftPWM = 11
leftStepPinForward = 13
leftStepPinBackward = 15

# Right Motor PINS
rightSoftPWM = 22
rightStepPinForward = 24
rightStepPinBackward = 26

# Left Motor Encoder PIN
leftMotorEncoderOut = 19

# Right Motor Encoder PIN
rightMotorEncoderOut = 16      

# Motor Encoder PINS

# GPIO Setup
GPIO.setmode(GPIO.BOARD)

# LED
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 0)

# SONAR
GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

# LEFT MOTOR
GPIO.setup(leftStepPinForward, GPIO.OUT)
GPIO.setup(leftStepPinBackward, GPIO.OUT)

# RIGHT MOTOR
GPIO.setup(rightStepPinForward, GPIO.OUT)
GPIO.setup(rightStepPinBackward, GPIO.OUT)

# LEFT MOTOR PWM
GPIO.setup(leftSoftPWM, GPIO.OUT)
leftp = GPIO.PWM(leftSoftPWM, 50)

# RIGHT MOTOR PWM
GPIO.setup(rightSoftPWM, GPIO.OUT)
rightp = GPIO.PWM(rightSoftPWM, 50)

# Left Motor Encoder
# setup done when necessary
GPIO.setup(leftMotorEncoderOut, GPIO.IN)
# GPIO.setup(leftMotorEncoderOut, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Right Motor Encoder
GPIO.setup(rightMotorEncoderOut, GPIO.IN)
# GPIO.setup(rightMotorEncoderOut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# setup done when necessary
