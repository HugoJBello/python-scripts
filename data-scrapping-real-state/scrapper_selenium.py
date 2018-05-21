from selenium import webdriver
from idealista_entry_dto import IdealistaEntryDTO
import time

class ScrapperSelenium:

    def __init__(self, urls):
        self.urls = urls
        self.driver = webdriver.Chrome()
        self.data ={}

    def parse_info_container_and_update_dictionary(self,info_container_array):
        if(self.data==None): self.data = {}
        for home in info_container_array:
            title=home.find_element_by_tag_name('a').text
            prize=home.find_elements_by_class_name('item-price')[0].text
            rooms=home.find_elements_by_class_name('item-detail')[0].text.replace(" hab.","")
            meters=home.find_elements_by_class_name('item-detail')[1].text.replace(" m²","")
            dto=IdealistaEntryDTO(title,prize,meters,rooms)
            if (title): self.data[title]=dto
    
    def get_data(self):
        for url in self.urls:
            driver = self.driver
            driver.set_window_size(1000, 10000)
            driver.get(url) 
            self.get_data_from_page(driver)
            
            
    def is_next_page(self):
        next_button=self.driver.find_elements_by_class_name("icon-arrow-right-after")
        return not next_button == []

    def get_data_from_page(self,driver):
        item_info_container = self.driver.find_elements_by_class_name("item-info-container")
        self.parse_info_container_and_update_dictionary(item_info_container)
        driver.execute_script("window.scrollTo(0, 4250);")
        time.sleep(1)
        self.parse_info_container_and_update_dictionary(item_info_container)
        driver.execute_script("window.scrollTo(0, 8573);")
        time.sleep(1)
        self.parse_info_container_and_update_dictionary(item_info_container)

        print(self.data)
        time.sleep(1)
        if (self.is_next_page()):
            url=driver.find_elements_by_class_name("icon-arrow-right-after")[0].get_attribute("href")
            print(url)
            driver.get(url)
            self.get_data_from_page(driver)

        
