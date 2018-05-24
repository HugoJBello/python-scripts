import unittest
import sys
sys.path.append("..")
from scrapper_selenium_fotocasa import ScrapperSeleniumFotocasa


class TestFotocasa(unittest.TestCase):  

    def testFotocasa(self):
        test_urls=["https://www.fotocasa.es/es/comprar/casas/galapagar/todas-las-zonas/l?latitude=40.5796&longitude=-4.00262&maxPrice=300000&propertySubtypeIds=3;5;7;9&combinedLocationIds=724,14,28,172,218,28061,0,0,0&gridType=3"]
        scrapper = ScrapperSeleniumFotocasa(test_urls)
        scrapper.get_data()
        self.assertIsNotNone(scrapper.data)

if __name__ == '__main__':
	    unittest.main()
