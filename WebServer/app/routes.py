"""
Questo file contiene le definizioni deglu URL del sito.
Ad ogni URL è associato un metodo che esegue un'azione
e ritorna una risposta HTML.
"""

from datetime import datetime

from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from sqlalchemy.exc import IntegrityError

import bgtasks
from app import app
from db import Classroom, SchoolHour
from db import db

@app.route("/")
def index():
	"""Ritorna la homepage del sito."""
	return render_template("index.html", title="Home")

@app.route("/scan")
def scan():
	"""Ritorna la pagina per scansionare le aule con gli orari attuali delle classi"""
	data = []
	classrooms = Classroom.query.all()

	for classroom in classrooms:
		school_hour = SchoolHour.query.filter(SchoolHour.classroom_id == classroom.code, SchoolHour.start_time < datetime.now(), SchoolHour.end_time > datetime.now()).first()
		data.append({ "classroom": classroom, "school_hour": school_hour })

	return render_template("scan.html", title = "Scan Classroom", data = data)

@app.route("/guide")
def guide():
	"""Ritorna la pagina della guida utente all'uso del sito"""
	return render_template("guide.html", title = "Guide")

@app.route("/schedule/<int:id>")
def schedule(id):
	"""Ritorna gli orari di una classe specifica."""
	data = {}

	classroom = Classroom.query.get_or_404(id);
	data["classroom"] = classroom

	timetables = SchoolHour.query.filter(SchoolHour.classroom_id == classroom.code).all()

	data["timetables"] = []
	for timetable in timetables:
		data["timetables"].append(timetable)

	return render_template("schedule.html", title = "Schedule", data = data)

@app.route("/admin")
def admin():
	"""Ritorna il pannello di controllo admin"""
	classrooms = Classroom.query.order_by(Classroom.code).all()
	school_hours = SchoolHour.query.order_by(SchoolHour.day, SchoolHour.start_time).all()
	return render_template("admin.html", title = "DB Admin", classrooms = classrooms, school_hours = school_hours)

@app.route("/admin/deletecr/<int:code>")
def admin_delete_cr(code):
	"""Elimina l'aula specificata dal database."""
	classroom_to_delete = Classroom.query.get_or_404(code)
	db.session.delete(classroom_to_delete)
	db.session.commit()
	return redirect(url_for("admin"))

@app.route("/admin/addcr", methods = ["POST"])
def admin_add_cr():
	"""Aggiunge una nuova aula nel database."""
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
	"""Aggiorna un'aula."""
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
	"""Aggiorna gli orari di un'aula."""
	classroom = Classroom.query.get_or_404(code)
	bgtasks.fetch_classroom_timetable(classroom.name)
	flash("Gli orari stanno venendo aggiornati in background. Ricaricare regolarmente la pagina per visualizzare le modifiche.")
	return redirect(url_for("admin"))

@app.route("/admin/deletesh/<int:id>")
def admin_delete_sh(id):
	"""Elimina un orario di un'aula dal database."""
	school_hour_to_delete = SchoolHour.query.get_or_404(id)
	db.session.delete(school_hour_to_delete)
	db.session.commit()
	return redirect(url_for("admin"))

@app.route("/admin/addsh", methods = ["POST"])
def admin_add_sh():
	"""Aggiunge l'orario di un'aula al database."""
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
	"""Aggiorna un'orario di un'aula."""
	old_id = int(request.form["id"])

	school_hour_to_edit = SchoolHour.query.get_or_404(old_id)
	school_hour_to_edit.classroom_id = request.form["classroom_id"]
	school_hour_to_edit.start_time = datetime.strptime(request.form["start_time"], "%H:%M:%S").time()
	school_hour_to_edit.end_time = datetime.strptime(request.form["end_time"], "%H:%M:%S").time()
	school_hour_to_edit.teacher = request.form["teacher"]
	school_hour_to_edit.day = datetime.isoformat(request.form["day"]).date()
	school_hour_to_edit.school_subject = request.form["subject"]

	try:
		db.session.commit()
	except IntegrityError as e:
		return render_template("error.html", message = "L'elemento esiste già nel database.", details = str(e))

	return redirect(url_for("admin"))

@app.route("/admin/shcleanup")
def admin_shcleanup():
	"""Elimina tutti gli orari dei giorna passati dal database."""

	school_hours_to_delete = SchoolHour.query.filter(SchoolHour.day < datetime.now()).delete()

	db.session.commit()

	return redirect(url_for("admin"))

@app.route("/admin/refreshall")
def admin_refreshall():
	"""Aggiorna gli orari di tutte le aule."""
	classrooms = Classroom.query.all()
	for classroom in classrooms:
		bgtasks.fetch_classroom_timetable(classroom.name)
	return redirect(url_for("admin"))

@app.route("/running_tasks")
def running_tasks():
	return str(bgtasks.get_running_tasks())

@app.errorhandler(404)
def page_not_found(e):
	"""Gestisce gli errori 404 delle pagine non trovate."""
	return render_template("error.html", message = "La pagina non è stata trovata.", details = str(e))
