
"""AoC 2021: day**/
    - puzzle1
    - puzzle2
"""

# %% imports
import numpy as np

do_debug = False #or True

# %% input data

in_Fp = 'test_input.txt'
if not do_debug:
    in_Fp = 'input.txt'

def input_reader(file):
    # iterating over blocks of lines not separated by white-space line
    with open(file, 'r') as fh:
        block = []
        while line := fh.readline():
            line = line.strip()
            #print('got line:', line)
            # splitting on empty line
            if len(line) == 0:
                #print('len 0')
                yield block
                block = []
            else:
                block.append(line)
                

blocks = [b for b in input_reader(in_Fp)]

# separate first block
draws = tuple(map(int, blocks.pop(0)[0].split(',')))
print(draws)

# %% puzzle 1
print('---\npuzzle 1:')

# %% puzzle 2
print('---\npuzzle 2:')

