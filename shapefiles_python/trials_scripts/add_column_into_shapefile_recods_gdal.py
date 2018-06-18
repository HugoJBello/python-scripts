#pip3 install gdal
#sudo apt install gdal-bin python3-gdal
#https://gis.stackexchange.com/questions/152076/where-can-i-find-gdal-python-bindings-for-python-3-4

from osgeo import ogr

fn = r"13006SECC_CPV_E_20111101_01_R_INE_MADRID.shp"  # The path of your shapefile
layer_name = fn.replace("data/","").replace(".shp","")
cca="'13'"

ds = ogr.Open(fn, True)  # True allows to edit the shapefile

layer = ds.GetLayer()

new_col="TEST_COLUMN2"
new_layer_name=layer_name + "_" + new_col
layer_new = ds.CopyLayer(layer, new_layer_name)

new_field = ogr.FieldDefn(new_col, ogr.OFTString)
layer_new.CreateField(new_field)


layerDefinition = layer_new.GetLayerDefn()
for i in range(layerDefinition.GetFieldCount()):
    print(layerDefinition.GetFieldDefn(i).GetName()) 