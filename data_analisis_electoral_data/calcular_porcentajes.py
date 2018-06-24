import os
import sys
import pandas as pd
pd.options.mode.chained_assignment = None
#sys._enablelegacywindowsfsencoding()


def principal(directorio, prefijo_fichero):
    #el sufijo que añadiremos al guardar los resultados en un nuevo fichero
    sufijo = "_pc.csv"
    for fichero in os.listdir(directorio):
        nombre_subfichero = os.fsdecode(fichero)
        #Verificamos que tiene el prefijo que queremos
        if (prefijo_fichero in nombre_subfichero):
            print("calculando porcentajes para " + nombre_subfichero)
            if (not ( sufijo in nombre_subfichero)):
                subfichero = directorio + "/" + nombre_subfichero
                df = calcular_porcentaje(subfichero)

                nombre_subfichero_salida = nombre_subfichero.replace(".csv","") + sufijo
                df.to_csv(directorio + "/" + nombre_subfichero_salida, sep=";", index=False)

def calcular_porcentaje(subfichero):
    cols_no_partidos=['CUSEC','PROV','DIST','SECC_CEN']
    df=pd.read_csv(subfichero,error_bad_lines=False, sep=";", encoding="latin-1")

    df_partidos = df.copy()
    for col in cols_no_partidos: 
        del df_partidos[col]
    
    suma_partidos = df_partidos["SUMA"]
    for col in list(df):
        if col not in cols_no_partidos:
            nueva_col="%"+col
            df[nueva_col] = (df[col]/suma_partidos)*100
            df[nueva_col]=df[nueva_col].round(decimals = 3)
    
    return df



if __name__ == "__main__":
    #Directorio donde estarán los ficheros a substituir, en cuyo nombre contendrán lo que pongamos en 
    # la variable prefijo_fichero 
    directorio = "tmp"
    nombre_fichero_denom_cand = "recursos_input/F03_MUN_2015.csv"
    prefijo_fichero = "F10_MUN_2015_denom_cand_agrupado_ruben"
    nombre_fichero_con_codigos_municipios = "recursos_input/F03_MUN_2015.csv"
    principal(directorio, prefijo_fichero)