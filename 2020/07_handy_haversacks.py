with open('input/07.txt') as f:
    data = f.read().splitlines()

bags = {}
n_bags = {}
for idx, line in enumerate(data):
    line = line.replace('.', '')
    line = line.replace('bags', '')
    line = line.replace('bag', '')
    line = line.replace('contain', ',')
    line = line.replace(' no ', ' 0 ')
    line = [i.strip() for i in line.split(',')]

    bags[line[0]] = [i.split(' ', 1)[1] for i in line[1:]]
    n_bags[line[0]] = [int(i.split(' ', 1)[0]) for i in line[1:]]

my_color = 'shiny gold'

def can_it_hold(test_color):
    if not test_color in bags:
        allowed = False
    elif my_color in bags[test_color]:
        allowed = True
    else:
        allowed = any([can_it_hold(c) for c in bags[test_color]])
    return allowed


count = 0
for color in bags:
    count += can_it_hold(color)
print('A1:', count)


def how_many(test_color):
    if (not test_color in bags) or (n_bags[test_color] == [0]):
        n = 0  # no more bags inside this one
    else:
        n_this_level = sum(n_bags[test_color])

        n_next_levels = 0
        for c, n_c in zip(bags[test_color], n_bags[test_color]):
            n_next_levels += n_c * how_many(c)
        n = n_this_level + n_next_levels

    return n


print('A2:', how_many(my_color))
