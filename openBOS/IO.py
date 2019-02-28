import os

def list_images_in_folder(path,file_type = ".tif"):
        return sorted([file for file in os.listdir(path) if file.endswith(file_type)])

