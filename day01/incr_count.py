"""AoC 2021: day01/
    + puzzle1
    + puzzle2
"""

import numpy as np

# %% input data
depth = np.genfromtxt('input.txt')
len(depth)

# %% puzzle 1
print('---\npuzzle 1:')
ddepth = np.diff(depth)
print('*A:* number of successive measurements\n\t'
      'showing increased depth:', sum(ddepth > 0))


# %% puzzle 2
print('---\npuzzle 2:')
sumWin = 3
cs3_dep = np.convolve(depth, [1.,]*sumWin, mode='valid')
assert len(cs3_dep) == (len(depth) - sumWin + 1)

ddepth = np.diff(cs3_dep)
print('*A:* number of successive [%d-]sum-windows\n\t'
      'showing increased depth:' % sumWin, sum(ddepth > 0))
