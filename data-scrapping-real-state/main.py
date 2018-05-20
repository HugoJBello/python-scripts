from scrapper import Scrapper
from scrapper_selenium import ScrapperSelenium

def main():
    urls=['https://www.idealista.com/venta-viviendas/galapagar-madrid/con-precio-hasta_300000,chalets,casas-de-pueblo/']
    scrapper = ScrapperSelenium(urls)
    scrapper.get_data()



if __name__ == '__main__':
	main()
