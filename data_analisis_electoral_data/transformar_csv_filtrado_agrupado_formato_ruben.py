# OBJETIVO: 
# PROCESO:  
import os
import utils
def obtener_conjunto_partidos(fichero_csv_en_texto, encabezado):
    resultado = set()
    num_col_cod_cand = utils.encuentra_numero_columna_para(encabezado,"SIGLAS_CAND")
    filas = fichero_csv_en_texto.split("\n")
    for n in range(1,len(filas)):
        if(len(filas[n].split(";"))>1): 
            partido = filas[n].split(";")[num_col_cod_cand].strip()
            resultado.add(partido)
    return sorted(resultado)
            
def crear_tabla_partidos(fichero_csv_en_texto,encabezado,conjunto_partidos):
    filas = fichero_csv_en_texto.split("\n")
    dic_secciones ={}
    nuevo_encabezado = crear_encabezado(conjunto_partidos)
    num_col_provincia = utils.encuentra_numero_columna_para(encabezado,"COD_PROV")
    num_col_municipio = utils.encuentra_numero_columna_para(encabezado,"COD_MUN")
    num_col_distrito = utils.encuentra_numero_columna_para(encabezado,"DISTRITO")
    num_col_seccion = utils.encuentra_numero_columna_para(encabezado,"SECCION")
    num_col_partido = utils.encuentra_numero_columna_para(encabezado,"SIGLAS_CAND")
    num_col_votos = utils.encuentra_numero_columna_para(encabezado,"VOTOS_CAND")

    for n in range(1,len(filas)):
        fila_cortada = filas[n].split(";")
        if(len(fila_cortada)>1): 
            cusec = fila_cortada[num_col_provincia].rjust(2,"0") + fila_cortada[num_col_municipio].rjust(3,"0") +  fila_cortada[num_col_distrito].rjust(2,"0") +fila_cortada[num_col_seccion].rjust(3,"0") 
            partido_en_linea=fila_cortada[num_col_partido].strip()
            if cusec in dic_secciones.keys():
                votos_partido_linea = fila_cortada[num_col_votos]
                dic_secciones[cusec][partido_en_linea] = votos_partido_linea
            else:
                nuevo_dic_secc ={}
                for partido in conjunto_partidos:
                    nuevo_dic_secc[partido] = "0"
                dic_secciones[cusec] = nuevo_dic_secc
                votos_partido_linea = fila_cortada[num_col_votos]
                dic_secciones[cusec][partido_en_linea] = votos_partido_linea
    nuevo_csv=nuevo_encabezado + "\n"

    for cusec in dic_secciones.keys():
        prov = cusec[0:2]
        dist = cusec[6]
        secc= cusec[8:11]
        nueva_fila = cusec + ";" + prov + ";" + dist + ";" + secc 
        for partido in dic_secciones[cusec].keys():
            nueva_fila = nueva_fila + ";" + dic_secciones[cusec][partido]
        nuevo_csv=nuevo_csv + nueva_fila +"\n"
    return nuevo_csv

def crear_encabezado(conjunto_partidos):
    encabezado = "CUSEC;PROV;DIST;SECC_CEN"
    for partido in conjunto_partidos:
        encabezado = encabezado + ";" + partido
    return encabezado

#----------------------------------------------------------------------------------------------------
# programa principal
def principal(directorio,prefijo_fichero):
    sufijo = "_ruben.csv"

    print("---------------------------------")
    print("limpiando el formato de ficheros ")
    print("---------------------------------")

    for fichero in os.listdir(directorio):
        nombre_subfichero = os.fsdecode(fichero)
		#Verificamos que tiene el prefijo que queremos
        if (prefijo_fichero in nombre_subfichero): 
            print("procesando " + nombre_subfichero)
            subfichero_csv_en_texto = open(directorio + "/" + nombre_subfichero,"r").read()
            encabezado = utils.extraer_encabezado(subfichero_csv_en_texto)
            conjunto_partidos= obtener_conjunto_partidos(subfichero_csv_en_texto, encabezado)
            tabla_partidos = crear_tabla_partidos(subfichero_csv_en_texto,encabezado,conjunto_partidos)
            
            nombre_subfichero_salida = nombre_subfichero.replace(".csv","") + sufijo
            subfichero_salida = open(directorio + "/" + nombre_subfichero_salida,"w")
            subfichero_salida.writelines(tabla_partidos)
            subfichero_salida.close()

if __name__ == "__main__":
    directorio = "filtrados_municipios_substit_candidaturas"
    prefijo_fichero = "F10_MUN_2015_denom_cand_agrupado.csv"
    principal(directorio,prefijo_fichero)