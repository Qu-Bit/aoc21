"""AoC 2021: day01/puzzle1
"""
depth = np.genfromtxt('input.txt')
len(depth)

ddepth = np.diff(depth)
print('number of successive measurements showing increased depth:', sum(ddepth > 0))

