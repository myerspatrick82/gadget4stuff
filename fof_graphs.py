import h5py

with h5py.File("bak-fof_tab_000.hdf5", "r") as f:
    group_lengths = f["Group/GroupLen"][:]
    group_masses = f["Group/GroupMass"][:]
    group_positions = f["Group/GroupPos"][:]
    print(group_lengths[:5])
