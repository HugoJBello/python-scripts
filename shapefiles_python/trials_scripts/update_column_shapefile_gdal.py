#pip3 install gdal
#sudo apt install gdal-bin python3-gdal
#https://gis.stackexchange.com/questions/152076/where-can-i-find-gdal-python-bindings-for-python-3-4

from osgeo import ogr

fn = r"13006SECC_CPV_E_20111101_01_R_INE_MADRID_TEST_COLUMN2.shp"  # The path of your shapefile
layer_name = fn.replace("data/","").replace(".shp","")
cca="'13'"

ds = ogr.Open(fn, True)  # True allows to edit the shapefile

layer = ds.GetLayer()

feature = layer.GetNextFeature()

val = 111
col="TEST_COLUM"

while feature:
    feature.SetField(col, val)
    layer.SetFeature(feature)
    print(feature)
    feature = layer.GetNextFeature()