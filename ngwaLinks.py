from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os

class NGWSLinks:
    data = {}
    service = Service("C:/chromedriver.exe")

    def __init__(self):
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def land_required_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(3)

    def get_links(self):
        links = self.driver.find_elements(By.XPATH, '//a[@class="item-list__title"]')
        self.driver.implicitly_wait(4)
        for l in links:
            print("Link: "+l.get_attribute('href'))
            self.data['Link'] = l.get_attribute('href')
            p = pd.DataFrame([self.data])
            p.to_csv("path/links.csv", mode='a', header=not os.path.exists("path/links.csv"), index=False)




bot = NGWSLinks()
for i in range(0, 401, 20):
    bot.land_required_page(f'https://www.ngwa.org/publications-and-news/find-a-business-or-professional?startRow={i}&rowsPerPage=20')
    bot.get_links()