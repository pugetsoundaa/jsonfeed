from flask import Flask, jsonify
from meetingdata import meetingdata


app = Flask(__name__)

@app.route("/")
def main():
	return jsonify(meetingdata())
	