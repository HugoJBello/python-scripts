#pip3 install gdal
#sudo apt install gdal-bin python3-gdal
#https://gis.stackexchange.com/questions/152076/where-can-i-find-gdal-python-bindings-for-python-3-4

from osgeo import ogr

fn = r"data/SECC_CPV_E_20111101_01_R_INE.shp"  # The path of your shapefile
layer_name = fn.replace("data/","").replace(".shp","")
cca="'13'"

ds = ogr.Open(fn, True)  # True allows to edit the shapefile
layer = ds.GetLayer()
layerDefinition = layer.GetLayerDefn()
for i in range(layerDefinition.GetFieldCount()):
    print(layerDefinition.GetFieldDefn(i).GetName()) 


sql ="DELETE FROM " + layer_name + " WHERE CCA != " + cca +";COMMIT"
print(sql)
layer_delete = ds.ExecuteSQL(sql, dialect='SQLITE')
layer2_delete = ds.CopyLayer(layer, layer_name + "_MADRID")
layer_delete = layer2_delete = ds = None

