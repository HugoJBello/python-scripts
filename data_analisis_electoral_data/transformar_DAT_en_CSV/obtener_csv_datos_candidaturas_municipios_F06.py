# OBJETIVO: Este script se encarga de transformar los ficheros que nos cede el instituto nacional de estadística.
# Genera por cada .DAT (de datos sin elemento de separación, en crudo) un .CSV con encabezado y los datos separados por ";" en una tabla.

# PROCESO:  buscará el fichero en la ruta que le pongamos en la variable ruta_fichero_sin_procesar. Para saber como tiene que agrupar los datos en 
# columnas deberemos rellenar la lista lista_longitudes_y_descrip con un elemento por cada corte que se deba hacer en cada línea, por ejemplo si los dos
# primeros caracteres son el TIPO_ELECCION pondremos un elemento [2,"TIPO_ELECCION"], si los cuatro siguientes son el año pondremos [4,"ANIO"] después y así

def crear_encabezado(lista_longitudes_y_descrip):
    resultado=""
    for n in range(0,len(lista_longitudes_y_descrip)):
        if (n==0):
            resultado = lista_longitudes_y_descrip[n][1].strip()
        else:
            resultado = resultado +";" +  lista_longitudes_y_descrip[n][1].strip()
    return resultado

def romper_cadenas_datos(datos_txt,lista_longitudes_y_descrip):
    datos_txt_lineas = datos_txt.split("\n")
    csv_salida = [crear_encabezado(lista_longitudes_y_descrip) + "\n"]
    for linea in datos_txt_lineas:
        linea_procesada = ""
        indice = 0
        for n in range(0,len(lista_longitudes_y_descrip)):
            if (n==0):
                linea_procesada = linea[indice:indice + lista_longitudes_y_descrip[n][0]].strip()
            else:
                linea_procesada = linea_procesada +";" +  linea[indice:indice + lista_longitudes_y_descrip[n][0]].strip()
            indice = indice + lista_longitudes_y_descrip[n][0]
        csv_salida = csv_salida + [linea_procesada + "\n"]
    return csv_salida

#----------------------------------------------------------------------------------------------------
# programa principal
if __name__ == "__main__":
    ruta_fichero_sin_procesar="06041505.DAT"
    #lista construida con las longitudes de cada bloque y la descripción en orden
    lista_longitudes_y_descrip=[
        [2  ,"TIPO_ELECCION"],
        [4  ,"ANIO"],
        [2  ,"MES"],
        [1  ,"VUELTA"],
        [2  ,"COD_PROV"],
        [3  ,"COD_MUN"],
        [2  ,"DIST_ELEC"],
        [6  ,"COD_CAND"],
        [8  ,"VOTOS_CAND"],
        [3  ,"CAND_OBTENIDOS"]
    ]
    nombre_fichero_salida =ruta_fichero_sin_procesar.split(".DAT")[0] + ".csv"
    datos_txt = open(ruta_fichero_sin_procesar,"r").read()

    resultado = romper_cadenas_datos(datos_txt, lista_longitudes_y_descrip)
    fichero_salida = open(nombre_fichero_salida,"w")
    fichero_salida.writelines(resultado)
    fichero_salida.close()
 