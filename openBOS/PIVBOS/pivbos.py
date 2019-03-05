import numpy as np
from collections import namedtuple
from openBOS.imageStack import ImageStack, imagestack_from_images

import openpiv.tools
import openpiv.process
import openpiv.scaling

Settings = namedtuple("diffBOS_settings", ["First_img_id", "N_imgs", "window_size", "overlap",
                                           "dt", "search_area_size",
                                           "sig2noise_method"])
Settings.__new__.__defaults__ = (0, None, False, 1)


class PIVBOS(object):
    def __init__(self, image_stack, settings):
        if not isinstance(image_stack, ImageStack):
            raise ValueError("Only instances of ImageStack is accepted")

        self._image_stack_ = image_stack

        self._n_imgs_ = min(settings.N_imgs, self._image_stack_.n_imgs)

        if isinstance(settings, Settings):
            self._settings_ = settings

    def run(self):
        umag_t = []

        for i, img in enumerate(self._image_stack_):
            if i > self._n_imgs_:
                break

            if i == 0:
                frame_a = img.astype(np.int32)
                frame_b = img.astype(np.int32)
                pass
            else:
                frame_a = frame_b
                frame_b = img.astype(np.int32)

                umag = self.__diff_images__(frame_a,frame_b)

                print("Processing frame nr: %i") % i

                umag_t.append(umag)
        return imagestack_from_images(umag_t, filter=None)

    def __diff_images__(self, frame_a, frame_b):
        u, v, sig2noise = openpiv.process.extended_search_area_piv(frame_a,
                                                                   frame_b,
                                                                   window_size=self._settings_.window_size,
                                                                   overlap=self._settings_.overlap,
                                                                   dt=self._settings_.dt,
                                                                   search_area_size=self._settings_.search_area_size,
                                                                   sig2noise_method=self._settings_.sig2noise_method)
        return np.sqrt(u ** 2. + v ** 2.)

