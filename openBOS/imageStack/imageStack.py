import os
import scipy.ndimage as nd
from copy import copy
from functools import partial
import numpy as np
import os

# TODO: Implement this
class ImageStack(object):
    def __init__(self, image_reader,n_imgs, filter=None):

        self.current_frame = 0

        self.image_reader = image_reader

        self.n_imgs = n_imgs

        if not filter:
            self.filter = lambda img: img

    def set_filter(self, filter,sigma=20.):
        if filter is None:
            self.filter = lambda img: img
        else:
            self.filter = partial(filter,sigma=sigma)

    def __iter__(self):
        return self

    def next(self):
        if self.current_frame > self.n_imgs:
            raise StopIteration
        else:
            self.current_frame += 1
            return self.filter(self.image_reader(self.current_frame))

    def __call__(self, frame):
        return self.filter(self.image_reader(frame))

    def __len__(self):
        return self.n_imgs


# TODO: Implement this
def imagestack_from_folder(path_folder, file_suffix=".tif", lazy=True, filter=None):
    img_names = list_images_in_folder(path_folder, file_type=file_suffix)
    img_paths = [path_folder + img_name for img_name in img_names]

    if lazy:
        image_reader = lambda frame: nd.imread(img_paths[frame]).astype(np.float64)
        return ImageStack(image_reader, len(img_paths), filter)
    else:
        images = [nd.imread(path_img).astype(np.float64) for path_img in img_paths]
        image_reader = lambda frame: images[frame]
        return ImageStack(image_reader,len(img_paths), filter)


def imagestack_from_images(images, filter=None):
    if not isinstance(images[0],np.ndarray) or type(images)!= list:
        raise IOError("Only a list of numpy arrays is accepted as input")
    imgs = copy(images)
    image_reader = lambda frame: imgs[frame]
    return ImageStack(image_reader,len(images), filter)


def list_images_in_folder(path, file_type=".tif"):
    return sorted([file for file in os.listdir(path) if file.endswith(file_type)])
