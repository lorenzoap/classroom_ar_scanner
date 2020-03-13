from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask("classroom_ar_scanner")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://query:Punk42h2AsaCbzs@db:3306/classroom_timetables"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///classroom.db" # Debug
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

@app.route("/admin")
def admin():
	classrooms = Classroom.query.order_by(Classroom.code).all()
	return render_template("admin.html", title = "DB Admin", classrooms = classrooms)

@app.route("/admin/delete/<int:code>")
def admin_delete_cr(code):
	classroom_to_delete = Classroom.query.get_or_404(code)
	db.session.delete(classroom_to_delete)
	db.session.commit()
	return redirect("/admin")

@app.route("/admin/add", methods = ["POST"])
def admin_add_cr():
	name = ""

	try:
		name = str(request.form["name"])
	except ValueError as e:
		return render_template("error.html", message = "Uno o più valori inseriti non sono validi.", details = str(e))
	except Exception as e:
		return render_template("error.html", message = "Errore sconosciuto.", details = str(e))

	new_classroom = Classroom(name = name)
	db.session.add(new_classroom)
	db.session.commit()
	return redirect("/admin")

@app.route("/admin/edit", methods = ["POST"])
def admin_edit_cr():
	old_code = 0
	new_name = ""

	try:
		old_code = int(request.form["classroom_id"])
		new_name = str(request.form["name"])
	except ValueError as e:
		return render_template("error.html", message = "Uno o più valori inseriti non sono validi.", details = str(e))
	except Exception as e:
		return render_template("error.html", message = "Errore sconosciuto.", details = str(e))

	classroom_to_edit = Classroom.query.get_or_404(old_code)
	classroom_to_edit.name = request.form["name"]
	db.session.commit()
	return redirect("/admin")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
