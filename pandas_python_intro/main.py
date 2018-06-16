#pip3 install pandas
import pandas as pd
pd.options.mode.chained_assignment = None

def obtener_nombre_cand(df_nom_cand,cod_cand):
    return df_nom_cand.loc[df_nom_cand['COD_CAND'] == cod_cand]['DENOM_CAND'].values.tolist()[0]

def extraer_comunidad_madrid(df_cod_mun,cca_madrid):
    df_filtrado=df_cod_mun.loc[df_cod_mun['COD_CCAA'] == cca_madrid]
    return df_filtrado



df_nom_cand = pd.read_csv("data/F03_MUN_2015.csv",sep=";",error_bad_lines=False)
df_cod_mun = pd.read_csv("data/F05_1_MUN_2015.csv",sep=";",error_bad_lines=False)
df_cod_cand_mesas = pd.read_csv("data/F10_MUN_2015.csv",sep=";",error_bad_lines=False)

print(obtener_nombre_cand(df_nom_cand,1))

cca_madrid=13

#filtrar los data frame para que solo contengan madrid
df_cod_mun_madrid=extraer_comunidad_madrid(df_cod_mun,cca_madrid)
df_cod_cand_mesas_madrid=extraer_comunidad_madrid(df_cod_cand_mesas,cca_madrid)

print(df_cod_cand_mesas_madrid)


#substituir codigo candidatura por nombre candidatura
for i, row in df_cod_cand_mesas_madrid.iterrows():
    nom_cand= obtener_nombre_cand(df_nom_cand,row["COD_CAND"])
    df_cod_cand_mesas_madrid.ix[i,"COD_CAND"]=nom_cand

print(df_cod_cand_mesas_madrid)
