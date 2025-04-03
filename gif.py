import imageio.v2 as imageio
import os

# Folder where your images are saved
# plot_folder = "plots"
output_gif = "filamentary.gif"

# Get all the phase plot images in sorted order
image_filenames = [f"dm_particle_plot_{i:03d}.png" for i in range(20)]
image_paths = [os.path.join("ex1", fname) for fname in image_filenames]

# Read and compile images into a gif
with imageio.get_writer(output_gif, mode='I', duration=0.3) as writer:
    for filename in image_paths:
        if os.path.exists(filename):
            image = imageio.imread(filename)
            writer.append_data(image)
            print(f"Added {filename} to GIF")
        else:
            print(f"WARNING: {filename} not found!")

print(f"\nGIF saved as: {output_gif}")
