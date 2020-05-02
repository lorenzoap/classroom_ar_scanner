from datetime import date, datetime, time

from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from sqlalchemy.exc import IntegrityError

from app import app
from db import Classroom, SchoolHour
from db import db

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
	school_hours = SchoolHour.query.order_by(SchoolHour.day).all()
	return render_template("admin.html", title = "DB Admin", classrooms = classrooms, school_hours = school_hours)

@app.route("/admin/deletecr/<int:code>")
def admin_delete_cr(code):
	classroom_to_delete = Classroom.query.get_or_404(code)
	db.session.delete(classroom_to_delete)
	db.session.commit()
	return redirect(url_for("admin"))

@app.route("/admin/addcr", methods = ["POST"])
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
	try:
		db.session.commit()
	except IntegrityError as e:
		return render_template("error.html", message = "L'elemento esiste già nel database.", details = str(e))

	return redirect(url_for("admin"))

@app.route("/admin/editcr", methods = ["POST"])
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

	try:
		db.session.commit()
	except IntegrityError as e:
		return render_template("error.html", message = "L'elemento esiste già nel database.", details = str(e))

	return redirect(url_for("admin"))

@app.route("/admin/refresh/<int:code>")
def admin_refresh_cr(code):
	classroom = Classroom.query.get_or_404(code)
	scrapper.refresh_classroom_timetable(classroom.name)
	return redirect(url_for("admin"))

@app.route("/admin/deletesh/<int:id>")
def admin_delete_sh(id):
	school_hour_to_delete = SchoolHour.query.get_or_404(id)
	db.session.delete(school_hour_to_delete)
	db.session.commit()
	return redirect(url_for("admin"))

@app.route("/admin/addsh", methods = ["POST"])
def admin_add_sh():
	new_school_hour = SchoolHour(classroom_id = request.form["classroom_id"],
	                             start_time = datetime.strptime(request.form["start_time"], "%H:%M").time(),
	                             end_time = datetime.strptime(request.form["end_time"], "%H:%M").time(),
	                             teacher = request.form["teacher"],
	                             day = datetime.fromisoformat(request.form["day"]).date(),
	                             school_subject = request.form["subject"])

	db.session.add(new_school_hour)

	try:
		db.session.commit()
	except IntegrityError as e:
		return render_template("error.html", message = "L'elemento esiste già nel database.", details = str(e))

	return redirect(url_for("admin"))

@app.route("/admin/editsh", methods = ["POST"])
def admin_edit_sh():
	old_id = int(request.form["id"])

	school_hour_to_edit = SchoolHour.query.get_or_404(old_id)
	school_hour_to_edit.classroom_id = request.form["classroom_id"]
	school_hour_to_edit.start_time = datetime.strptime(request.form["start_time"], "%H:%M:%S").time()
	school_hour_to_edit.end_time = datetime.strptime(request.form["end_time"], "%H:%M:%S").time()
	school_hour_to_edit.teacher = request.form["teacher"]
	school_hour_to_edit.day = datetime.fromisoformat(request.form["day"]).date()
	school_hour_to_edit.school_subject = request.form["subject"]

	try:
		db.session.commit()
	except IntegrityError as e:
		return render_template("error.html", message = "L'elemento esiste già nel database.", details = str(e))

	return redirect(url_for("admin"))
