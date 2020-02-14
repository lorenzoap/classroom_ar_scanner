from flask import Flask
from flask import render_template

app = Flask("classroom_ar_scanner")

@app.route("/")
def index():
	return render_template("index.html", title="Home")

@app.route("/scan")
def scan():
	return render_template("base.html", title="Scan Classroom")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
