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

# Recorre el fichero de códigos y obtiene un diccionario para transformar los cod. de candidatura
# en denominaciones de candidatura.
def crear_diccionario_candidaturas(fichero_codigos):
	encabezado = utils.extraer_encabezado(fichero_codigos)
	num_col_cod_cand = utils.encuentra_numero_columna_para(encabezado,"COD_CAND")
	num_col_siglas_cand = utils.encuentra_numero_columna_para(encabezado,"SIGLAS_CAND")
	
	resultado = {}
	for fila in fichero_codigos.split("\n"):
			datos_fila = fila.split(";")
			if (len(datos_fila)>1): resultado[datos_fila[num_col_cod_cand]]=datos_fila[num_col_siglas_cand]
	return resultado

# Substituye los códigos de candidatura por las denominaciones de candidatura a partir de los 
# datos del diccionario obtenido. Asumirá que los códigos de candidatura están en la columna 10.
def substituir_cod_cand(fichero_base,diccionario):
	num_col_cod_cand = 10
	resultado=[]
	for fila in fichero_base.split("\n"):
			datos_fila = fila.split(";")
			if (len(datos_fila)>1): 
				cod_cand=datos_fila[num_col_cod_cand]
				fila_reemplazada = fila.replace(";"+cod_cand+";",";"+ diccionario[cod_cand]+";")
				resultado = resultado + [fila_reemplazada+"\n"]
	return resultado		

#Programa principal -------------------------------------------------------------------------------------	
def principal(directorio,prefijo_fichero,nombre_fichero_codigos):
	print("-----------------------------------------------")
	print("substituyendo codigos de candidatura por siglas")
	print("-----------------------------------------------")

	
	#el sufijo que añadiremos al guardar los resultados en un nuevo fichero
	sufijo = "_denom_cand.csv"
	
	#Extraemos el fichero de códigos
	fichero_csv_en_texto = open(nombre_fichero_codigos,"r").read()
	
	#Creamos el diccionario
	diccionario_codigos = crear_diccionario_candidaturas(fichero_csv_en_texto)
	
	#Recorremos cada fichero en la subcarpeta 
	for fichero in os.listdir(directorio):
		nombre_subfichero = os.fsdecode(fichero)
		#Verificamos que tiene el prefijo que queremos
		if (prefijo_fichero in nombre_subfichero):
			#Descartamos que no haya sido tratado antes
			if (not ( sufijo in nombre_subfichero)):
				print("obteniendo nombres de candidaturas para " + nombre_subfichero)
				subfichero_csv_en_texto = open(directorio + "/" + nombre_subfichero,"r").read()
				
				#hacemos la sustitución
				resultado = substituir_cod_cand(subfichero_csv_en_texto,diccionario_codigos)
				
				#guardamos los resultados en un fichero con el sufijo para distinguirlo
				nombre_subfichero_salida = nombre_subfichero.replace(".csv","") + sufijo
				subfichero_salida = open(directorio + "/" + nombre_subfichero_salida,"w")
				subfichero_salida.writelines(resultado)
				subfichero_salida.close()

if __name__ == "__main__":
	#Directorio donde estarán los ficheros a substituir, en cuyo nombre contendrán lo que pongamos en 
	# la variable prefijo_fichero 
	directorio = "filtrados_municipios_substit_candidaturas"
	
	prefijo_fichero = "F10_MUN_2015.csv"
	nombre_fichero_con_codigos_municipios = "recursos_input/F03_1_MUN_2015.csv"
	principal(directorio,prefijo_fichero,nombre_fichero_con_codigos_municipios)