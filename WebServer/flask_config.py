import os

class FlaskConfigBase:
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class FlaskConfigDebug(FlaskConfigBase):
	SQLALCHEMY_DATABASE_URI = "sqlite:///classroom.db"
	SQLALCHEMY_ECHO = True

class FlaskConfigRelease(FlaskConfigBase):
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://query:Punk42h2AsaCbzs@db:3306/classroom_timetables"
	SQLALCHEMY_ECHO = False

def get_flask_config():
	debug_mode = os.environ.get("DEBUG_MODE")

	if debug_mode == "yes":
		return FlaskConfigDebug
	else:
		return FlaskConfigRelease
