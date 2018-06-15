# OBJETIVO: 
# 
# REQUISITOS: 

import os

def agrupa_por_secciones_sumando_votos(fichero_csv_en_texto):
	secciones = {}
	num_col_seccion= 8
	num_col_mesas = 9
	num_col_partidos = 10
	num_col_distrito = 7
	num_col_votos = 11
	num_col_provincia = 5
	num_col_municipio = 6
	for fila in fichero_csv_en_texto.split("\n"):
		cols_en_fila = fila.split(";")
		if(len(cols_en_fila)>1):
			mesa = cols_en_fila[num_col_mesas]
			fila_sin_mesa = fila.replace(";" + mesa + ";", ";")
			partido_de_fila = cols_en_fila[num_col_partidos]
			cusec = cols_en_fila[num_col_provincia].rjust(2,"0") + cols_en_fila[num_col_municipio].rjust(3,"0") +  cols_en_fila[num_col_distrito].rjust(2,"0") +cols_en_fila[num_col_seccion].rjust(2,"0") 
			if (cusec in secciones.keys()):
				partidos_seccion = secciones[cusec]
			else:
				partidos_seccion = {}
			if (partido_de_fila in partidos_seccion.keys()):
				fila_en_dic = partidos_seccion[partido_de_fila]
				cols_fila_en_dic = fila_en_dic.split(";")
				votos_en_fila_dic =cols_fila_en_dic[num_col_votos-1]
				votos_en_fila = cols_en_fila[num_col_votos]
				votos_sumados = int(float(votos_en_fila_dic)) + int(float(votos_en_fila))
				fila_en_dic_actualizada = fila_en_dic.replace(partido_de_fila + ";" + votos_en_fila_dic,partido_de_fila + ";" + str(votos_sumados))
				partidos_seccion[partido_de_fila] = fila_en_dic_actualizada
			else:
				partidos_seccion[partido_de_fila]=fila_sin_mesa
			secciones[cusec] = partidos_seccion
	return secciones
	
def guardar_diccionario_a_fichero(diccionario_secciones, nombre_subfichero_salida, directorio):
	secciones_array = diccionario_secciones.values()
	resultado_texto=""
	for seccion_dic_partidos in secciones_array:
		for fila in seccion_dic_partidos.values():
			resultado_texto = resultado_texto + fila + "\n"
			
	subfichero_salida = open(directorio + "/" + nombre_subfichero_salida,"w")
	subfichero_salida.writelines(resultado_texto)
	subfichero_salida.close()

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
				subfichero_csv_en_texto = open(directorio + "/" + nombre_subfichero,"r").read()
				nombre_subfichero_salida = nombre_subfichero.replace(".csv","") + sufijo
				diccionario_quitar_rep = agrupa_por_secciones_sumando_votos(subfichero_csv_en_texto)
				guardar_diccionario_a_fichero(diccionario_quitar_rep,nombre_subfichero_salida,directorio)
	

if __name__ == "__main__":
	directorio = "filtrados_municipios_substit_candidaturas"
	prefijo_fichero = "F10_MUN_2015_denom_cand.csv"
	principal(directorio,prefijo_fichero)
	