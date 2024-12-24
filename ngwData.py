from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from geopy.geocoders import ArcGIS
from geopy.geocoders import ArcGIS
import pandas as pd
import os
import time

class NGWSData:
    data = {}
    contacts = {}
    service = Service("C:/chromedriver.exe")
    geoLocation = ArcGIS(timeout=10)

    def __init__(self):
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def land_required_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)

    def get_my_id(self, my_id):
        self.data['listing ID'] = my_id

    def get_title(self):
        try:
            name = self.driver.find_element(By.XPATH, '//h1[@class="page-title"]').text
            self.driver.implicitly_wait(2)
            self.data['Title'] = name
        except:
            self.data['Title'] = 'N/A'

    def get_description(self):
        try:
            des = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__intro margin"]/div/p').text
            self.driver.implicitly_wait(2)
            self.data['Description'] = des
        except:
            self.data['Description'] = 'N/A'

    def get_logo(self):
        try:
            logo = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__intro margin"]/img').get_attribute('src')
            self.driver.implicitly_wait(2)
            self.data['Logo'] = logo
        except:
            self.data['Logo'] = 'N/A'

    def get_address(self):
        try:
            add = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[1]/p').text.replace('\n', ', ')
            self.driver.implicitly_wait(2)
            self.data['Address'] = add
            geocode = self.geoLocation.geocode(add)
            self.data['Latitude'] = str(geocode.latitude)
            self.data['Longitude'] = str(geocode.longitude)
        except:
            self.data['Address'] = 'N/A'
            self.data['Latitude'] = "N/A"
            self.data['Longitude'] = "N/A"

    def get_contacts(self):
        try:
            phone = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[2]/p[1]').text
            self.driver.implicitly_wait(2)
            self.data['Phone'] = phone
        except:
            self.data['Phone'] = 'N/A'

        try:
            fax = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[2]/p[2]').text
            self.driver.implicitly_wait(2)
            self.data['Fax'] = fax
        except:
            self.data['Fax'] = 'N/A'

    def get_website(self):
        try:
            web = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[3]/p/a').get_attribute('href')
            self.driver.implicitly_wait(3)
            self.data['Website'] = web
        except:
            self.data['Website'] = "N/A"

        try:
            try:
                category = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[3]/p[2]').text
                self.driver.implicitly_wait(2)
            except:
                category = None

            try:
                cate_2 = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[3]/p').text
                self.driver.implicitly_wait(2)
            except:
                cate_2 = None

            if category.lower() == 'Supplier'.lower() or category.lower() == 'Manufacturer'.lower():
                self.data['Category'] = category
            else:
                self.data['Category'] = cate_2
        except:
            self.data['Category'] = "N/A"

    def get_social_links(self):
        try:
            social = self.driver.find_elements(By.XPATH, '//div[@class="buyer-company__social margin"]/a')
            self.driver.implicitly_wait(2)

            # for facebook

            for s in social:
                if s.get_attribute('href').find('facebook.com') != -1:
                    self.data['Facebook'] = s.get_attribute('href')
                    break
            else:
                self.data['Facebook'] = "N/A"

            # get Instagram

            for s in social:
                if s.get_attribute('href').find('instagram.com') != -1:
                    self.data['Instagram'] = s.get_attribute('href')
                    break
            else:
                self.data['Instagram'] = "N/A"

            # get Twitter

            for s in social:
                if s.get_attribute('href').find('twitter.com') != -1:
                    self.data['Twitter'] = s.get_attribute('href')
                    break
            else:
                self.data['Twitter'] = "N/A"

            # get Youtube

            for s in social:
                if s.get_attribute('href').find('youtube.com') != -1:
                    self.data['Youtube'] = s.get_attribute('href')
                    break
            else:
                self.data['Youtube'] = "N/A"

            # get Linkedin

            for s in social:
                if s.get_attribute('href').find('linkedin.com') != -1:
                    self.data['Linkedin'] = s.get_attribute('href')
                    break
            else:
                self.data['Linkedin'] = "N/A"

        except:
            self.data['Facebook'] = "N/A"
            self.data['Instagram'] = "N/A"
            self.data['Twitter'] = "N/A"
            self.data['Youtube'] = "N/A"
            self.data['Linkedin'] = "N/A"

    def get_other_contacts(self, my_id):

        try:
            self.contacts['My Id'] = my_id
            conts = self.driver.find_elements(By.XPATH, '//div[@class="buyer-company__contacts margin"]/div')
            self.driver.implicitly_wait(2)
            for c in conts:
                cont_type = c.find_element(By.XPATH, './/div[1]/p[1]').text
                self.driver.implicitly_wait(3)
                self.contacts['Contact Type'] = cont_type
                name = c.find_element(By.XPATH, './/div[1]/p[2]').text
                self.driver.implicitly_wait(2)
                self.contacts['Name'] = name
                mail_type = c.find_element(By.XPATH, './/div[2]/p[1]').text
                self.driver.implicitly_wait(3)
                self.contacts['Email Type'] = mail_type
                mail = c.find_element(By.XPATH, './/div[2]/p[2]/a').get_attribute('href')
                self.driver.implicitly_wait(2)
                self.contacts['Email'] = mail

                for key, value in self.contacts.items():
                    print(key+": "+str(value))

                p = pd.DataFrame([self.contacts])
                p.to_csv('path/contacts1.csv', mode='a', header=not os.path.exists("path/contacts1.csv"), index=False)
        except:
            self.contacts['My Id'] = my_id
            self.contacts['Contact Type'] = "N/A"
            self.contacts['Name'] = 'N/A'
            self.contacts['Email Type'] = "N/A"
            self.contacts['Email'] = 'N/A'
            p = pd.DataFrame([self.contacts])
            p.to_csv('path/contacts1.csv', mode='a', header=not os.path.exists("path/contacts1.csv"), index=False)

    def get_video_link(self):
        try:
            v_link = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__media margin"]/div/iframe').get_attribute('src')
            self.driver.implicitly_wait(2)
            self.data['Video Link'] = v_link

        except:
            self.data['Video Link'] = "N/A"

    def get_images(self):
        try:
            images = self.driver.find_elements(By.XPATH, '//li[@class="media"]/a/img')
            self.driver.implicitly_wait(2)
            my_images = [i.get_attribute('src') for i in images]
            self.data['Image Urls'] = str(my_images)
        except:
            self.data['Image Urls'] = 'N/A'

    def get_Ameities(self):
        try:
            dict3 = {}
            all_amen_title = self.driver.find_elements(By.XPATH, '//div[@class="buyer-company__categories margin-top-large"]/h4')
            self.driver.implicitly_wait(2)
            all_amen_list = self.driver.find_elements(By.XPATH, '//div[@class="buyer-company__categories margin-top-large"]/ul')
            self.driver.implicitly_wait(2)
            for i, j in zip(all_amen_title, all_amen_list):
                dict3[i.text] = []
                dict3[i.text].append(str(j.text))
            self.data['My All Categories'] = str(dict3)
            dict3.clear()
        except:
            self.data['My All Categories'] = "N/A"

    def get_categories(self):
        try:
            try:
                category = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[3]/p[2]').text
                self.driver.implicitly_wait(2)
            except:
                category = None

            try:
                cate_2 = self.driver.find_element(By.XPATH, '//div[@class="buyer-company__info margin grid"]/div[3]/p').text
                self.driver.implicitly_wait(2)
            except:
                cate_2 = None

            if category.lower() == 'Supplier'.lower() or category.lower() == 'Manufacturer'.lower():
                self.data['Category'] = category
            else:
                self.data['Category'] = cate_2
        except:
            self.data['Category'] = "N/A"



    def move_into_file(self):
        self.data['Listing Url'] = self.driver.current_url
        for key, value in self.data.items():
            print(key + ": " + str(value))
        p = pd.DataFrame([self.data])
        p.to_csv('path/data.csv', mode='a',
                 header=not os.path.exists("path/data.csv"), index=False)
        print("********************************************************************************")



bot = NGWSData()
i = 1
with open("C:/imp codes/ngwa/links/links.csv") as file:
    for f in file:
        spl = f.split(',')
        bot.land_required_page(spl[1])
        bot.get_my_id(spl[0])
        bot.get_title()
        bot.get_description()
        bot.get_logo()
        bot.get_address()
        bot.get_contacts()
        bot.get_website()
        bot.get_social_links()
        bot.get_other_contacts(spl[0])
        bot.get_video_link()
        bot.get_images()
        bot.get_Ameities()
        bot.move_into_file()
        i = i + 1










