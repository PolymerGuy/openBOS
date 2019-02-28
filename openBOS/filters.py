import scipy.ndimage as nd
import numpy as np

def filter_image(image,filter_type="gaussian",sigma=2.0):
    if not isinstance(image,np.ndarray) or image.ndim != 2:
        raise ValueError("Only BW images are supported")

    img = image.copy()
    if filter_type is "gaussian":
        img = nd.gaussian_filter(image,sigma=sigma)

    elif filter_type is "gaussian_highpass":
        img = img-nd.gaussian_filter(image,sigma=sigma)
    
    else:
        raise ValueError("Invalid filter type received")

    return img
