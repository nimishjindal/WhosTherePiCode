from flask import Flask,send_file
import picamera
from GetStaticUrl import GetStaticUrl
from GetStaticUrl import GetStaticUrl
import time
import boto3
from config import awsCreds as creds
from uploadURL import uploadurl
from config import STATUS_LED_PIN
from lightctrlDirect import gpio

app = Flask(__name__)

@app.route("/capture/")
def capture_visitor():
		
	try:
		filename = "target.JPG"
		bucket_name = "alexaguestentry"
		
		print("About to take a picture.")
		
		with picamera.PiCamera() as camera:
			#camera.resolution = (320,240)
			camera.capture("/home/pi/Desktop/"+filename)
			
		print("Picture taken.")
		
		session = boto3.Session(aws_access_key_id = creds["AWS_SERVER_PUBLIC_KEY"], aws_secret_access_key = creds["AWS_SERVER_SECRET_KEY"])
		s3 = session.resource('s3')

		s3.meta.client.upload_file("/home/pi/Desktop/"+filename, bucket_name, filename)
		
		return filename
	except Exception as e:
		return str(e)

@app.route("/")
def home():
	return "home"
	
@app.route("/unlock/")
def Unlock_door():
	return "unlock api"

if __name__ == '__main__':
	
	statusLED = gpio(STATUS_LED_PIN)
	if uploadurl():	
		app.run()
		statusLED.TurnOn()
	else:
		print("error")
		statusLED.blink()
		
