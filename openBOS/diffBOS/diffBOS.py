import numpy as np
from collections import namedtuple
from openBOS.IO import ImageStack


Settings = namedtuple("diffBOS_settings", ["First_img_id", "N_imgs", "Ref_rolling", "Ref_stack_depth"])
Settings.__new__.__defaults__ = (0, None, False, 1)

class diffBOS(object):
    def __init__(self,image_stack,settings):
        if isinstance(image_stack,ImageStack):
            self._image_stack_ =image_stack

        self._n_imgs_ = min(settings.N_imgs,len(self._image_stack_)) 

        if isinstance(settings, Settings):
            self._settings_ = settings



    def run(self):
        diff_stack = []
        for i,img in enumerate(self._image_stack_):
            diff_stack.append(self.__diff_images__(img,self.background(i)))
        return diff_stack

    def __diff_images__(self,image,background):
        return np.abs(image-background) # <- "Schlieren"





