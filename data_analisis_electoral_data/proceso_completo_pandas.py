

import os
import pandas as pd



df_f05 = pd.read_csv("recursos_input/F05_1_MUN_2015.csv",sep=";",error_bad_lines=False, encoding="utf-8")
df_f03 = pd.read_csv("recursos_input/F03_MUN_2015.csv",sep=";",error_bad_lines=False, encoding="utf-8")
df_f10 = pd.read_csv("recursos_input/F10_MUN_2015.csv",sep=";",error_bad_lines=False, encoding="utf-8")
df_siglas_cand = df_f03[["COD_CAND", "SIGLAS_CAND"]]

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

for n_mun in nombres_municipios:
    cod_municipio = df_f05.loc[df_f05['MUNICIPIO'] == n_mun]['COD_MUN'].values.tolist()[0] 			
    cod_ccaa = df_f05.loc[df_f05['MUNICIPIO'] == n_mun]['COD_CCAA'].values.tolist()[0] 
    cod_prov = df_f05.loc[df_f05['MUNICIPIO'] == n_mun]['COD_PROV'].values.tolist()[0] 

    print("----------------------------------------")
    print("filtrando datos para municipio " + n_mun)
    df_municipio = df_f10.loc[(df_f10['COD_MUN'] == cod_municipio) & (df_f10['COD_CCAA']==cod_ccaa) & (df_f10['COD_PROV']==cod_prov)].reset_index()

    print("sumando votos y agrupando por distrito " + n_mun)
    df_agrupado_sumado = df_municipio.groupby(["TIPO_ELECCION","ANIO","MES", "VUELTA", "COD_CCAA","COD_PROV","COD_MUN","DISTRITO", "SECCION","COD_CAND"],squeeze=False)["VOTOS_CAND"].sum().reset_index()

    print("substituyendo siglas candidatura " + n_mun)
    df_agrupado_sumado=df_agrupado_sumado.merge(df_siglas_cand, left_on='COD_CAND', right_on='COD_CAND',left_index=True, how='left')
    del df_agrupado_sumado["COD_CAND"]
    df_agrupado_sumado=df_agrupado_sumado.rename(index=str, columns={"SIGLAS_CAND": "COD_CAND"})

    print("organizando datos " + n_mun)
    df_agrupado_sumado["CUSEC"] = df_agrupado_sumado["COD_PROV"].astype(str).apply(lambda x: x.rjust(2,"0")) + df_agrupado_sumado["COD_MUN"].astype(str).apply(lambda x: x.rjust(3,"0"))+ df_agrupado_sumado["DISTRITO"].astype(str).apply(lambda x: x.rjust(2,"0")) + df_agrupado_sumado["SECCION"].astype(str).apply(lambda x: x.rjust(3,"0"))
    df_agrupado_sumado = pd.pivot_table(df_agrupado_sumado, values = 'VOTOS_CAND', index=["CUSEC","COD_PROV","DISTRITO", "SECCION"], columns = 'COD_CAND').reset_index()
    df_agrupado_sumado = df_agrupado_sumado.rename(index=str, columns={"COD_PROV": "PROV", "DISTRITO": "DIST", "SECCION":"SECC_CEN"})

    print("calculando porcentajes de cada partido para " + n_mun)
    cols_no_partidos=['CUSEC','PROV','DIST','SECC_CEN']
    df_partidos = df_agrupado_sumado.copy()
    for col in cols_no_partidos: 
        del df_partidos[col]

    suma_partidos = df_partidos.sum(axis=1)
    for col in list(df_agrupado_sumado):
        if col not in cols_no_partidos:
            nueva_col="%"+col
            df_agrupado_sumado[nueva_col] = (df_agrupado_sumado[col]/suma_partidos)*100
            df_agrupado_sumado[nueva_col]=df_agrupado_sumado[nueva_col].round(decimals = 3)

    print("guardando en fichero de salida")
    dir_salida = "resultados"
    nombre_subfichero_salida = n_mun + "_F10_MUN_2015_denom_cand_agrupado_ruben_pc.csv"
    df_agrupado_sumado.to_csv(dir_salida + "/" + nombre_subfichero_salida, sep=";", index=False)
