#pip3 install pyshp
import shapefile

#Read the original shapefile and create a new one adding one new field
sh_reader = shapefile.Reader('SECC_CPV_E_20111101_01_R_INE')
sh_writer = shapefile.Writer()
shapes = sh_reader.shapes() # -> the geometries in a list
fields = sh_reader.fields[1:]
fields_name = [field[0] for field in fields] 
print(fields_name)

records = sh_reader.records()
print(records[75])

#Add new record programatically
sh_writer.fields = list(sh_reader.fields)

for rec in sh_reader.records():
    #print(rec[7])
    # Add the modified record to the new shapefile 
    if (rec[6]=='28'):
        sh_writer.records.append(rec)
        print(rec)

sh_writer._shapes.extend(sh_reader.shapes())
#sh_writer.save("SECC_CPV_E_20111101_01_R_INE_MOD") 

#Then copy the prj and sbn files from the original