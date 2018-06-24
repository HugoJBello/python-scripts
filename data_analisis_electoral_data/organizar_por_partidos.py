

import os
import utils
import pandas as pd



df_f05 = pd.read_csv("recursos_input/F05_1_MUN_2015.csv",sep=";",error_bad_lines=False, encoding="latin-1")
df_f03 = pd.read_csv("recursos_input/F03_MUN_2015.csv",sep=";",error_bad_lines=False, encoding="latin-1")
df_f10 = pd.read_csv("recursos_input/F10_MUN_2015.csv",sep=";",error_bad_lines=False, encoding="latin-1")

nombres_municipios = ["Burgos"]

n_mun="Madrid"

cod_municipio = df_f05.loc[df_f05['MUNICIPIO'] == n_mun]['COD_MUN'].values.tolist()[0] 			
cod_ccaa = df_f05.loc[df_f05['MUNICIPIO'] == n_mun]['COD_CCAA'].values.tolist()[0] 
cod_prov = df_f05.loc[df_f05['MUNICIPIO'] == n_mun]['COD_PROV'].values.tolist()[0] 


df_municipio = df_f10.loc[(df_f10['COD_MUN'] == cod_municipio) & (df_f10['COD_CCAA']==cod_ccaa) & (df_f10['COD_PROV']==cod_prov)].reset_index()


for i, row in df_municipio.iterrows():
    cod_cand= df_municipio.ix[i,"COD_CAND"]
    nom_cand= df_f03.loc[df_f03['COD_CAND'] == cod_cand]['SIGLAS_CAND'].values.tolist()[0]
    df_municipio.ix[i,"COD_CAND"]=nom_cand

df_agrupado_sumado = df_municipio.groupby(["TIPO_ELECCION","ANIO","MES", "VUELTA", "COD_CCAA","COD_PROV","COD_MUN","DISTRITO", "SECCION","COD_CAND"],squeeze=False)["VOTOS_CAND"].sum().reset_index()

print(df_agrupado_sumado)

df_agrupado_sumado = pd.pivot_table(df_agrupado_sumado, values = 'VOTOS_CAND', index=["COD_CCAA","COD_PROV","COD_MUN","DISTRITO", "SECCION"], columns = 'COD_CAND').reset_index()
print(df_agrupado_sumado)