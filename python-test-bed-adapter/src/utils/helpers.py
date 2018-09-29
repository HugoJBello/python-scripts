
import os
from functools import reduce
import collections
import os
import pathlib


def scantree_recursive(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree_recursive(entry.path)  # see below for Python 2.x
        else:
            yield entry

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

        for entry in scantree_recursive(directory_path):
            if entry.is_file():
                files_schema.append(entry.path)
        return files_schema



    def missing_key_files(files:list):
        value_schema_files = list(filter (lambda filename:"-value.avsc" in filename, files))
        result = []
        for value_schema in value_schema_files:
            key_schema = value_schema.replace("-value.avsc","-key.avsc")
            if not (key_schema in files):
                result.append(key_schema)
        return result