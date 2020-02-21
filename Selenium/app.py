from flask import *
from scrapper import Scrapper

app = Flask(__name__)

@app.route('/aule', methods=['GET'])
def aule():
    aula = request.args.get('aula')
    settimanaDopo = request.args.get('settimanaDopo')

    # Conversione da string a boolean
    if settimanaDopo == 'True':
        settimanaDopo = True
    else:
        settimanaDopo = False
    scrapper = Scrapper()
    dati = scrapper.cerca_orario_aule(aula, settimanaDopo)
    if dati is None:
        return "SETTIMANA DI VACANZA"
    ris = "Aula " + aula + "<br>"
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

