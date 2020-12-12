import numpy as np

def look_around(position, row_max, col_max, all_chairs, direct_only=False):
    if not position in all_chairs:
        return []

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                   (0, 1), (1, -1), (1, 0), (1, 1)]
    visible = []
    for (dr, dc) in directions:
        r = position[0] + dr
        c = position[1] + dc
        found = False
        while not found and ((r in range(row_max)) and (c in range(col_max))):
            if (r, c) in all_chairs:
                visible.append((r, c))
                found = True
            else:
                r += dr
                c += dc
            if direct_only:
                found = True
    return visible


def update(info_dict, npa, n_max):
    npa_new = npa.copy()
    for pos, neigbor in info_dict.items():
        n = sum(npa[p] for p in neigbor)
        npa_new[pos] = n < n_max if npa[pos] else n == 0

    return npa_new, (npa_new == npa).all()


def day11(n_max, direct_only):

    with open('input/11.txt') as f:
        data = f.read().splitlines()

    seats = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == 'L':
                seats[(row, col)] = []
    n_row, n_col = len(data), len(data[0])
    for p in seats:
        seats[p] = look_around(p, len(data), len(data[0]), seats, direct_only)

    status_matrix = np.zeros((n_row, n_col)) == 1
    static = False
    while not static:
        status_matrix, static = update(seats, status_matrix, n_max)
    return status_matrix.sum()

print('A1:', day11(4, True))
print('A2:', day11(5, False))
