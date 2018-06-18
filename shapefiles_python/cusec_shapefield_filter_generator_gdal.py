#pip3 install gdal
#sudo apt install gdal-bin python3-gdal
#https://gis.stackexchange.com/questions/152076/where-can-i-find-gdal-python-bindings-for-python-3-4
#pip3 install GDAL-2.2.4-cp37-cp37m-win_amd64.whl
from osgeo import ogr
class CusecShapefiledFilterGDAL:
    def __init__(self,data_shapefile,c_mun_cca_array,output_folder):
        self.data_params_array = c_mun_cca_array
        self.data_shapefile=data_shapefile
        self.output_folder=output_folder
        self.layer_name =""

        self.set_layer_and_ds()
        #self.extract_cusecs_shapefiles()
        
    def set_layer_and_ds(self):
        splitted=self.data_shapefile.split("/")
        self.layer_name = splitted[len(splitted)-1].replace(".shp","")

        self.data_source = ogr.Open(self.data_shapefile, True)  # True allows to edit the shapefile
        self.layer = self.data_source.GetLayer()

    def extract_cusecs_shapefiles(self):
        for item in self.data_params_array:
        
            cca= item[0]
            cmun= item[1]            
            sql ="SELECT * FROM " + self.layer_name + " WHERE CMUN = '" + cmun+ "';COMMIT"
            new_layer_name = cca + cmun + self.layer_name
            print (new_layer_name + "\n" + sql)
            result = self.data_source.ExecuteSQL(sql, dialect='SQLITE')
            layer2_new = self.data_source.CopyLayer(result, new_layer_name)
            result = layer2_new =  None
        


