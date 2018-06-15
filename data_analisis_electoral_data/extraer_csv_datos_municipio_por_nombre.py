#
# 
# ESTO ES PYTHON 3

# el programa principal generará una serie de ficheros csv con los datos filtrados de los municipios de la lista que le demos 
import os
import utils

# extrae los códigos de comunidad autónoma, provincia y municipio de la tabla de municipios dado el nombre de un municipio
def extraer_codigos_municipio_desde_nombre(nombre, nombre_fichero_con_codigos_municipios):
	fichero_csv_en_texto_municipios = open(nombre_fichero_con_codigos_municipios,"r").read()
	encabezado= utils.extraer_encabezado(fichero_csv_en_texto_municipios)
	num_columna_de_municipio=utils.encuentra_numero_columna_para(encabezado,"COD_MUN")
	num_columna_ccaa = utils.encuentra_numero_columna_para(encabezado,"COD_CCAA")
	num_columna_prov = utils.encuentra_numero_columna_para(encabezado,"COD_PROV")
	num_columna_nombre = utils.encuentra_numero_columna_para(encabezado,"MUNICIPIO")
	fila_encontrada = []
	encontrado = False
	resultado = []
	for fila in fichero_csv_en_texto_municipios.split("\n"):
		fila=fila.split(";")
		if(len(fila)>1):
			nombre_en_fichero = fila[num_columna_nombre].strip()
			if (nombre.strip() == nombre_en_fichero):
				fila_encontrada=fila
				encontrado= True
				break
	if (encontrado): 
		resultado = [ fila_encontrada[num_columna_ccaa],fila_encontrada[num_columna_prov],fila_encontrada[num_columna_de_municipio]]
	return resultado

# extrae o filtra  las filas del fichero que tienen un codigo de ccaa, codigo de provincia y municipio concretos.	
def extraer_filas( cod_municipio, cod_ccaa,cod_prov, fichero_csv_en_texto, nombre_fichero):
		encabezado= utils.extraer_encabezado(fichero_csv_en_texto)
		num_columna_de_municipio=utils.encuentra_numero_columna_para(encabezado,"COD_MUN")
		num_columna_ccaa = utils.encuentra_numero_columna_para(encabezado,"COD_CCAA")
		num_columna_prov = utils.encuentra_numero_columna_para(encabezado,"COD_PROV")
		if (num_columna_de_municipio == -1): num_columna_de_municipio = 6
		if (num_columna_ccaa==-1):num_columna_ccaa = 4
		if (num_columna_prov==-1):num_columna_prov = 5
		# transformamos el fichero en un vector que en cada elemento contiene una fila (
		filas_resultados_mesas_array = fichero_csv_en_texto.split("\n")
		
		resultados_mesas_de_municipio = []
		for fila in filas_resultados_mesas_array:
			#rompemos la fila en columnas usando la coma (que separa las columnas del csv)
			fila_dividida_en_columnas = fila.split(";")
			if (len(fila_dividida_en_columnas)>=num_columna_de_municipio):
				columna_municipio = fila_dividida_en_columnas[num_columna_de_municipio]
				columna_ccaa = fila_dividida_en_columnas[num_columna_ccaa]
				columna_prov = fila_dividida_en_columnas[num_columna_prov]
				 
				if ("F06_1_MUN" in nombre_fichero):
					encontrado = ((columna_municipio.strip() == cod_municipio.strip()) and
					(columna_prov.strip() == cod_prov.strip()))
				else :
					encontrado = ((columna_municipio.strip() == cod_municipio.strip()) and
					(columna_ccaa.strip() == cod_ccaa.strip())and
					(columna_prov.strip() == cod_prov.strip()))
					
				if encontrado:
					resultados_mesas_de_municipio = resultados_mesas_de_municipio + [fila + "\n"]
		return resultados_mesas_de_municipio
		
		
#----------------------------------------------------------------------------------------------------
# programa principal: Filtra los datos y crea nuevos archivos con los datos filtrados.	
def principal (nombres_municipios, nombre_ficheros_mesas_y_cera, nombre_fichero_con_codigos_municipios, nombre_carpeta_datos, nombre_carpeta_temporal):
	
	print("---------------------------------")
	print("extrayendo y filtrando municipios")
	print("---------------------------------")
		
	#creamos subdirectorios  si no existen
	if not os.path.exists(nombre_carpeta_temporal):
		os.makedirs(nombre_carpeta_temporal)

	for nombre_fichero in os.listdir(nombre_carpeta_datos):

		fichero_csv_en_texto = open(nombre_carpeta_datos + "/" +nombre_fichero,"r").read()
		# extraemos el encabezado (nombres de las variables)
		encabezado = utils.extraer_encabezado(fichero_csv_en_texto)
		
		for municipio in nombres_municipios:
			print("procesando los datos del fichero " + nombre_fichero+ " para " + municipio)
			codigos_municipio = extraer_codigos_municipio_desde_nombre(municipio, nombre_fichero_con_codigos_municipios)
			cod_municipio = codigos_municipio[2]
			cod_ccaa=codigos_municipio[0]
			cod_prov = codigos_municipio[1]
			# extraemos las filas correspondientes al codigo de mnicipio
			resultado = extraer_filas(cod_municipio,cod_ccaa,cod_prov, fichero_csv_en_texto,nombre_fichero)
			
			#anadimos el emcabezado al resultado
			resultado = [encabezado + "\n"] + resultado
			
			#guardamos el nuevo fichero con los datos de nuestro municipio
			nombre_fichero_salida = nombre_carpeta_temporal+ "/" + municipio + "_" + nombre_fichero
			fichero_salida = open(nombre_fichero_salida,"w")
			fichero_salida.writelines(resultado)
			fichero_salida.close()

if __name__ == "__main__":
	nombre_carpeta_salida = "resultados_output"
	nombre_carpeta_temporal= "ficheros_temporales"
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

	nombre_fichero_con_codigos_municipios = "recursos_input/F05_1_MUN_2015.csv"
	nombre_fichero_candidaturas_mesas_y_cera = "recursos_input/F10_MUN_2015.csv"
	
	principal(nombres_municipios, nombre_fichero_candidaturas_mesas_y_cera, nombre_fichero_con_codigos_municipios, nombre_carpeta_datos, nombre_carpeta_temporal)
	