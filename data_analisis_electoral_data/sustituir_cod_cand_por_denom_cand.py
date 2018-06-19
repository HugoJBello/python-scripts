# OBJETIVO: 
# Este script busca los ficheros que contienen la cadena de texto F10_MUN en 
# la carpeta que le indiquemos. Por cada fichero de datos 
# busca la columna con los códigos de candidatura y 
# usando la tabla F03_MUN_2015.csv los substituye por la denominación de la
# candidatura. Después guarda cada uno de estos ficheros substituidos con el sufijo "_denom_cand.csv"
# 

# REQUISITOS:  Es python 3.

import os
import utils
import sys
import pandas as pd
pd.options.mode.chained_assignment = None
sys._enablelegacywindowsfsencoding()

def obtener_nombre_cand(df_nom_cand,cod_cand):
    return df_nom_cand.loc[df_nom_cand['COD_CAND'] == cod_cand]['SIGLAS_CAND'].values.tolist()[0]

#Programa principal -------------------------------------------------------------------------------------	
def principal(directorio,prefijo_fichero,nombre_fichero_codigos,nombre_fichero_con_codigos_municipios):
	print("-----------------------------------------------")
	print("substituyendo codigos de candidatura por siglas")
	print("-----------------------------------------------")

	
	#el sufijo que añadiremos al guardar los resultados en un nuevo fichero
	sufijo = "_denom_cand.csv"
	
	#Creamos data frame
	df_cod_mun = pd.read_csv(nombre_fichero_codigos,sep=";",error_bad_lines=False,encoding='latin-1')
	df_nom_cand = pd.read_csv(nombre_fichero_con_codigos_municipios,sep=";",error_bad_lines=False,encoding='latin-1')

	#Recorremos cada fichero en la subcarpeta 
	for fichero in os.listdir(directorio):
		nombre_subfichero = os.fsdecode(fichero)
		#Verificamos que tiene el prefijo que queremos
		if (prefijo_fichero in nombre_subfichero):
			#Descartamos que no haya sido tratado antes
			if (not ( sufijo in nombre_subfichero)):
				print("obteniendo nombres de candidaturas para " + nombre_subfichero)
				subfichero = directorio + "/" + nombre_subfichero
			
				df_cod_cand_mesas = pd.read_csv(subfichero,error_bad_lines=False, sep=";")

				#hacemos la sustitución
				for i, row in df_cod_cand_mesas.iterrows():
					cod_cand= df_cod_cand_mesas.ix[i,"COD_CAND"]
					nom_cand= obtener_nombre_cand(df_nom_cand,cod_cand)
					df_cod_cand_mesas.ix[i,"COD_CAND"]=nom_cand
				print(nombre_fichero_codigos)
				nombre_subfichero_salida = nombre_subfichero.replace(".csv","") + sufijo
				df_cod_cand_mesas.to_csv(directorio + "/" + nombre_subfichero_salida, index=False)

if __name__ == "__main__":
	#Directorio donde estarán los ficheros a substituir, en cuyo nombre contendrán lo que pongamos en 
	# la variable prefijo_fichero 
	directorio = "tmp"

	nombre_fichero_denom_cand = "recursos_input/F03_MUN_2015.csv"
	prefijo_fichero = "F10_MUN_2015.csv"
	nombre_fichero_con_codigos_municipios = "recursos_input/F03_MUN_2015.csv"
	principal(directorio,prefijo_fichero,nombre_fichero_con_codigos_municipios,nombre_fichero_con_codigos_municipios)