import time

from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)

class Classroom(db.Model):
	"""Modello che descrive una classe."""

	__tablename__ = "classroom"
	code = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(16), nullable = False, unique = True)

	def __repr__(self):
		return f"Classroom(code: {self.code}, name: {self.name})"

class SchoolHour(db.Model):
	"""Modello che descrive una lezione scolastica."""

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

db.create_all()
