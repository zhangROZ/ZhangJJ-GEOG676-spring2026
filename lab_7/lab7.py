import arcpy

source = r'D:\Spring2026_Courses\GEOG676\ZhangJJ-GEOG676-spring2026\lab_7'
band1 = arcpy.sa.Raster(source + r'\landsat4\blue.tif')
band2 = arcpy.sa.Raster(source + r'\landsat4\green.tif')
band3 = arcpy.sa.Raster(source + r'\landsat4\red.tif')
band4 = arcpy.sa.Raster(source + r'\landsat4\nir08.tif')

combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r'\output_combined.tif')

azimuth = 315
altitude = 45

shadows = 'NO_SHADOWS'
z_factor = 1

arcpy.ddd.HillShade(source + r'\dem\dem_30m.tif', source +  r'\output_Hillshade.tif', azimuth= azimuth, altitude= altitude, model_shadows=shadows, z_factor= z_factor)

output_measurement = 'DEGREE'
z_factor = 1
arcpy.ddd.Slope(source +  r'\output_combined.tif', source +  r'\output_slope.tif', output_measurement, z_factor)
print('success~')