import yt
import os

snapshot_folder = "ex1/hdf5"

for i in range(20):
    snapshot_name = f"snapshot_{i:03d}.hdf5"
    snapshot_path = os.path.join(snapshot_folder, snapshot_name)
    ds = yt.load(snapshot_path)

    # Create a 2D particle plot of mass
    plot = yt.ParticlePlot(ds, "particle_position_x", "particle_position_y", ("PartType1", "particle_mass"))

    # Optional: tweak style
    plot.set_cmap(("PartType1", "particle_mass"), "viridis")
    plot.set_log(("PartType1", "particle_mass"), True)
    plot.annotate_title("Dark Matter Particle Plot (Mass)")

    plot.save(f"ex1/dm_particle_plot_{i:03d}.png")



# import yt
# import os

# # Folder where your .hdf5 snapshots live
# snapshot_folder = "ex2/hdf5"
# output_folder = "plots"

# # Make output directory if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Loop over snapshot_000.hdf5 to snapshot_045.hdf5
# for i in range(46):
#     snapshot_name = f"snapshot_{i:03d}.hdf5"
#     snapshot_path = os.path.join(snapshot_folder, snapshot_name)

#     # Load the dataset
#     ds = yt.load(snapshot_path)

#     # Create the 2D particle phase plot
#     plot = yt.ParticlePhasePlot(ds,
#                                 ("PartType1", "particle_position_x"),
#                                 ("PartType1", "particle_position_y"),
#                                 ("PartType1", "particle_mass"))

#     # Customize plot
#     plot.set_cmap(("PartType1", "particle_mass"), "viridis")
#     plot.set_log(("PartType1", "particle_mass"), True)

#     # Set axis range manually
#     xlim = (-7000, 7000)
#     ylim = (-7000, 7000)
#     plot.set_xlim(*xlim)
#     plot.set_ylim(*ylim)

#     plot.plots[("PartType1", "particle_mass")].axes.set_title(
#         f"Dark Matter Particle Phase Plot — {snapshot_name}"
#     )

#     # Save to plots/dm_particle_phase_plot_###.png
#     output_filename = os.path.join(output_folder, f"dm_particle_phase_plot_{i:03d}.png")
#     plot.save(output_filename)

#     print(f"Saved {output_filename}")
