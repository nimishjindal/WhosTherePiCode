import RPi.GPIO as GPIO
from time import sleep

class Servo:
	def __init__(self,pNo):
		self.pinNo = pNo	
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pNo,GPIO.OUT)		
		self.pwm=GPIO.PWM(pNo, 100)
	def __del__(self):
		self.pwm.stop()
		GPIO.cleanup()
	
	def setAngle(self,angle):
		self.pwm.start(5)
		duty = float(angle) / 10.0 + 2.5
		self.pwm.ChangeDutyCycle(duty)
		sleep(1)
		
if __name__ == "__main__":	
	try:
		s = Servo(2)
		while True:
			an = int(input("enter angle"))
			
			s.setAngle(an)
			
			#s.setAngle(90)
			#s.setAngle(0)
			#s.setAngle(180)
				
	except Exception as e:
		del s
		print(e)
		
"""
pwm.ChangeDutyCycle(7.5)  # turn towards 90 degree
sleep(1) # sleep 1 second
pwm.ChangeDutyCycle(2.5)  # turn towards 0 degree
sleep(1) # sleep 1 second
pwm.ChangeDutyCycle(12.5) # turn towards 180 degree
sleep(1) # sleep 1 second 
"""