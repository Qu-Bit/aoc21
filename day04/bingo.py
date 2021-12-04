
"""AoC 2021: day04/
    + puzzle1
    + puzzle2
"""

import numpy as np

# %% input data

in_Fp = 'test_input.txt'
in_Fp = 'input.txt'

def input_reader(file):
    with open(file, 'r') as fh:
        block = []
        while line := fh.readline():
            line = line.strip()
            #print('got line:', line)
            if len(line) == 0:
                #print('len 0')
                yield block
                block = []
            else:
                block.append(line)
                

boards = [b for b in input_reader(in_Fp)]

# draws input line
draws = tuple(map(int, boards.pop(0)[0].split(',')))
print(draws)

print('-'*5)
#for b in blocks:
#    for l in b:
#        print(l.split())
#    print('-')

boards = np.array([[l.split() for l in b] for b in boards]).astype(int)
#print(blocks)

# %% puzzle 1
print('---\npuzzle 1:')

hits = np.zeros_like(boards, dtype=bool)

for d_cnt, draw in enumerate(draws):
    print('* draw (#%d):' % d_cnt, draw)
    this_hit = boards == draw
    hits |= this_hit
    # just printing
    #for b,h in zip(blocks, hits):
    #    print(b[h])
    # checking
    # get matrix shapes
    shapes = list(map(np.shape, hits))
    # hit column sums
    h_col_sums = hits.sum(axis=1)
    h_row_sums = hits.sum(axis=2)
    # column hits, row hits
    check_res = [(h_col_sums[i] == shp[0], 
                  h_row_sums[i] == shp[1]) 
                    for i, shp in enumerate(shapes)]
    check_res = np.array(check_res)
    #print(check_res)
    # win stats per board
    win_bd = check_res.any(axis=-1).any(-1)
    if win_bd.any():
        win_bd = win_bd.argmax()
        score = boards[win_bd][~ hits[win_bd]].sum() * draw
    else:
        win_bd = 'NONE'
        score = 0
    print('winboard:', win_bd, 'score:', score)
    if score > 0:
        break;
    #input()


# %% puzzle 2
print('---\npuzzle 2:')

hits = np.zeros_like(boards, dtype=bool)

for d_cnt, draw in enumerate(draws):
    print('* draw (#%d):' % d_cnt, draw)
    this_hit = boards == draw
    hits |= this_hit
    # checking
    # get matrix shapes
    shapes = list(map(np.shape, hits))
    # hit column sums
    h_col_sums = hits.sum(axis=1)
    h_row_sums = hits.sum(axis=2)
    # column hits, row hits
    check_res = [(h_col_sums[i] == shp[0], 
                  h_row_sums[i] == shp[1]) 
                    for i, shp in enumerate(shapes)]
    check_res = np.array(check_res)
    #print(check_res)
    # win stats per board
    win_bd = check_res.any(axis=-1).any(-1)
    score = 0 
    #print(win_bd)
    # only 1 missing?
    if win_bd.sum() == (len(boards) - 1):
        lwin_bd = win_bd.argmin()
        print(' set last win bd:', lwin_bd)
    elif win_bd.all():
        print('score')
        score = boards[lwin_bd][~ hits[lwin_bd]].sum() * draw
    else:
        lwin_bd = 'NONE'
    print('last winboard:', lwin_bd, 'score:', score)
    if score > 0:
        break;
    #input()


