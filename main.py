from flask import Flask
from datatojson import datatojson
from commitjson import commitjson

app = Flask(__name__)

@app.route("/")
def main():
	file = open("meetingdata/meetingdata.json", "w")
	file.write(datatojson())
	#commitjson()
	return "One Heroku step at a time my friend :)"