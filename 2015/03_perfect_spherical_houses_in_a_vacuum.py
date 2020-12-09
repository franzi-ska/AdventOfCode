
def count_houses(instructions, n_santas):
    x = [0]*n_santas
    y = x.copy()
    visited_houses = [(0,0)]
    for i, c in enumerate(instructions):
        idx=i%n_santas
        if c in '<>':
            x[idx] += (1 if c=='>' else -1)
        else:
            y[idx] += (1 if c=='^' else -1)
        visited_houses.append((x[idx],y[idx]))
    return len(set(visited_houses))

with open('input/03.txt') as f:
    data = f.read().splitlines()

print('A1:', count_houses(data[0], 1))
print('A2:', count_houses(data[0], 2))
