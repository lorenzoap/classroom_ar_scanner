import datetime
import json
import os
import re # Regex
import time
from threading import Thread

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Scraper:
	def __init__(self, url, debug = False):
		self.url = url

		driver_options = Options()
		driver_options.headless = not debug # Use headless mode if debug is disabled

		self.browser = webdriver.Firefox(options = driver_options, executable_path = "./geckodriver")

	def get_timetable(self, classroom_name):
		self.browser.get(self.url)

		# Aspetta che la pagina si carichi
		self.loaded_check("GInterface.Instances[0].Instances[0]_Combo1")

		# Sezione "Aule"
		self.browser.find_element_by_id("GInterface.Instances[0].Instances[0]_Combo2").click()

		# Barra di ricerca
		search_bar = self.browser.find_element_by_id("GInterface.Instances[1].Instances[1].bouton_Edit")
		search_bar.clear()
		search_bar.send_keys(classroom_name)

		# Clicca la lente per avviare la ricerca
		self.browser.find_element_by_id("GInterface.Instances[1].Instances[1].bouton_Bouton").click()

		# Attendi che la ricerca sia terminata e la pagina sia apparsa
		time.sleep(1)

		# Apre il menu per cambiare la visulalizzazione
		self.browser.find_element_by_id("GInterface.Instances[0].Instances[2].bouton_Bouton").click()

		# Attendi il termine dell'animazione del menu
		time.sleep(1)

		# Passa alla visualizzazione a elenco
		self.browser.find_element_by_id("GInterface.Instances[0].Instances[2]_1").click()

		# Attendi il caricamento della pagina
		time.sleep(1)

		# Parsa la pagina HTML
		html_page = BeautifulSoup(self.browser.page_source, features = "html5lib")

		# Cerca la tabella che contiene l'orario
		table = html_page.find("table", id = "GInterface.Instances[1].Instances[8]_Contenu_0")

		result = {
			"is_holiday": table is None,
			"timetable": []
		}

		# Se la tabella non esiste, è una settimana di vacanza
		if table is not None:
			# Contiene il giorno in forma testuale e le materie del giorno
			day = {
				"day": "",
				"subjects": []
			}

			subjects = []  # Contiene le materie del giorno

			lesson = {
				"time": None,
				"lesson": None,
				"teacher": None,
				"classes": None
			}  # Contiene i dati della lezione.

			first_time = True  # Serve a non far fare l'inserimento nei dizionari al primo ciclo

			# Cerca le righe che contengono le info sulle materie (oario inizio e fine, docente, ...)
			rows = table.find_all("tr", recursive = True)

			for row in rows:
				cols = row.find_all("td", recursive = True)
				for i, col in enumerate(cols):
					if col.has_attr("class") and col["class"][0] == "Gras":
						if not first_time:
							day["subjects"] = subjects
							subjects = []
							result["timetable"].append(day)
							day = {"day": None, "subjects": None}
						first_time = False
						day["day"] = col.text.strip()
					elif col.has_attr("style"):
						if i == 2:
							lesson["time"] = col.text.strip()

						# Cerca Lezione
						if i == 3:
							lesson["lesson"] = col.text.strip()

							# Cerca docente
						if i == 4:
							lesson["teacher"] = col.text.strip()

						# Cerca Classe
						if i == 5:
							lesson["classes"] = self.parse_class(col.text)
							subjects.append(lesson)
							lesson = {
								"time": None,
								"lesson": None,
								"teacher": None,
								"classes": None
							}
							break
			day["subjects"] = subjects
			result["timetable"].append(day)
		return result

	def parse_class(self, text):
		pattern = "SAM [IED][1-4][ABCD]{2}"
		classes = re.findall(pattern, text)
		ris =  []

		if classes is not None:
			for _class in classes:
				ris.append(_class.strip())

		return ris

	def loaded_check(self, element_id):
		loaded = False
		try:
			WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, element_id)))
			loaded = True
		except TimeoutException:
			print("ERROR: TimeoutException " + str(element_id))

		return loaded

	def __del__(self):
		self.browser.close()
