import re
import site
import json
import time
import datetime
from builtins import print
from operator import le

site.addsitedir('./PIL')
site.addsitedir('./selenium')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, url="https://www.cpttrevano.ti.ch/orario/invite?invite=true"):
        self.url = url
        opts = Options()
        opts.set_headless()
        assert opts.headless
        self.browser = webdriver.Chrome(options=opts)
     
    def cerca_orario_aule(self, ricerca):
        snow_logged = False
        self.browser.get(self.url)
        self.loaded_check("GInterface.Instances[0].Instances[0]_Combo1")

        # clicca su Corso
        self.browser.find_element_by_id("GInterface.Instances[0].Instances[0]_Combo2").click()

        # Clicca sulla barra di ricerca
        cerca_orario = self.browser.find_element_by_id("GInterface.Instances[1].Instances[1].bouton_Edit")
        cerca_orario.clear()
        cerca_orario.send_keys(ricerca)

        # Clicca la lente per ricercare
        self.browser.find_element_by_id("GInterface.Instances[1].Instances[1].bouton_Bouton").click()

        time.sleep(1)

        #self.clicca_numero_settimana_dopo()

        #apre il menu per cambiare la visulalizzazione
        self.browser.find_element_by_id("GInterface.Instances[0].Instances[2].bouton_Bouton").click()

        time.sleep(1)

        # clicca su in elenco
        self.browser.find_element_by_id('GInterface.Instances[0].Instances[2]_1').click()

        time.sleep(1)

        soup = BeautifulSoup(self.browser.page_source, features="html5lib")

        # cerca la tabella che contiene l'orario
        table = soup.find('table', id="GInterface.Instances[1].Instances[8]_Contenu_0")

        # cerca le righe che contengono le info sulle materie (oario inizio e fine, docente, ...)
        rows = table.find_all('tr', recursive=True)

        settimana = [] # Contiene tutto l'orario della settimana

        giorno = {'giornoTesto': None, 'materie': None} # Contiene il giorno in forma testuale e le materie del giorno

        materie = [] # Contiene le materie del giorno

        lezione = {'time': None, 'lesson': None, 'teacher': None, 'classe': None} # Contiene i dati della lezione.

        primaVolta = True # Serve ha non far fare l'inserimento nei dizionari al primo ciclo

        for row in rows:
            tds = row.find_all('td', recursive=True)
            for i, td in enumerate(tds):
                if td.has_attr('class') and td['class'][0] == 'Gras':
                    if(not primaVolta):
                        giorno['materie'] = materie
                        materie = []
                        settimana.append(giorno)
                        giorno = {'giornoTesto': None, 'materie': None}
                    primaVolta = False
                    giorno['giornoTesto'] = td.text.strip()
                elif td.has_attr('style'):
                    if (i == 2):
                        lezione['time'] = td.text.strip()

                        # Cerca Lezione
                    if (i == 3):
                        lezione['lesson'] = td.text.strip()

                        # Cerca docente
                    if (i == 4):
                        lezione['teacher'] = td.text.strip()

                        # Cerca Classe
                    if (i == 5):
                        lezione['classe'] = self.parse_classe(td.text)
                        materie.append(lezione)
                        lezione = {'time': None, 'lesson': None, 'teacher': None, 'classe': None}
                        break
        giorno['materie'] = materie
        settimana.append(giorno)
        print(settimana)
        return settimana

    # Clicca il numero della prossima settimana
    def clicca_numero_settimana_dopo(self):
        numero_settimana = ((datetime.datetime.now() - datetime.datetime(datetime.datetime.now().year, 1, 1)).days // 7) + 1
        table = self.browser.find_element_by_id("GInterface.Instances[1].Instances[4]_Calendrier")
        settimane = table.find_elements_by_class_name("Calendrier_Jour_Const")

        for settimana in settimane:
            if settimana.text == str(numero_settimana + 1):
                settimana.click()
                break
            else:
                pass

    def parse_classe(self, text):
        pattern = 'SAM [IED][1-4][ABCD]{2}'
        classi = re.findall(pattern, text)
        ris = ""
        if classi is None:
            return ""
        for classe in classi:
            ris += classe + " "
        return ris.strip()

    def get_chart(self):
        url = str(self.url)
        self.browser.get(url) 
        self.loaded_check("chart-container-builder")
        time.sleep(2)
        try:
            element = self.browser.find_element_by_class_name('highcharts-contextbutton')
            self.browser.execute_script("""var element = arguments[0];element.parentNode.removeChild(element);""", element)
        except:
            pass
        chart = self.browser.find_element_by_id("report-container-builder")
        chart_source = chart.get_attribute('innerHTML')

        return chart_source

    def get_data(self):
        availability = {}
        agreed_availability = {
            "Application Management" : 99,
            "EWP Services" : 99,
            "eArchive" : 99
        }
        
        s3_url = str(self.s3_url)
        self.browser.get(s3_url) 
        self.loaded_check("AvailPercLabel")
        measured_availability = self.browser.find_element_by_id("AvailPercLabel").get_attribute('innerHTML').replace('%', '')
        availability["measured_availability"] = measured_availability
        availability["agreed_availability"] = 99

        return availability
        
    def loaded_check(self,element_id):
        loaded = False
        try:
            myElem = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, element_id)))            
            loaded = True
        except TimeoutException:
            print("ERROR: TimeoutException " + str(element_id))

        return loaded

    def exit(self):
        self.browser.close()

if __name__ == "__main__":
    pass




