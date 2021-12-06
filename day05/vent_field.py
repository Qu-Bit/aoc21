"""AoC 2021: day**/
    + puzzle1
    + puzzle2
"""

# %% imports
import numpy as np
from numpy.core.numeric import zeros_like
import matplotlib.pyplot as plt

# %% input data

do_debug = False  # or True

in_Fp = "test_input.txt"
if not do_debug:
    in_Fp = "input.txt"


def input_reader(file):
    print("* reading file:", file)
    res = None
    with open(file, "r") as fh:
        lines = list(map(str.strip, fh.readlines()))
        res = [
            [list(map(int, f[0].split(","))), list(map(int, f[2].split(",")))]
            for f in map(str.split, lines)
        ]
    return res


# %%

vent_lines = np.array(input_reader(in_Fp))

max_dims = vent_lines.max(axis=1).max(axis=0)
min_dims = vent_lines.min(axis=1).min(axis=0)
horiz_dims = max_dims - min_dims
print(max_dims)
print(min_dims)
print(horiz_dims)

# %% set up scan field
scan_horizon = np.zeros(horiz_dims + 1, dtype=int)

# %% generate plot lines


def mark_vent_line(vl, only_straight_lines=True):
    l_scan_hor = np.zeros_like(scan_horizon)

    # number of fields to fill
    crd_diffs = np.diff(vl.T)
    if only_straight_lines:
        if not np.any(crd_diffs == 0):
            # return empty
            return l_scan_hor

    steps = np.abs(crd_diffs).max() + 1
    plot_pos = [
        np.linspace(d_lims[0], d_lims[1], num=steps, dtype=int) for d_lims in vl.T
    ]
    # print(plot_pos)
    # actual plotting
    for pos in np.r_[plot_pos].T:
        pos -= min_dims
        l_scan_hor[pos[0], pos[1]] += 1
    return l_scan_hor


# flag for only straight lines
only_straight = False or True

vent_crit_lvl = 2

# %% puzzle 1
print("---\npuzzle 1:")

for vl in vent_lines:
    # print(vl)
    l_scan_hor = mark_vent_line(vl, only_straight)
    # print(l_scan_hor)

    scan_horizon += l_scan_hor
# print(scan_horizon)
plt.matshow(scan_horizon)

print("results: (only straight: %s)" % only_straight)
print(
    "* critical vent crossings (>= %d):" % vent_crit_lvl,
    (scan_horizon >= vent_crit_lvl).sum(),
)
# %% puzzle 2
print("---\npuzzle 2:")

# reset scan field
scan_horizon = np.zeros(horiz_dims + 1, dtype=int)

# with flag
only_straight = False

for vl in vent_lines:
    # print(vl)
    l_scan_hor = mark_vent_line(vl, only_straight)
    # print(l_scan_hor)

    scan_horizon += l_scan_hor
# print(scan_horizon)
plt.matshow(scan_horizon)

print("results: (only straight: %s)" % only_straight)
print(
    "* critical vent crossings (>= %d):" % vent_crit_lvl,
    (scan_horizon >= vent_crit_lvl).sum(),
)

# %%
