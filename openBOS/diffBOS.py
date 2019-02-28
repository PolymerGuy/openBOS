import numpy as np
from collections import namedtuple


DiffBOS_settings = namedtuple("diffBOS_settings",["First_img_id","N_imgs","Ref_rolling","Ref_stack_depth"])


class diffBOS(object):
    def __init__(self,image_stack,settings):
        if isinstance(image_stack,ImageStack):
            self._image_stack_ =image_stack

        self._n_imgs_ = min(settings.N_imgs,len(self._image_stack_)) 

        if isinstance(settings,DiffBOS_settings):
            self._settings_ = settings

        if self._settings_

    def run(self):
        diff_stack = []
        for i,img in enumerate(self._image_stack_):
            diff_stack.append(self.__diff_images__(img,self.background(i)))
        return diff_stack

    def __diff_images__(image,background):
        return diff = np.abs(images[i,:,:]-background) # <- "Schlieren"





