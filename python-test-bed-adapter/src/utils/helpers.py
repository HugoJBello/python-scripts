
import os

class Helpers:
    def __init__(self):
        pass

    def find_files_in_dir(self,directory:str):
        if not os.path.isdir(directory):
            return []

        files = []
        for filename in os.listdir(directory):
            if ".avsc" in filename:
                files.append(filename)
        return files

    def find_missing_key_files(self,files:list):
        pass