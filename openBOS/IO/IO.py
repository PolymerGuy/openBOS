import os


# TODO: Implement this
def ImageStackFromFolder(path_to_img_folder, file_suffix=".tif", lazy=True):
        raise NotImplementedError("To be done")


def list_images_in_folder(path,file_type = ".tif"):
        return sorted([file for file in os.listdir(path) if file.endswith(file_type)])

