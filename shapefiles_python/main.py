from cusec_shapefield_filter_generator_gdal import CusecShapefiledFilterGDAL



def main():
    data_parameters=[["13","045"]]
    shapefile="data/result.shp"
    output_folder = "data"
    cusecShapefileFilter = CusecShapefiledFilterGDAL(shapefile,data_parameters,output_folder)
    cusecShapefileFilter.extract_cusecs_shapefiles()
if __name__ == '__main__':
	main()
