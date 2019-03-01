import os
import scipy.ndimage as nd


# TODO: Implement this
class ImageStack(object):
    def __init__(self,img_paths,lazy=True,filter=None):
        self.img_paths = img_paths
        self.n_imgs = len(img_paths)
        self.lazy = lazy
        self.current_frame = 0

        if not filter:
            self.filter = lambda img:img

        if lazy:
            self.images = lambda frame:nd.imread(self.img_paths[frame])
        else:

            self.image_stack =[self.import_image(img_path) for img_path in img_paths]
            self.images = lambda frame:self.image_stack[frame]


    def set_filter(self,filter):
        self.filter = filter


    def __iter__(self):
        return self

    def next(self):
        if self.current_frame > self.n_imgs:
            raise StopIteration
        else:
            self.current_frame += 1
            return self.filter(self.images(self.current_frame))

    def __call__(self, frame):
        return self.filter(self.images(frame))


# TODO: Implement this
def ImageStackFromFolder(path_folder, file_suffix=".tif", lazy=True):
    img_names = list_images_in_folder(path_folder, file_type=file_suffix)
    img_paths = [path_folder + img_name for img_name in img_names]

    return ImageStack(img_paths,lazy=lazy)


def list_images_in_folder(path, file_type=".tif"):
    return sorted([file for file in os.listdir(path) if file.endswith(file_type)])
