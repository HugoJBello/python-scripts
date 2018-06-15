import os

def extraer_encabezado(fichero_csv_en_texto):
	fichero_filas = fichero_csv_en_texto.split("\n")
	return fichero_filas[0]

# extrae el número de columna dado un nombre de columna (es decir que posición ocupa la columna 0,1,2,3...)
def encuentra_numero_columna_para(encabezado,nombre_de_columna_a_buscar):
	nombres_columna=encabezado.split(";")
	num_col=0
	for col in nombres_columna:
		if(col.strip() == nombre_de_columna_a_buscar):
			return num_col
		else:
			num_col= num_col + 1
	return -1

def mover_ficheros(directorio_origen,directorio_destino,prefijo):
    for nombre_fichero in os.listdir(directorio_origen):
        if prefijo in nombre_fichero:
            nueva_ruta = directorio_destino + "/" + nombre_fichero
            os.rename(directorio_origen + "/" + nombre_fichero, nueva_ruta)
