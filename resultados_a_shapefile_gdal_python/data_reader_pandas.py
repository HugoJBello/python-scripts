import pandas as pd
import os
import sys
sys._enablelegacywindowsfsencoding()

#https://www.visualstudio.com/es/thank-you-downloading-visual-studio/?sku=BuildTools
#then once visual studio is installed install build tools with it
#pip3 install pandas
class ResultadosEnMunicipio:
    def __init__(self,nombre_municipio,fichero):
        self.nombre_municipio=nombre_municipio
        self.fichero=fichero

class DataReaderPandas:
    def __init__(self,data_folder):
        self.data_folder=data_folder
        self.resultados=[]
        for fichero in os.listdir(self.data_folder):
            municipio=fichero.split("_")[0]
            print(municipio)
            ruta_fichero=self.data_folder+"/"+fichero
            resultado = ResultadosEnMunicipio(municipio,fichero)
            resultado.datos_partidos = self.extraer_datos_partidos(ruta_fichero)
            resultado.nombres_partidos= self.extraer_nombres_partidos(resultado.datos_partidos)
            self.resultados = self.resultados + [resultado]

    def extraer_datos_partidos(self,fichero):
        df_resultados_mun = pd.read_csv(fichero,sep=";")
        #print(df_resultados_mun.iloc[1]['P.P.'])
        return df_resultados_mun

    def extraer_nombres_partidos(self,datos_partidos):
        lista= list(datos_partidos)
        for col in ['CUSEC','PROV','DIST','SECC_CEN']:
            lista.remove(col)
        return lista        


         
        
   