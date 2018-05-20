from selenium import webdriver

class ScrapperSelenium:

    def __init__(self, urls):
        self.urls = urls
        self.driver = webdriver.Chrome()
    
    def get_data(self):

        for url in self.urls:
            self.driver.get(url) # url associated with button click
            print(self.driver.page_source.encode("utf-8"))
            button = self.driver.find_elements_by_class_name("item-info-container")
            print(button)