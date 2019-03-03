import numpy as np
from collections import namedtuple
from openBOS.imageStack import ImageStack, imagestack_from_images


Settings = namedtuple("diffBOS_settings", ["First_img_id", "N_imgs", "Ref_rolling", "Ref_stack_depth"])
Settings.__new__.__defaults__ = (0, None, False, 1)

class diffBOS(object):
    def __init__(self,image_stack,settings):
        if not isinstance(image_stack,ImageStack):
            raise ValueError("Only instances of ImageStack is accepted")

        self._image_stack_ =image_stack


        self._n_imgs_ = min(settings.N_imgs,self._image_stack_.n_imgs)

        if isinstance(settings, Settings):
            self._settings_ = settings

        if not settings.Ref_rolling:
            self.background_static = self._average_images_(0,settings.Ref_stack_depth)
            self.background = lambda _:self.background_static

        else:
            self.background = lambda frame: self._average_images_(frame, frame+settings.Ref_stack_depth)


    def _average_images_(self,start,stop):
        reference_stack = np.array([self._image_stack_(i) for i in range(start,stop)])
        return np.average(reference_stack,axis=0)

    def run(self):
        diff_stack = []
        for i,img in enumerate(self._image_stack_):
            if i>self._n_imgs_:
                break
            print("Processing frame nr: %i")%i
            diff_stack.append(self.__diff_images__(img,self.background(i)))
        return imagestack_from_images(diff_stack,filter=None)

    def __diff_images__(self,image,background):
        return np.abs(image-background) # <- "Schlieren"





