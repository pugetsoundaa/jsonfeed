from flask import Flask
from datatojson import datatojson

app = Flask(__name__)

@app.route("/")
def main():
	file = open("meetingdata.json", "w")
	file.write(datatojson())
	return "One step at a time my friend :)"