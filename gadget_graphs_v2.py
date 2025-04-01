import yt
import os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.usetex"] = False
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

# Paths
snapshot_dir = "ex2/hdf5"
output_dir = "plots_multi"
os.makedirs(output_dir, exist_ok=True)

# Plotting function for a single snapshot
def process_snapshot(i):
    snap = f"snapshot_{i:03d}.hdf5"
    path = os.path.join(snapshot_dir, snap)
    outpath = os.path.join(output_dir, f"colliding_galaxies_{i:03d}.png")

    if os.path.exists(outpath):
        print(f"⏩ Skipping {snap} (already exists)")
        return

    try:
        ds = yt.load(path)
        print(f"🔄 Processing {snap}")

        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

                # Dark Matter
        p_dm = yt.ParticlePlot(ds,
                               ("PartType1", "particle_position_x"),
                               ("PartType1", "particle_position_y"),
                               ("PartType1", "particle_mass"),
                               depth=(500, "code_length"))
        p_dm.set_cmap(("PartType1", "particle_mass"), "viridis")
        p_dm.set_log(("PartType1", "particle_mass"), True)
        p_dm.set_background_color(("PartType1", "particle_mass"), "black")
        p_dm.annotate_title(f"Dark Matter — {snap}")
        p_dm.plots[("PartType1", "particle_mass")].colorbar_label = "Particle Mass"
        p_dm.plots[("PartType1", "particle_mass")].figure = fig
        p_dm.plots[("PartType1", "particle_mass")].axes = axes[0]
        p_dm._setup_plots()
        axes[0].set_xlim(-100, 100)
        axes[0].set_ylim(-100, 100)
        axes[0].set_xlabel("x (kpc)")
        axes[0].set_ylabel("y (kpc)")

        # Gas
        p_gas = yt.ParticlePlot(ds,
                                ("PartType0", "particle_position_x"),
                                ("PartType0", "particle_position_y"),
                                ("PartType0", "particle_mass"),
                                depth=(500, "code_length"))
        p_gas.set_cmap(("PartType0", "particle_mass"), "plasma")
        p_gas.set_log(("PartType0", "particle_mass"), True)
        p_gas.set_background_color(("PartType0", "particle_mass"), "black")
        p_gas.annotate_title("Gas")
        p_gas.plots[("PartType0", "particle_mass")].colorbar_label = "Gas Mass"
        p_gas.plots[("PartType0", "particle_mass")].figure = fig
        p_gas.plots[("PartType0", "particle_mass")].axes = axes[1]
        p_gas._setup_plots()
        axes[1].set_xlim(-100, 100)
        axes[1].set_ylim(-100, 100)
        axes[1].set_xlabel("x (kpc)")
        axes[1].set_ylabel("y (kpc)")

        # Stars (if present)
        if ("PartType4", "particle_position_x") in ds.field_list:
            p_star = yt.ParticlePlot(ds,
                                     ("PartType4", "particle_position_x"),
                                     ("PartType4", "particle_position_y"),
                                     ("PartType4", "particle_mass"),
                                     depth=(500, "code_length"))
            p_star.set_cmap(("PartType4", "particle_mass"), "inferno")
            p_star.set_log(("PartType4", "particle_mass"), True)
            p_star.set_background_color(("PartType4", "particle_mass"), "black")
            p_star.annotate_title("Stars")
            p_star.plots[("PartType4", "particle_mass")].colorbar_label = "Star Mass"
            p_star.plots[("PartType4", "particle_mass")].figure = fig
            p_star.plots[("PartType4", "particle_mass")].axes = axes[2]
            p_star._setup_plots()
            axes[2].set_xlim(-100, 100)
            axes[2].set_ylim(-100, 100)
            axes[2].set_xlabel("x (kpc)")
            axes[2].set_ylabel("y (kpc)")
        else:
            axes[2].axis("off")
            axes[2].set_title("No stars (yet)", fontsize=12, color="gray")

        fig.tight_layout()
        fig.savefig(outpath, dpi=150)
        plt.close(fig)
        print(f"✅ Saved {outpath}")

    except Exception as e:
        print(f"❌ Error on {snap}: {e}")


# Run in parallel (adjust max_workers to match your CPU)
with ThreadPoolExecutor(max_workers=1) as executor:
    executor.map(process_snapshot, range(46))
