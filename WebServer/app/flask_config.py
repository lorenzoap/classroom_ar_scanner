import os

class FlaskConfigBase:
	"""Contiene la configurazione base per Flask"""
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///classroom.db"
	SECRET_KEY = "eAWYiIPDcjIbYxrr1qfn"

class FlaskConfigDebug(FlaskConfigBase):
	"""Contiene la configurazione di debug per Flask"""
	SQLALCHEMY_ECHO = True

class FlaskConfigRelease(FlaskConfigBase):
	"""Contiene la configurazione di produzione per Flask"""
	SQLALCHEMY_ECHO = False

def get_flask_config():
	"""Restituisce la configurazione di Flask da usare in base alla variabile d'ambiente "DEBUG_MODE"."""
	debug_mode = os.environ.get("DEBUG_MODE")

	if debug_mode in ["yes", "on", "true"]:
		return FlaskConfigDebug
	else:
		return FlaskConfigRelease
