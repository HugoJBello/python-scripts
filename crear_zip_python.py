import os
import zipfile
import datetime


def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)



def extension (filename):
    extension = os.path.splitext(filename)[1][1:]
    return extension

def excluded (filename,list_extensions, list_filenames):
    for ext in list_extensions:
        if extension(filename)== ext:
            return True
    for name in list_filenames:
        if filename == name:
            return True
    return False

def zip_for_backup ():
    source_dir = os.path.dirname(os.path.realpath(__file__))
    output_filename = source_dir.split("\\")[len(source_dir.split("\\"))-1]+"_"+datetime.datetime.now().strftime("%Y%m%d")+".zip"
    excluded_extensions = ["zip", "py"]
    excluded_filenames = []

    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename) and not excluded(filename,excluded_extensions,excluded_filenames):  # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)

def main():
    zip_for_backup()


main()



#make_zipfile(zip_filename,file_path)

#import shutil

#shutil.make_archive(zip_filename, 'zip', file_path)

# info
# http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
#