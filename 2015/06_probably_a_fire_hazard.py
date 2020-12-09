import re
import numpy as np

with open('input/06.txt') as f:
    data = f.read().splitlines()

regex_xy = re.compile('\d+')
regex_instruction = re.compile(r'([a-z]+\s*[a-z]*)')

grid_size = 1000
grid = np.zeros((grid_size, grid_size), bool)
grid_dimm = np.zeros((grid_size, grid_size))


for line in data:
    [x_min, y_min, x_max, y_max] = [int(i) for i in regex_xy.findall(line)]
    instruction = regex_instruction.match(line).group().strip()

    subset = grid[x_min:x_max+1, y_min:y_max+1]
    subset_2 = grid_dimm[x_min:x_max+1, y_min:y_max+1]
    if instruction=='toggle':
        subset = ~subset
        subset_2 += 2
    if instruction=='turn on':
        subset = True
        subset_2 += 1
    if instruction == 'turn off':
        subset = False
        subset_2 -= 1
        subset_2[subset_2<0] = 0


    grid[x_min:x_max+1, y_min:y_max+1] = subset
    grid_dimm[x_min:x_max+1, y_min:y_max+1] = subset_2

print('A1:', grid.sum())
print('A2:', grid_dimm.sum())
