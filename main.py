from flask import Flask
from datatojson import datatojson
from commitjson import commitjson

app = Flask(__name__)

@app.route("/")
def main():
	file = open("meetingdata/meetingdata.json", "w")
	file.write(datatojson())
	file.close()
	#commitjson()

	#heroku test of file writing
	with open("meetingdata/meetingdata.json", "rb") as myfile:
		data_to_read = myfile.read()

	return data_to_read