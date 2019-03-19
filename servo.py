import RPi.GPIO as GPIO
from time import sleep

pinNo = 2

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(pinNo, True)
	pwm.ChangeDutyCycle(duty)
	sleep(7)
	GPIO.output(pinNo, False)
	pwm.ChangeDutyCycle(0)
	

	
dc90 = 7.5
dc0 = 2.5
dc180 = 12.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNo,GPIO.OUT)		
pwm=GPIO.PWM(pinNo, 50)
pwm.start(7.5)

	
def rotate(angle):
	dc = 0

	if angle==90:
		dc = dc90
	elif angle==180:
		dc = dc180
	else:
		dc = 0

	pwm.ChangeDutyCycle(dc)
	sleep(5)
	

rotate(90)
rotate(0)
rotate(90)

pwm.stop()
GPIO.cleanup()

	