from scrapper import Scrapper
from scrapper_selenium_idealista import ScrapperSeleniumIdealista
from scrapper_selenium_fotocasa import ScrapperSeleniumFotocasa

from mongodb_data_recorder import MongoDBDataRecorder
from mongodb_config_grabber import MongoConfigGrabber
from mongodb_summary_recorder import MongoDBSummaryRecorder

def main():
    #urls=['https://www.idealista.com/venta-viviendas/galapagar-madrid/con-precio-hasta_300000,chalets,casas-de-pueblo/']
    
    config_grabber = MongoConfigGrabber()
    config_grabber.get_scrapping_urls()
    urls_idealista=config_grabber.scrapping_urls_idealista
    urls_fotocasa = config_grabber.scrapping_urls_fotocasa
    
    scrapper_fotocasa = ScrapperSeleniumFotocasa(urls_fotocasa)
    scrapper_fotocasa.get_data()
    data_fotocasa = scrapper_fotocasa.data
    #summary_dictionary = scrapper_fotocasa.summaries

    scrapper_idealista = ScrapperSeleniumIdealista(urls_idealista)
    scrapper_idealista.get_data()
    data_idealista = scrapper_idealista.data
    summary_dictionary = scrapper_idealista.summaries

    data = data_idealista.copy()
    data.update(data_fotocasa)

    mongodb_data_recorder = MongoDBDataRecorder(data)
    mongodb_data_recorder.post_data()

    mongodb_summary_recorder= MongoDBSummaryRecorder(summary_dictionary)
    mongodb_summary_recorder.post_data()


if __name__ == '__main__':
	main()

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z