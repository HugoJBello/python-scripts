
import os
from functools import reduce

class Helpers:
    def __init__(self):
        pass

    #directory should be a relative path to the api root folder
    def find_files_in_dir(directory:str):
        file_path=os.path.abspath(__file__)
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
        directory_path = os.path.join(root_path,directory)
        if not os.path.isdir(directory_path):
            return []

        files_schema = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if ".avsc" in file:
                    files_schema.append(file)
        return files_schema

    def missing_key_files(files:list):
        value_schema_files = list(filter (lambda filename:"-value.avsc" in filename, files))
        result = []
        for value_schema in value_schema_files:
            if not (value_schema.replace("-value.avsc","-key.avsc") in files):
                result.append(value_schema)
        return result