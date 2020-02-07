import re
import site
import json
import time
site.addsitedir('./PIL')
site.addsitedir('./selenium')
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup

class Scrapper:
    baseurl = "https://www.cpttrevano.ti.ch/orario/invite?invite=true"
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome()
     
    def cercaOrarioAule(self, ricerca):
        snow_logged = False
        k = Controller()
        self.browser.get(self.baseurl)
        self.loaded_check("GInterface.Instances[0].Instances[0]_Combo1")


        #clicca su Corso
        self.browser.find_element_by_id("GInterface.Instances[0].Instances[0]_Combo2").click()

        #Clicca sulla barra di ricerca
        cerca_orario = self.browser.find_element_by_id("GInterface.Instances[1].Instances[1].bouton_Edit")
        cerca_orario.clear()
        cerca_orario.send_keys(ricerca)

        #Clicca la lente per ricercare
        self.browser.find_element_by_id("GInterface.Instances[1].Instances[1].bouton_Bouton").click()

        #clicca su in griglia per cambiare la visulalizzazione
        self.browser.find_element_by_id("GInterface.Instances[0].Instances[2].bouton_Bouton").click()

        #Preme i tasti giù e invio per cambire la selezione da griglia ad elenco
        time.sleep(1)
        k.press(Key.down)
        time.sleep(1)
        k.release(Key.down)
        k.press(Key.enter)
        k.release(Key.enter)

        time.sleep(2)

        soup = BeautifulSoup(self.browser.page_source)

        #cerca la tabella che contiene l'orario
        table = soup.find('table', id="GInterface.Instances[1].Instances[8]_Contenu_0")

        #cerca le righe che contengono le info sulle materie (oario inizio e fine, docente, ...)
        rows = table.find_all_next('tr', {"class": "AvecMain c_7"})

        #cerca nella tabella il giorno
        giorni = table.find_all_next('td', {"class": "Gras"})

        for i, row in enumerate(rows):
            for el in row.find_all_next('td'):
                print(el.text)

        giorno = ""

        for g in giorni:
            pattern = r'(?P<giorno>\w{3}).*\s(?P<dd>\d\d)\s(?P<mese>\w{3,10})\s+(?P<anno>\d\d\d\d)'
            m = re.search(pattern, g.text)
            if m:
                giorno = m.group('giorno')




        e = "(?P<hinizio>\d{2})h\d{2} - (\d\d)h(\d\d) (?P<materia>[\w\s]+) (?P<classe>\w{3,6})\s+(N°\d+)"

        try:
            login_status = self.browser.find_element_by_id("sysparm_search")
            snow_logged = True
        except:
            pass

        return snow_logged
    
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




