from flask import Flask
from datatojson import datatojson
from commitjson import commitjson

app = Flask(__name__)

@app.route("/")
def main():
	file = open("meetingdatatest/meetingdata.json", "w")
	file.write(datatojson())
	file.close()
	#commitjson()

	return "Success"