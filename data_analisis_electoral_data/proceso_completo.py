import os
import extraer_csv_datos_municipio_por_nombre
import sustituir_cod_cand_por_denom_cand
import agrupar_secciones
import transformar_csv_filtrado_agrupado_formato_ruben
import utils

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
    nombre_fichero_con_codigos_candidaturas = "recursos_input/F03_MUN_2015.csv"
    nombre_fichero_candidaturas_mesas_y_cera = "recursos_input/F10_MUN_2015.csv"
      
    prefijo_sustituir = nombre_fichero_candidaturas_mesas_y_cera.split("/")[1].replace(".csv","") + ".csv"
    prefijo_agrupar = prefijo_sustituir.split(".csv")[0] + "_denom_cand.csv"
    prefijo_transformar = prefijo_agrupar.split(".csv")[0] + "_agrupado.csv"
    prefijo_mover = prefijo_transformar.split(".csv")[0] + "_ruben.csv"

    #Ejecutamos los scripts paso a paso
    extraer_csv_datos_municipio_por_nombre.principal (nombres_municipios, nombre_fichero_candidaturas_mesas_y_cera, nombre_fichero_con_codigos_municipios, nombre_carpeta_datos, nombre_carpeta_temporal)
    sustituir_cod_cand_por_denom_cand.principal (nombre_carpeta_temporal,prefijo_sustituir, nombre_fichero_con_codigos_candidaturas)
    agrupar_secciones.principal(nombre_carpeta_temporal, prefijo_agrupar)
    transformar_csv_filtrado_agrupado_formato_ruben.principal(nombre_carpeta_temporal, prefijo_transformar)
    
    utils.mover_ficheros(nombre_carpeta_temporal,nombre_carpeta_salida,prefijo_mover)