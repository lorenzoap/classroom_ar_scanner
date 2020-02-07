from flask import Flask

app = Flask("classroom_ar_scanner")

@app.route("/")
def test():
	return "Se vedi questo messaggio, il server funziona!"

if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")
