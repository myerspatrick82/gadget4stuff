# import yt

# ds = yt.load("ex2\snapshot_000.hdf5")

# # Create a 2D particle plot of mass
# plot = yt.ParticlePlot(ds, "particle_position_x", "particle_position_y", ("PartType1", "particle_mass"))

# # Optional: tweak style
# plot.set_cmap(("PartType1", "particle_mass"), "viridis")
# plot.set_log(("PartType1", "particle_mass"), True)
# plot.annotate_title("Dark Matter Particle Plot (Mass)")

# plot.save("dm_particle_plot_002.png")
import yt

# Load the dataset
ds = yt.load("ex2/snapshot_002.hdf5")

# Create the 2D particle phase plot
plot = yt.ParticlePhasePlot(ds,
                            ("PartType1", "particle_position_x"),
                            ("PartType1", "particle_position_y"),
                            ("PartType1", "particle_mass"))

# Customize appearance
plot.set_cmap(("PartType1", "particle_mass"), "viridis")
plot.set_log(("PartType1", "particle_mass"), True)

# Manually set the title (this bypasses yt's internal ambiguity issue)
plot.plots[("PartType1", "particle_mass")].axes.set_title("Dark Matter Particle Phase Plot")

# Save the result
plot.save("dm_particle_phase_plot_002.png")
