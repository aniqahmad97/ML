import os
from osgeo import gdal,ogr

import csv

rast=[]
head=['XCoord','YCoord']

for i in os.listdir(r"D:\Test"):
    filename,fileext=os.path.splitext(i)
    if fileext=='.tif':
        print(i)
        rast.append(i)
        head.append(filename)
        
with open("output.csv", "w",newline='') as fp:
       wr = csv.writer(fp, dialect='excel')
       wr.writerow(head)
        
print(head)
foldpath=r"D:\Test"  
ds=ogr.Open(r'D:\Documents\free lancing assigment\dem visualization\test\data.shp')
lyr=ds.GetLayer()



for feat in lyr:
    geom = feat.GetGeometryRef()
    mx,my=geom.GetX(), geom.GetY()  #coord in map units
    list1=[mx,my]
     
    for raster in rast:
        src_ds=gdal.Open(os.path.join(foldpath,raster))
        
        geotransform = src_ds.GetGeoTransform()
        originX = geotransform[0]
        originY = geotransform[3]
       
        pixelWidth = geotransform[1]
        pixelHeight = geotransform[5]
        
        sub1=mx-originX
        sub2=my-originY
       
        xOffset = int((sub1) / pixelWidth)
        yOffset = int((sub2) / pixelHeight) 
    
        rb=src_ds.GetRasterBand(1)
    
        
        
        print(raster)
        data = rb.ReadAsArray(xOffset, yOffset, 1, 1)
        print(data[0][0])
        list1.append(data[0][0])
        
    with open("output.csv", "a",newline='') as fp:
           wr = csv.writer(fp, dialect='excel')
           wr.writerow(list1)
           print(list1)
    
   
