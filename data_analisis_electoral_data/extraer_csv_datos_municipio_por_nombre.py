#
# 
# ESTO ES PYTHON 3

# el programa principal generará una serie de ficheros csv con los datos filtrados de los municipios de la lista que le demos 
import os
import utils
import pandas as pd
import sys
sys.getfilesystemencoding()

#----------------------------------------------------------------------------------------------------
# programa principal: Filtra los datos y crea nuevos archivos con los datos filtrados.	
def principal (nombres_municipios,nombre_fichero_denom_cand, nombre_ficheros_mesas_y_cera, nombre_fichero_con_codigos_municipios, nombre_carpeta_datos, nombre_carpeta_temporal):
	
	print("---------------------------------")
	print("extrayendo y filtrando municipios")
	print("---------------------------------")
		
	#creamos subdirectorios  si no existen
	if not os.path.exists(nombre_carpeta_temporal):
		os.makedirs(nombre_carpeta_temporal)

	for nombre_fichero in os.listdir(nombre_carpeta_datos):
		if (not nombre_fichero in nombre_fichero_denom_cand):
			ruta_fichero=nombre_carpeta_datos + "/" +nombre_fichero

			df_cod_mun = pd.read_csv(nombre_fichero_con_codigos_municipios,sep=";",error_bad_lines=False, encoding="latin-1")

			for municipio in nombres_municipios:
				print("procesando los datos del fichero " + nombre_fichero+ " para " + municipio)

				cod_municipio = df_cod_mun.loc[df_cod_mun['MUNICIPIO'] == municipio]['COD_MUN'].values.tolist()[0] 
				
				df_fichero = pd.read_csv(ruta_fichero,sep=";",error_bad_lines=False, encoding="latin-1")

				df_filtrado=df_fichero.loc[df_fichero['COD_MUN'] == cod_municipio]
				#guardamos el nuevo fichero con los datos de nuestro municipio

				nombre_fichero_salida = nombre_carpeta_temporal+ "/" + municipio + "_" + nombre_fichero
				df_filtrado=df_filtrado.to_csv(nombre_fichero_salida, sep = ';', encoding="latin-1",index=False)

			

if __name__ == "__main__":
	nombre_carpeta_salida = "resultados_output"
	nombre_carpeta_temporal= "tmp"
	nombre_carpeta_datos="recursos_input"

	nombres_municipios = ["Madrid", "Móstoles", "Alcalá de Henares", 
							"Fuenlabrada", "Leganés", "Getafe", 
							"Alcorcón", "Torrejón de Ardoz", "Parla", "Alcobendas",
							"Las Rozas de Madrid", "San Sebastián de los Reyes",
							"Pozuelo de Alarcón", "Coslada", "Rivas-Vaciamadrid",
							"Valdemoro", "Majadahonda", "Collado Villalba", "Aranjuez",
							"Arganda del Rey", "Boadilla del Monte", "Pinto", "Colmenar Viejo",
							"Tres Cantos", "San Fernando de Henares", "Galapagar", "Arroyomolinos",
							"Villaviciosa de Odón", "Navalcarnero", "Ciempozuelos", "Torrelodones",
							"Paracuellos de Jarama", "Mejorada del Campo", "Algete"]

	nombre_fichero_denom_cand = "recursos_input/F03_MUN_2015.csv"
	nombre_fichero_con_codigos_municipios = "recursos_input/F05_1_MUN_2015.csv"
	nombre_fichero_candidaturas_mesas_y_cera = "recursos_input/F10_MUN_2015.csv"
	
	principal(nombres_municipios,nombre_fichero_denom_cand, nombre_fichero_candidaturas_mesas_y_cera, nombre_fichero_con_codigos_municipios, nombre_carpeta_datos, nombre_carpeta_temporal)
	