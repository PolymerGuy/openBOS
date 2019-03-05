import openBOS as bos
import matplotlib.pyplot as plt

# Initial draft on a script representing a typical workflow of an analysis

path_to_img_folder = r"./images/"

# Generate an image stack from all images in the folder
image_stack = bos.imageStack.imagestack_from_folder(path_to_img_folder, file_suffix=".tif", lazy=True)

# Remove background drift by high-pass filtering the image_stack
image_stack.set_filter(bos.filtering.highpass_gaussian,sigma=10)

# visualisation = bos.Visualizer(image_stack)
# visualisation.show_frame(10)


# Define the settings for the analysis
settings = bos.PIVBOS.Settings(First_img_id=0,
                                        N_imgs=150,
                               window_size=24, overlap=12,
                               dt=0.02, search_area_size=64,
                               sig2noise_method='peak2peak')

# Initialize and run an analysis
bos_job = bos.PIVBOS.PIVBOS(image_stack, settings=settings)
bos_res = bos_job.run()

bos_res.set_filter(filter=bos.filtering.lowpass_gaussian,sigma=1)

# Show results
visualisation = bos.Visualizer(bos_res)
visualisation.show_frame(60,vmax=20)
visualisation.save_frame(2)
