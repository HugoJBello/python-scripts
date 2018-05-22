from selenium import webdriver
from idealista_entry_dto import IdealistaEntryDTO
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
    
    def get_data(self):
        for url in self.urls:
            driver = self.driver
            driver.get(url) 
            driver.set_window_position(-4000,0)

            self.get_data_from_page(driver)
            

    def get_data_from_page(self,driver):
        item_info_container = self.driver.find_elements_by_class_name("item-info-container")
        self.parse_info_container_and_update_dictionary(item_info_container)
        random_int =4250 + random.randint(-3, 3)
        driver.execute_script("window.scrollTo(0, "+str(random_int) +");")
        time.sleep(random.uniform(0.5,1))
        self.parse_info_container_and_update_dictionary(item_info_container)
        random_int =8573 + random.randint(-3, 3)
        driver.execute_script("window.scrollTo(0, "+str(random_int) +");")
        time.sleep(random.uniform(0.5,1))
        self.parse_info_container_and_update_dictionary(item_info_container)

        print(self.data)
        time.sleep(random.uniform(5.5,6))
        if (self.is_next_page()):
            url=driver.find_elements_by_class_name("icon-arrow-right-after")[0].get_attribute("href")
            driver.get(url)
            self.get_data_from_page(driver)
        else: driver.close()

    def is_next_page(self):
        next_button=self.driver.find_elements_by_class_name("icon-arrow-right-after")
        return not next_button == []

    def parse_info_container_and_update_dictionary(self,info_container_array):
            if(self.data==None): self.data = {}
            for home in info_container_array:
                title=home.find_element_by_tag_name('a').text
                prize=home.find_elements_by_class_name('item-price')[0].text 
                rooms=home.find_elements_by_class_name('item-detail')[0].text.replace(" hab.","")
                meters=home.find_elements_by_class_name('item-detail')[1].text.replace(" m²","")
                dto=IdealistaEntryDTO(title,prize,meters,rooms,self.driver.current_url)
                if (title): self.data[title]=dto