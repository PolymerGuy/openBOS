import matplotlib.pyplot as plt
from scipy.ndimage import histogram


# TODO: Implement this
class Visualizer(object):
    def __init__(self, bos_res):
        self.results = bos_res
        self.n_frames = len(self.results)

    def show_frame(self, frame, clip=False, **kwargs):


        vmax = self.results(frame).max()
        vmin = self.results(frame).min()


        if not kwargs:
            plt.imshow(self.results(frame), vmin=vmin, vmax=vmax, cmap=plt.cm.magma)
        else:
            plt.imshow(self.results(frame), **kwargs)
        plt.show()

    def save_frame(self, frame):
        raise NotImplementedError()
