# OBJETIVO: 
# 
# REQUISITOS: 

import os


#Programa principal -------------------------------------------------------------------------------------	
def principal(directorio,prefijo_fichero):
	print("----------------------------------------------")
	print("agrupando y sumando las mesas de cada distrito")
	print("----------------------------------------------")

	#Directorio donde estarán los ficheros a substituir, en cuyo nombre contendrán lo que pongamos en 
	# la variable prefijo_fichero 
	 
	#el sufijo que añadiremos al guardar los diccionarios en un nuevo fichero
	sufijo = "_agrupado.csv"
		
	#Recorremos cada fichero en la subcarpeta 
	for fichero in os.listdir(directorio):
		nombre_subfichero = os.fsdecode(fichero)
		#Verificamos que tiene el prefijo que queremos
		if (prefijo_fichero in nombre_subfichero):
			#Descartamos que no haya sido tratado antes
			if (not ( sufijo in nombre_subfichero)):
				print("agrupando secciones para " + nombre_subfichero)
				
	

if __name__ == "__main__":
	directorio = "tmp"
	prefijo_fichero = "F10_MUN_2015_denom_cand.csv"
	principal(directorio,prefijo_fichero)
	