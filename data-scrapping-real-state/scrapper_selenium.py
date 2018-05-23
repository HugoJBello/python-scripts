from selenium import webdriver
from idealista_entry_dto import IdealistaEntryDTO
from summary_scrapped_dto import SummaryScrappedDTO
import time
import random

#https://www.seleniumhq.org/download/
#14393
#https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

class ScrapperSelenium:

    def __init__(self, urls):
        self.urls = urls
        self.driver = webdriver.Edge()
        #self.driver = webdriver.Chrome()
        self.data ={}
        self.summary = None
    
    def get_data(self):
        for url in self.urls:
            driver = self.driver
            driver.get(url) 
            driver.set_window_position(-4000,0)

            self.get_data_from_page(driver)
            

    def get_data_from_page(self,driver):
        item_info_container = self.driver.find_elements_by_class_name("item-info-container")
        self.parse_info_container_and_update_data(item_info_container)

        random_int =4250 + random.randint(-3, 3)
        driver.execute_script("window.scrollTo(0, "+str(random_int) +");")
        time.sleep(random.uniform(0.5,0.9))
        self.parse_info_container_and_update_data(item_info_container)
        print(len(self.data))

        random_int =8573 + random.randint(-3, 3)
        driver.execute_script("window.scrollTo(0, "+str(random_int) +");")
        time.sleep(random.uniform(0.5,0.9))
        self.parse_info_container_and_update_data(item_info_container)
        print(len(self.data))
        print("-------------")


        time.sleep(random.uniform(1.5,2))
        if (self.is_next_page()):
            url=driver.find_elements_by_class_name("icon-arrow-right-after")[0].get_attribute("href")
            driver.get(url)
            self.get_data_from_page(driver)
        else: 
            self.get_summary(driver)
            driver.close()
            

    def is_next_page(self):
        next_button=self.driver.find_elements_by_class_name("icon-arrow-right-after")
        return not next_button == []

    def parse_info_container_and_update_data(self,info_container_array):
            if(self.data==None): self.data = {}
            for home in info_container_array:
                title=home.find_element_by_tag_name('a').text.strip()
                url_element=home.find_element_by_tag_name('a').get_attribute("href").strip()
                prize=home.find_elements_by_class_name('item-price')[0].text.replace(" €","").replace("\u20ac","").strip()
                rooms=home.find_elements_by_class_name('item-detail')[0].text.replace(" hab.","").strip()
                meters=home.find_elements_by_class_name('item-detail')[1].text.replace(" m²","").strip()
                dto=IdealistaEntryDTO(title,prize,meters,rooms,self.driver.current_url,url_element)
                if (not dto.url_element in self.data.keys()): 
                    self.data[dto.url_element]=dto
                else:
                    if (self.data[dto.url_element].title==""):
                        self.data[dto.url_element]=dto

    def get_summary(self,driver):
        average_prize=self.driver.find_elements_by_class_name("items-average-price")[0].text.replace("Precio medio","").replace("eur/m²","").strip()
        self.summary = SummaryScrappedDTO(average_prize,len(self.data.keys()),self.driver.current_url,"")
        