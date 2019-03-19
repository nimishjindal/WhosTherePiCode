import RPi.GPIO as GPIO
from time import sleep

pinNo = 2

def SetAngle(angle):
	duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
	sleep(1)
	
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNo,GPIO.OUT)		
pwm=GPIO.PWM(pinNo, 50)

pwm.start(5)

try:
    while True:
		"""
        pwm.ChangeDutyCycle(7.5)  # turn towards 90 degree
        sleep(1) # sleep 1 second
        pwm.ChangeDutyCycle(2.5)  # turn towards 0 degree
        sleep(1) # sleep 1 second
        pwm.ChangeDutyCycle(12.5) # turn towards 180 degree
        sleep(1) # sleep 1 second 
		"""
		SetAngle(90)
		setAngle(0)
		setAngle(180)
		
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
