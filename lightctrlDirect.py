import RPi.GPIO as GPIO
import time

class gpio:
	def __init__(self,pinNo):
		self.pin = pinNo
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pinNo,GPIO.OUT)
		GPIO.output(pinNo,GPIO.LOW)
	def __del__(self):
		self.TurnOff()
		GPIO.cleanup()
	def TurnOn(self):
		GPIO.output(self.pin,GPIO.HIGH)
	def TurnOff(self):
		GPIO.output(self.pin,GPIO.LOW)
		

abcd = gpio(18)
abcd.TurnOn()
time.sleep(5)

