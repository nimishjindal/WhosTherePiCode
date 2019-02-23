from flask import Flask,send_file
from GetStaticUrl import GetStaticUrl

app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def home():
	return "home"
	
@app.route("/unlock/")
def Unlock_door():
	return "unlock api"

if __name__ == '__main__':
    
	app.run()