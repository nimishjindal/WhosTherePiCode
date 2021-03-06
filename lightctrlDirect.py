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
	def blink(self,times = 1):
		for _ in range(times):
			self.TurnOn()
			time.sleep(1)
			self.TurnOff()
			time.sleep(1)

if __name__ == "__main__":			
	led = gpio(18)
	led.blink(2)
	#time.sleep(1)