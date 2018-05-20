from selenium import webdriver
import time

class ScrapperSelenium:

    def __init__(self, urls):
        self.urls = urls
        self.driver = webdriver.Chrome()
    
    def get_data(self):

        for url in self.urls:
            driver = self.driver
            driver.get(url) # url associated with button click
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
            time.sleep(0.5)
            homes = self.driver.find_elements_by_class_name("item-info-container")
            titles =[]
            for home in homes:
                titles = titles + [home.find_element_by_tag_name('a').text]

            print(titles)