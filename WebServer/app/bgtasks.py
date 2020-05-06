import datetime
import re
from threading import Thread

from app import app
from db import Classroom, db, SchoolHour
from scraper import Scraper

def convert_time_format(scraper_time):
	raw_start_time = scraper_time.split(" - ")[0].replace("h", ":")
	raw_end_time = scraper_time.split(" - ")[1].replace("h", ":")
	start_time = datetime.datetime.strptime(raw_start_time, "%H:%M").time()
	end_time = datetime.datetime.strptime(raw_end_time, "%H:%M").time()
	return { "start_time": start_time, "end_time": end_time }

def convert_date_format(scraper_date):
	day = int(scraper_date.split(" ")[1])

	year = int(scraper_date.split(" ")[3])

	month = 1
	if "gennaio" in scraper_date:
		month = 1
	elif "febbraio" in scraper_date:
		month = 2
	elif "marzo" in scraper_date:
		month = 3
	elif "aprile" in scraper_date:
		month = 4
	elif "maggio" in scraper_date:
		month = 5
	elif "giugno" in scraper_date:
		month = 6
	elif "luglio" in scraper_date:
		month = 7
	elif "agosto" in scraper_date:
		month = 8
	elif "settembre" in scraper_date:
		month = 9
	elif "ottobre" in scraper_date:
		month = 10
	elif "novembre" in scraper_date:
		month = 11
	elif "dicembre" in scraper_date:
		month = 12

	return datetime.date(year, month, day)

def task_fetch_classroom_timetable(classroom_id):
	classroom = Classroom.query.get_or_404(classroom_id)
	scraper = Scraper("https://www.cpttrevano.ti.ch/orario/invite?invite=true")
	result = scraper.get_timetable(classroom.name)

	days = result["timetable"]

	for day in days:
		for subject in day["subjects"]:
			# Aggiungi i dati al database
			time = convert_time_format(subject["time"])
			new_school_hour = SchoolHour(classroom_id = classroom_id,
			                             start_time = time["start_time"],
										 end_time = time["end_time"],
										 teacher = subject["teacher"],
										 day = convert_date_format(day["day"]),
										 school_subject = subject["lesson"])

			db.session.add(new_school_hour)
			db.session.commit()

def fetch_classroom_timetable(classroom_name):
	classroom = Classroom.query.filter_by(name = classroom_name).first()
	thread = Thread(target = task_fetch_classroom_timetable, args = (classroom.code, ))
	thread.start()