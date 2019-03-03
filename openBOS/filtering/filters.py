import scipy.ndimage as nd
import numpy as np





def highpass_gaussian(image, sigma=2.0):
    return image - nd.gaussian_filter(image, sigma=sigma)


def lowpass_gaussian(image, sigma=2.0):
    return nd.gaussian_filter(image, sigma=sigma)
