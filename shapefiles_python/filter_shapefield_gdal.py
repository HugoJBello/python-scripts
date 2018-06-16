#pip3 install gdal
#sudo apt install gdal-bin python3-gdal
#https://gis.stackexchange.com/questions/152076/where-can-i-find-gdal-python-bindings-for-python-3-4

from osgeo import ogr

fn = r"data/SECC_CPV_E_20111101_01_R_INE.shp"  # The path of your shapefile
ds = ogr.Open(fn, True)  # True allows to edit the shapefile
layer = ds.GetLayer()
layerDefinition = layer.GetLayerDefn()
for i in range(layerDefinition.GetFieldCount()):
    print(layerDefinition.GetFieldDefn(i).GetName()) 

count=layer.GetFeatureCount()
for feature in range(count):
    ds.ExecuteSQL('REPACK ' + layer.GetName())
    if (layer.GetFeature(feature).items()["CCA"]!=13):
        ds.ExecuteSQL('REPACK ' + layer.GetName())
        layer.DeleteFeature(feature)
