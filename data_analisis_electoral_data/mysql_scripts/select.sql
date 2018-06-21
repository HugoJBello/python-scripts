USE datalyze;
SET NAMES "utf8";

 

SELECT DISTINCT f10.TIPO_ELECCION, f10.ANIO, f10.MES, f10.VUELTA, f10.COD_CCAA, f10.COD_PROV, f10.COD_MUN, f10.DISTRITO, f10.SECCION, f3.siglas_cand,
	(SELECT SUM(g10.VOTOS_CAND)
	FROM F10_MUN_2015  g10
	WHERE g10.cod_cand = f10.cod_cand
		and g10.cod_ccaa= f10.cod_ccaa
		and g10.cod_mun = f10.cod_mun
		and g10.cod_prov = f10.cod_prov
		and g10.seccion = f10.seccion
		and g10.distrito = f10.distrito)
FROM F10_MUN_2015  f10,
     F03_MUN_2015  f3,
     F05_1_MUN_2015  f5
where f3.cod_cand = f10.cod_cand
and   f5.cod_mun = f10.cod_mun
and   f10.cod_ccaa = f5.cod_ccaa
and   f10.cod_prov = f5.cod_prov
and   f5.municipio = "Alcorcón";
