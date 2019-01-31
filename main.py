from flask import Flask
from datatojson import datatojson


app = Flask(__name__)

@app.route("/")
def main():
	return datatojson()