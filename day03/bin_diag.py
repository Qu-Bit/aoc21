
"""AoC 2021: day03/
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
    data = list([[int(b) for b in l] for l in map(str.strip, rdata)])
    print('data entries:', len(rdata))

data = np.array(data, dtype=bool)

def bool_arr_to_dec(ba):
    return int(''.join(map(str, map(int, ba))), 2)

# %% puzzle 1
print('---\npuzzle 1:')

# get gamma
gam_v = [v[np.argmax(c)] for v,c in
         (np.unique(c, return_counts=True) for c in data.T)]
gam_b10 = bool_arr_to_dec(gam_v)
print('* got gamma:', gam_b10)


# get epsilon
eps_v = [v[np.argmin(c)] for v,c in
         (np.unique(c, return_counts=True) for c in data.T)]
eps_b10 = bool_arr_to_dec(eps_v)
print('* got epsilon:', eps_b10)

print('* power cons.: ', gam_b10*eps_b10)

# %% puzzle 2
print('---\npuzzle 2:')

def filter_by_msb_val(data, filt_mode, i_msb=0):
    assert len(data.shape) == 2, ('dimension of data to filter != 2')
    # TODO: N column addressing check
    uniqC = [np.unique(c, return_counts=True) for c in data.T]
    if filt_mode == 'min':
        func_vcol = [v[np.argmin(c)]  
                     if ((len(c)>1) and (c[0]!=c[1])) else False
                        for v,c in uniqC]
    elif filt_mode == 'max':
        func_vcol = [v[np.argmax(c)]  
                     if ((len(c)>1) and (c[0]!=c[1])) else True 
                         for v,c in uniqC]
    else:
        raise ValueError
    # filter on column of msb
    fdata = data[data[:, i_msb] == func_vcol[i_msb]]
    if len(fdata) != 1:
        fdata = filter_by_msb_val(fdata, filt_mode, i_msb+1)
    if len(fdata) == 1:
        return(fdata[:1])
    raise Exception

oxGr = filter_by_msb_val(data, 'max')[0]
oxGr_b10 = bool_arr_to_dec(oxGr)
print('* Oxygen gen.rate: ', oxGr_b10)

co2Sr = filter_by_msb_val(data, 'min')[0]
co2Sr_b10 = bool_arr_to_dec(co2Sr)
print('* Oxygen gen.rate: ', co2Sr_b10)

print('* life support rating: ', oxGr_b10*co2Sr_b10)

