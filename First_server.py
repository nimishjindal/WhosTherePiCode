# flask_ngrok_example.py
from flask import Flask
from flask_ngrok import run_with_ngrok
import picamera


app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def hello():
		
	# Setup the camera such that it closes
	# when we are done with it.
	print("About to take a picture.")
	with picamera.PiCamera() as camera:
		camera.resolution = (1280,720)
		filename = "/home/pi/Desktop/newimage.jpg"
		camera.capture(filename)
		
	print("Picture taken.")
	
	return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
