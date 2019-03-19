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
	
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNo,GPIO.OUT)

pwm=GPIO.PWM(pinNo, 50)
pwm.start(7.5)
pwm.ChangeDutyCycle(7.5)
sleep(5)
pwm.ChangeDutyCycle(2.5)
sleep(5)

#SetAngle(90) 
pwm.stop()
GPIO.cleanup()

	