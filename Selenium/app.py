from flask import Flask
from scrapper import Scrapper

app = Flask(__name__)

@app.route("/")
def stampa_dati():
    scrapper = Scrapper()
    dati = scrapper.cerca_orario_aule("428 (A-422)")
    print(dati)
    ris = ""
    for giorni in dati:
        for giorno in giorni.values():
            if isinstance(giorno, str):
                ris += giorno + " "
            else:
                for materie in giorno:
                    for materia in materie.values():
                        ris += materia + " "
                ris += "<br>"
            ris += "<br>"
    return ris
