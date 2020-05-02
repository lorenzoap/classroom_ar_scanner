import os

class FlaskConfigBase:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///classroom.db"

class FlaskConfigDebug(FlaskConfigBase):
	SQLALCHEMY_ECHO = True

class FlaskConfigRelease(FlaskConfigBase):
	SQLALCHEMY_ECHO = False

def get_flask_config():
	debug_mode = os.environ.get("DEBUG_MODE")

	if debug_mode in ["yes", "on", "true"]:
		return FlaskConfigDebug
	else:
		return FlaskConfigRelease
