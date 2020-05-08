"""
Questo file è il punto di partenza dell'applicazione web.
Questo è il file che si dovrà avviare per eseguire l'applicazione.
"""

from app import app
import routes

if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0")
