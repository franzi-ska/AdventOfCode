# import pandas as pd
#
# data = pd.read_csv('03_trajectory.csv', squeeze=True)


def count_trees_on_trajectory(data, x_s, y_s):
    n_step = len(data)//y_s
    x_max = len(data[0])


    x_0, y_0 = 0,0
    x_coords = [(x_0 + i*x_s)%x_max for i in range(n_step)]
    y_coords = [(y_0 + i*y_s) for i in range(n_step)]

    p = []
    for x,y in zip(x_coords, y_coords):
        p.append(data[y][x])

    return p.count('#')


with open('input/03.txt') as f:
    data = f.read().splitlines()

data = [list(line) for line in data]

print('A1:', count_trees_on_trajectory(data, 3, 1))


slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees = [count_trees_on_trajectory(data, *s) for s in slopes]

prod = 1
for t in trees: prod *= t
print('A2:', prod)
