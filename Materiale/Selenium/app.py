from flask import Flask
from scrapper import Scrapper

app = Flask(__name__)

@app.route("/")
def stampa_dati():
    scrapper = Scrapper()
    dati = scrapper.cerca_orario_aule("328 (A-325)")
    ris = ""
    for i, item in dati.items():
        for j, lezioni in item.items():
            ris += j + ": " + lezioni + " "
        ris += "<br>"
    return ris
