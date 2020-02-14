from flask import Flask
from flask import render_template

app = Flask("classroom_ar_scanner")

@app.route("/")
def test():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
