"""
Questo file contiene l'inizializzazione dell'applicazione
base di Flask.
"""

from flask import Flask

from flask_config import get_flask_config

app = Flask(__name__)
app.config.from_object(get_flask_config())
