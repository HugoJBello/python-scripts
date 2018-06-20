#pip3 install gdal
#sudo apt install gdal-bin python3-gdal
#https://gis.stackexchange.com/questions/152076/where-can-i-find-gdal-python-bindings-for-python-3-4
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
#install python 3.7 and run   pip3 install GDAL-2.2.4-cp37-cp37m-win_amd64.whl

from osgeo import ogr
import pandas as pd

from data_reader_pandas import DataReaderPandas
from data_reader_pandas import ResultadosEnMunicipio
import traceback

class CusecShapefiledFilterGDAL:
    def __init__(self,data_shapefile,output_folder,lista_resultados):
        self.data_shapefile=data_shapefile
        self.output_folder=output_folder
        self.layer_name =""
        self.lista_resultados=lista_resultados

        self.set_layer_and_ds()
        #self.extract_cusecs_shapefiles()
        
    def set_layer_and_ds(self):
        splitted=self.data_shapefile.split("/")
        self.layer_name = splitted[len(splitted)-1].replace(".shp","")

        self.data_source = ogr.Open(self.data_shapefile, True)  # True allows to edit the shapefile
        self.layer = self.data_source.GetLayer()
    
    def extract_layer_from_nmun_and_add_data(self):
        resultados = self.lista_resultados
        for resultado in resultados:
            nmun=resultado.nombre_municipio
            column_array =resultado.nombres_partidos
            df_partidos=resultado.datos_partidos

            layer=self.extract_layer_by_nmun(nmun)
            self.add_new_columns_to_layer(layer,column_array)
            self.add_data_in_new_columns_to_layer(layer,column_array,df_partidos)
            layer=None


    #Extrameos un nuevo layer a partir del nombre del municipio usando el shapefile de toda la comunidad de madrid
    def extract_layer_by_nmun(self,nmun):
        sql ="SELECT * FROM " + self.layer_name + " WHERE NMUN = '" + nmun+ "';COMMIT"
        new_layer_name = nmun +"_"+ self.layer_name
        result = self.data_source.ExecuteSQL(sql, dialect='SQLITE')
        layer_new = self.data_source.CopyLayer(result, new_layer_name)
        result=None
        return layer_new
    
    #Añadimos las columnas de los partidos políticos votados en ese municipio
    def add_new_columns_to_layer(self, layer, column_array):
        for col in column_array:
            col_short=self.cut_column(col)
            if "%" in col_short:
                new_field = ogr.FieldDefn(col_short, ogr.OFTReal) 
                new_field.SetWidth(6)
                new_field.SetPrecision(3)           
            else:
                new_field = ogr.FieldDefn(col_short, ogr.OFTInteger)
            layer.CreateField(new_field)

    #Rellenamos las columnas nuevas con los datos de los votos
    def add_data_in_new_columns_to_layer(self, layer, column_array,df_partidos):
        feature = layer.GetNextFeature()
        while feature:
            for col in column_array:
                cusec=feature.GetField("CUSEC")
                try:
                    value=df_partidos.loc[df_partidos["CUSEC"].isin([cusec])].iloc[0][col]
                    col_short=self.cut_column(col)
                    if (not "%" in col_short):
                        feature.SetField(col_short, str(value))
                    else:
                        feature.SetField(col_short, value)
                    layer.SetFeature(feature)
                except: traceback.print_exc()
            feature = layer.GetNextFeature()


    def cut_column(self,column_str):
        return column_str[0:9]


    def extract_cusecs_shapefiles_by_nmun(self,data_nmuns_array):
                for item in data_nmuns_array:
                    nmun= item            
                    layer_new = self.extract_layer_by_nmun(nmun)
                    result = layer_new =  None