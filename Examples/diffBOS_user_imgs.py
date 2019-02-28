import openBOS as bos

# Initial draft on a script representing a typical workflow of an analysis

path_to_img_folder = r"./images/"

# Generate an image stack from all images in the folder
image_stack = bos.IO.ImageStackFromFolder(path_to_img_folder, file_suffix=".tif", lazy=True)

# Remove background drift by high-pass filtering the image_stack
# image_stack.set_filter(bos.filtering.highpass_gaussian)

# Define the settings for the analysis
settings = bos.diffBOS.Settings(First_img_id=0,
                                        N_imgs=150,
                                        Ref_rolling=False,
                                        Ref_stack_depth=10)

# Initialize and run an analysis
bos_job = bos.diffBOS.diffBOS(image_stack, settings=settings)
bos_res = bos_job.run()

#bos_res_blurred = bos_res.set_filter(filter=bos.filtering.lowpass_gaussian)

# Show results
visualisation = bos.Visualizer(bos_res)
visualisation.show_frame(60)
visualisation.save_frame(45)
