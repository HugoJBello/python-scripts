from cusec_shapefield_filter_generator_gdal import CusecShapefiledFilterGDAL



def main():
    data_parameters=[["13","006"],["13","045"],["13","007"],
    ["13","009"],["13","007"],["13","013"],["13","014"],["13","023"],["13","022"],["13","040"],["13","047"],["13","007"]]

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

    shapefile="data/SECC_CPV_E_20111101_01_R_INE_MADRID.shp"
    output_folder = "data"
    cusecShapefileFilter = CusecShapefiledFilterGDAL(shapefile,output_folder)
    cusecShapefileFilter.extract_cusecs_shapefiles_by_nmun(nombres_municipios)
if __name__ == '__main__':
	main()
