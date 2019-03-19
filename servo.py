import RPi.GPIO as GPIO
from time import sleep

pinNo = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNo,GPIO.OUT)
pwm=GPIO.PWM(pinNo, 50)
pwm.start(0)
SetAngle(90) 
pwm.stop()
GPIO.cleanup()

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(pinNo, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(pinNo, False)
	pwm.ChangeDutyCycle(0)
	

	