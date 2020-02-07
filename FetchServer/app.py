from flask import Flask
from flask_restful import Resource, Api

app = Flask("classroom_ar_scanner_fetch")

if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")
