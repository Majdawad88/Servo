# git clone https://github.com/Majdawad88/Servo.git

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
pwmPIN = 18
GPIO.setup(pwmPIN, GPIO.OUT)
pwm = GPIO.PWM(pwmPIN, 50) # GPIO 17 for PWM with 50Hz pwm.start(0) # Initialization

while True:
        pwm.start(0)
        dutyCycle=int(input('Enter Duty Cycle: '))
        if dutyCycle == 2:
                print ("Go to 0 degree")
        elif dutyCycle == 3:
                print ("Go to 18 degree")
        elif dutyCycle == 4:
                print ("Go to 36 degree")
        elif dutyCycle == 5:
                print ("Go to 54 degree")
        elif dutyCycle == 6:
                print ("Go to 72 degree")
        elif dutyCycle == 7:
                print ("Go to 90 degree")
        elif dutyCycle == 8:
                print ("Go to 108 degree")
        elif dutyCycle == 9:
                print ("Go to 126 degree")
        elif dutyCycle == 10:
                print ("Go to 144 degree")
        elif dutyCycle == 11:
                print ("Go to 162 degree")
        elif dutyCycle == 12:
                print ("Go to 180 degree")

        else:
                print("Invalid Entry!")

        pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.1)
