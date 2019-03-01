import matplotlib.pyplot as plt
from scipy.ndimage import histogram

# TODO: Implement this
class Visualizer(object):
    def __init__(self,bos_res):
        self.results = bos_res
        self.n_frames = len(self.results)

    def show_frame(self,frame):
        vmax = self.results[frame].max()
        vmin = self.results[frame].min()

        plt.imshow(self.results[frame],vmin=vmin*1.1 ,vmax=vmax*0.9 ,cmap=plt.cm.magma)
        plt.show()

    def save_frame(self,frame):
        raise NotImplementedError()