class FlaskConfigBase(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class FlaskConfigDebug(FlaskConfigBase):
	SQLALCHEMY_DATABASE_URI = "sqlite:///classroom.db"
	SQLALCHEMY_ECHO = True

class FlaskConfigRelease(FlaskConfigBase):
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://query:Punk42h2AsaCbzs@db:3306/classroom_timetables"
	SQLALCHEMY_ECHO = False
