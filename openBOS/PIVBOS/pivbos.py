import numpy as np
from collections import namedtuple
from openBOS.imageStack import ImageStack, imagestack_from_images

import openpiv.tools
import openpiv.process
import openpiv.scaling

Settings = namedtuple("diffBOS_settings", ["First_img_id", "N_imgs", "Ref_rolling", "Ref_stack_depth"])
Settings.__new__.__defaults__ = (0, None, False, 1)

class PIVBOS(object):
    def __init__(self,image_stack,settings):
        if not isinstance(image_stack,ImageStack):
            raise ValueError("Only instances of ImageStack is accepted")

        self._image_stack_ =image_stack


        self._n_imgs_ = min(settings.N_imgs,self._image_stack_.n_imgs)

        if isinstance(settings, Settings):
            self._settings_ = settings




    def _average_images_(self,start,stop):
        reference_stack = np.array([self._image_stack_(i) for i in range(start,stop)])
        return np.average(reference_stack,axis=0)

    def run(self):
        umag_t = []




        for i,img in enumerate(self._image_stack_):
            if i>self._n_imgs_:
                break

            if i==0:
                frame_a = img.astype(np.int32)
                frame_b = img.astype(np.int32)
                pass
            else:
                frame_a = frame_b
                frame_b = img.astype(np.int32)

                u, v, sig2noise = openpiv.process.extended_search_area_piv(frame_a, frame_b, window_size=24, overlap=12,
                                                                           dt=0.02, search_area_size=64,
                                                                           sig2noise_method='peak2peak')
                print("Processing frame nr: %i")%i
                umag = np.sqrt(u**2.+v**2.)

                umag_t.append(umag)
        return imagestack_from_images(umag_t,filter=None)

    def __diff_images__(self,image,background):
        return np.abs(image-background) # <- "Schlieren"