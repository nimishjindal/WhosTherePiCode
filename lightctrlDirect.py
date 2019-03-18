# flask_ngrok_example.py
from flask import Flask
from flask_ngrok import run_with_ngrok
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def hello():

	ledpin = 13

	try:
		connection = SerialManager()
		a = ArduinoApi(connection = connection)

	except Exception as e:
		print("failed connection")
		return str(e)


	a.pinMode(ledpin, a.OUTPUT)

	try:
		while _ in range(3):
			a.digitalWrite(ledpin, a.HIGH)
			print("on")

			sleep(1)

			a.digitalWrite(ledpin, a.LOW)
			print("off")

			sleep(1)
	except:
		a.digitalWrite(ledpin, a.LOW)

	return "done LEDs 3 times"

if __name__ == '__main__':
    app.run()