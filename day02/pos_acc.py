
"""AoC 2021: day02/
    + puzzle1
    + puzzle2
"""

import numpy as np

do_debug = False #or True

# %% input data
in_Fn = 'input.txt'
if do_debug:
    in_Fn = 'test_input.txt'

with open(in_Fn) as fh:
    rdata = fh.readlines()
    rdata = list(map(str.split, rdata))
    print('data entries:', len(rdata))

# define replacement map x,depth
repl_map = {
    'up':       [0, -1],
    'down':     [0, 1],
    'forward':  [1, 0],
    #'back   ':  [-1, 0],
}

# %% puzzle 1
print('---\npuzzle 1:')
# make instructions into position shifts in x,y
steps = np.array([np.r_[repl_map[l[0]]]*int(l[1]) for l in rdata])

# cumulate steps
print(cuml_steps := steps.cumsum(axis=0))

# final x*y
print('*A:* final position:', cuml_steps[-1])
print('*A:* final product:', np.prod(cuml_steps[-1]))


# %% puzzle 2
print('---\npuzzle 2:')

# define replacement map x,depth,aim
repl_map = {
    'up':       lambda s: np.r_[[0, -1, -1]],
    'down':     lambda step: np.r_[[0, +1, +1]],
    'forward':  lambda step: [+1, 0, ],
    #'back   ':  [-1, 0],
}

def move(state, step):
    #x,d,a = state
    #dx,dd,da = update
    sz = int(step[1])
    if step[0] == 'up':
        return (state + np.r_[[+0, +0, -1]]*sz)
    elif step[0] == 'down':
        return (state + np.r_[[+0, +0, +1]]*sz)
    elif step[0] == 'forward':
        return (state + np.r_[[+1*sz, +state[2]*sz, +0]])
    else:
        raise ValueError(f'movement undefined: {step[0]}')

pos = [np.r_[(0,)*3],]

for step in rdata:
    pos.append(move(pos[-1], step))
    if do_debug:
        print(     pos[-2], step)
        print('Δ: ', pos[-1] - pos[-2])
        print("-> ", pos[-1])
        input()
    if len(pos)%100 == 0:
        print('  . did step # %6d' % len(pos))

pos = np.array(pos)
# final x*y
print('*A:* final position:', pos[-1])
print('*A:* final product:', np.prod(pos[-1,:2]))



#quit()
