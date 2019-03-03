import openBOS as bos
import matplotlib.pyplot as plt

# Initial draft on a script representing a typical workflow of an analysis

path_to_img_folder = r"./images/"

# Generate an image stack from all images in the folder
image_stack = bos.imageStack.imagestack_from_folder(path_to_img_folder, file_suffix=".tif", lazy=True)

# Remove background drift by high-pass filtering the image_stack
image_stack.set_filter(bos.filtering.highpass_gaussian,sigma=2)

# visualisation = bos.Visualizer(image_stack)
# visualisation.show_frame(10)


# Define the settings for the analysis
settings = bos.diffBOS.Settings(First_img_id=0,
                                        N_imgs=150,
                                        Ref_rolling=False,
                                        Ref_stack_depth=10)

# Initialize and run an analysis
bos_job = bos.diffBOS.diffBOS(image_stack, settings=settings)
bos_res = bos_job.run()

bos_res.set_filter(filter=bos.filtering.lowpass_gaussian,sigma=1)

# Show results
visualisation = bos.Visualizer(bos_res)
visualisation.show_frame(60)
visualisation.save_frame(45)
