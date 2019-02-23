from flask import Flask,send_file
import picamera
from GetStaticUrl import GetStaticUrl
from GetStaticUrl import GetStaticUrl
import time


app = Flask(__name__)

@app.route("/capture/")
def capture_visitor():
		
	print("About to take a picture.")
	
	with picamera.PiCamera() as camera:
		#camera.resolution = (1280,720)
		filename = "/home/pi/Desktop/newimage.jpg"
		camera.capture(filename)
		
	print("Picture taken.")
	return send_file(filename, mimetype='image/jpg')

@app.route("/")
def home():
	return "home"
	
@app.route("/unlock/")
def Unlock_door():
	return "unlock api"

if __name__ == '__main__':
    
	app.run()
