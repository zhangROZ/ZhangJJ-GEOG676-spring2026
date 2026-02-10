import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Spring2026_Courses\GEOG676\ZhangJJ-GEOG676-spring2026\lab_4\env"
folder_path = r"D:\Spring2026_Courses\GEOG676\ZhangJJ-GEOG676-spring2026\lab_4"
gdb_name = 'Test.gdb'
gdb_path = folder_path + "\\" + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

# Buffer distance input
Buffer_distance_input = input("Please enter a Buffer distance, unit: meter: ")

# Read XY
csv_path = r'D:\Spring2026_Courses\GEOG676\ZhangJJ-GEOG676-spring2026\lab_4\garages.csv'
garage_layer_name = "Garage_Points"
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + "\\" + garage_layer_name

# Read Campus
campus = r'D:\Spring2026_Courses\GEOG676\ZhangJJ-GEOG676-spring2026\lab_4\Campus.gdb'
buildings_campus = campus + '\\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# Re-project
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\\Garage_Points_reprojected', spatial_ref)

# Buffer
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\\Garage_Points_reprojected', gdb_path + '\\Garage_Points_buffered', Buffer_distance_input)

# Intersect
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\\Garage_Buildings_Intersection', 'ALL')

# Save
arcpy.TableToTable_conversion(gdb_path + '\\Garage_Buildings_Intersection', folder_path, 'nearbyBuildings.csv')

