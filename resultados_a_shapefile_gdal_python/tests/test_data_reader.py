import unittest
import sys
import os
sys.path.append("..")
from data_reader_pandas import DataReaderPandas


class TestDataReader(unittest.TestCase):  

    def testReader(self):
        data_folder="C:/Users/HJBG/Downloads/Datalyze-20180411T080217Z-001/Datalyze/Datos procesados/scripts_python_filtrado_y_procesado_municipios/resultados_output"
        data_reader = DataReaderPandas(data_folder)
        self.assertIsNotNone(data_reader.resultados)

if __name__ == '__main__':
	    unittest.main()
