import site
import time
import getpass
site.addsitedir('./PIL')
from PIL import *
site.addsitedir('./selenium')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class Scrapper:
    baseurl = "https://servicenow.adgr.net/navpage.do"
    def __init__(self, user, password, url, s3_user, s3_password, s3_url):
        self.user = user
        self.password = password
        self.url = url
        self.browser = webdriver.PhantomJS()
     
    def login_snow(self):
        snow_logged = False
        self.browser.get(self.baseurl)
        username = str(self.user)
        password = str(self.password)
        self.loaded_check("gsft_main")
        self.browser.switch_to.frame(self.browser.find_element_by_id("gsft_main"))

        username_field = self.browser.find_element_by_id("user_name")
        password_field = self.browser.find_element_by_id("user_password")
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_attempt = self.browser.find_element_by_id("sysverb_login")
        login_attempt.click()
        
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

    def save_report(self):
        self.browser.get('http://localhost:8080/login.html')
        element = self.browser.find_element_by_id('container') # find part of the page you want image of
        location = element.location
        size = element.size
        png = self.browser.get_screenshot_as_png() # saves screenshot of entire page
        fox.quit()
        im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom)) # defines crop points
        im.save('report.png') # saves new cropped image

    def exit(self):
        self.browser.close()

if __name__ == "__main__":
    pass




