from flask import Flask
from flask import redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask("classroom_ar_scanner")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://query:Punk42h2AsaCbzs@db:3306/classroom_timetables"
app.config["SQLALCHEMY_ECHO"] = True # Debug
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Classroom(db.Model):
	__tablename__ = "classroom"
	code = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(16), nullable = False, unique = True)

	def __repr__(self):
		return f"Classroom(code: {self.code}, name: {self.name})"

class SchoolHour(db.Model):
	__tablename__ = "school_hour"
	id = db.Column(db.Integer, primary_key = True)
	classroom_id = db.Column(db.Integer, nullable = False)
	start_time = db.Column(db.Time, nullable = False)
	end_time = db.Column(db.Time, nullable = False)
	teacher = db.Column(db.String(32))
	day = db.Column(db.Date, nullable = False)
	school_subject = db.Column(db.String(32))

	def __repr__(self):
		return f"SchoolHour(id: {self.id}, classroom_id: {self.classroom_id}, start_time: {self.start_time}, end_time: {self.endtime}, teacher: {self.teacher}, day: {self.day}, school_subject: {self.school_subject})"


while True:
	try:
		db.create_all()
		break
	except:
		print("Connection to database failed. Retrying ...")
		time.sleep(5)

@app.route("/")
def index():
	return render_template("index.html", title="Home")

@app.route("/scan")
def scan():
	classrooms = Classroom.query.all()
	return render_template("scan.html", title = "Scan Classroom", classrooms = classrooms)

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
