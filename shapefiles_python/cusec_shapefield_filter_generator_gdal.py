#pip3 install gdal
#sudo apt install gdal-bin python3-gdal
#https://gis.stackexchange.com/questions/152076/where-can-i-find-gdal-python-bindings-for-python-3-4
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal

#install python 3.7 and run   pip3 install GDAL-2.2.4-cp37-cp37m-win_amd64.whl

from osgeo import ogr
class CusecShapefiledFilterGDAL:
    def __init__(self,data_shapefile,output_folder):
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

    def extract_cusecs_shapefiles_by_cmun(self,data_params_array):
        for item in data_params_array:
            cca= item[0]
            cmun= item[1]            
            layer_new = self.extract_layer_by_cmun_cca(cmun,cca)
            result = layer_new =  None
        
    def extract_cusecs_shapefiles_by_nmun(self,data_nmuns_array):
            for item in data_nmuns_array:
                nmun= item            
                layer_new = self.extract_layer_by_nmun(nmun)
                result = layer_new =  None
    
    def extract_layer_by_nmun(self,nmun):
        sql ="SELECT * FROM " + self.layer_name + " WHERE NMUN = '" + nmun+ "';COMMIT"
        new_layer_name = nmun +"_"+ self.layer_name
        print (new_layer_name + "\n" + sql)
        result = self.data_source.ExecuteSQL(sql, dialect='SQLITE')
        layer_new = self.data_source.CopyLayer(result, new_layer_name)
        result=None
        return layer_new

    def extract_layer_by_cmun_cca(self,nmun,cca):
        sql ="SELECT * FROM " + self.layer_name + " WHERE CMUN = '" + cmun+ "';COMMIT"
        new_layer_name = nmun +"_"+ self.layer_name
        print (new_layer_name + "\n" + sql)
        result = self.data_source.ExecuteSQL(sql, dialect='SQLITE')
        layer_new = self.data_source.CopyLayer(result, new_layer_name)
        result=None
        return layer_new

