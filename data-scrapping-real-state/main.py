from scrapper import Scrapper
from scrapper_selenium import ScrapperSelenium
from mongodb_data_recorder import MongoDBDataRecorder
from mongodb_config_grabber import MongoConfigGrabber

def main():
    #urls=['https://www.idealista.com/venta-viviendas/galapagar-madrid/con-precio-hasta_300000,chalets,casas-de-pueblo/']
    
    config_grabber = MongoConfigGrabber()
    config_grabber.get_scrapping_urls()
    urls=config_grabber.scrapping_urls
    
    scrapper = ScrapperSelenium(urls)
    scrapper.get_data()
    data = scrapper.data

    mongodb_data_recorder = MongoDBDataRecorder(data)
    mongodb_data_recorder.post_data()

if __name__ == '__main__':
	main()
