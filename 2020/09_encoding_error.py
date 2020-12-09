import numpy as np

with open('input/09.txt') as f:
    data = f.read().splitlines()

data = [int(i) for i in data]

n_preamble=25

for idx in range(n_preamble, len(data)):
    # print(idx)

    preamble = data[idx-n_preamble:idx]
    sums = np.add(*np.meshgrid(preamble, preamble, sparse=True))
    np.fill_diagonal(sums, 0)
    if not data[idx] in sums:
        print('A1:', data[idx])
        sum_error = data[idx]
        break

data = np.array(data)
min_set_length = 2
for idx_start in range(len(data)- min_set_length):
    for idx_stop in range(idx_start+min_set_length, len(data)):
        subset = data[idx_start: idx_stop]
        subset_sum = subset.sum()

        if sum_error == subset_sum:
            print('A2:', subset.min()+subset.max())
        elif subset_sum > sum_error:
            break #go to next idx_start to speed up
