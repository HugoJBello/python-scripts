from cusec_shapefield_filter_generator_gdal import CusecShapefiledFilterGDAL
from data_reader_pandas import DataReaderPandas
from data_reader_pandas import ResultadosEnMunicipio


def main():
    #Carpeta que contiene los csv con los datos de los resultados de las elecciones
    data_folder="C:/hugo_documentos/otros/github/python-scripts/data_analisis_electoral_data/resultados_output"
    
    #Carpeta de salida
    output_folder="data"

    #Shapefile con las secciones censales de toda la comunidad de madrid. De aquí cortaremos cada municipio y añadiremos los resultados a las features
    shapefile="data/SECC_CPV_E_20111101_01_R_INE_MADRID.shp"
    #shapefile="data/SECC_CPV_E_20111101_01_R_INE.shp"

    #Extraemos los datos de los resultados de las eleciones
    data_reader = DataReaderPandas(data_folder)
    lista_resultados = data_reader.resultados

    #Añadimos los resultados de las elecciones y cortamos el shapefile
    cusecShapefileFilter = CusecShapefiledFilterGDAL(shapefile,output_folder,lista_resultados)
    cusecShapefileFilter.extract_layer_from_nmun_and_add_data()
if __name__ == '__main__':
	main()
