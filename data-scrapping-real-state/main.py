from scrapper.scrapper_selenium_idealista import ScrapperSeleniumIdealista
from scrapper.scrapper_selenium_fotocasa import ScrapperSeleniumFotocasa

from mongodb_dao.mongodb_data_recorder import MongoDBDataRecorder
from mongodb_dao.mongodb_config_grabber import MongoConfigGrabber
from mongodb_dao.mongodb_summary_recorder import MongoDBSummaryRecorder

def main():
    #urls=['https://www.idealista.com/venta-viviendas/galapagar-madrid/con-precio-hasta_300000,chalets,casas-de-pueblo/']
    
    config_grabber = MongoConfigGrabber()
    config_grabber.get_scrapping_urls()
    urls_idealista=config_grabber.scrapping_urls_idealista
    urls_fotocasa = config_grabber.scrapping_urls_fotocasa
    
    scrapper_fotocasa = ScrapperSeleniumFotocasa(urls_fotocasa)
    scrapper_fotocasa.get_data()
    data_fotocasa = scrapper_fotocasa.data
    summary_dictionary_fotocasa = scrapper_fotocasa.summaries

    scrapper_idealista = ScrapperSeleniumIdealista(urls_idealista)
    scrapper_idealista.get_data()
    data_idealista = scrapper_idealista.data
    summary_dictionary_idealista = scrapper_idealista.summaries

    data = data_idealista.copy()
    data.update(data_fotocasa)

    mongodb_data_recorder = MongoDBDataRecorder(data)
    mongodb_data_recorder.post_data()

    mongodb_summary_recorder_idealista= MongoDBSummaryRecorder(summary_dictionary_idealista)
    mongodb_summary_recorder_idealista.post_data()

    mongodb_summary_recorder_fotocasa= MongoDBSummaryRecorder(summary_dictionary_fotocasa)
    mongodb_summary_recorder_fotocasa.post_data()


if __name__ == '__main__':
	main()
