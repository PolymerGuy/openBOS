import openBOS as bos

# Initial draft on a script representing a typical workflow of an analysis

path_to_img_folder = r"/some/path/"

# Generate an image stack from all images in the folder
images_stack = bos.IO.ImageStackFromFolder(path_to_img_folder, file_suffix=".tif", lazy=True)

# Remove background drift by high-pass filtering the image_stack
image_stack_hp = bos.filtering.filter_image_stack(images_stack, filter=bos.filtering.highpass_gaussian)

# Define the settings for the analysis
settings = bos.diffBOS.Settings(First_img_id=0,
                                        N_imgs=100,
                                        Ref_rolling=False,
                                        Ref_stack_depth=10)

# Initialize and run an analysis
bos_job = bos.diffBOS.diffBOS(image_stack_hp, settings=settings)
bos_res = bos_job.run()

bos_res_blurred = bos.filtering.filter_image_stack(bos_res, filter=bos.filtering.lowpass_gaussian)

# Show results
visualisation = bos.visualize(bos_res)
visualisation.show_frame(15)
visualisation.save_frame(45)
