def find_seat(s, lower, upper, min_seat=0, max_seat=127):
    for c in s:
        seat_range = max_seat-min_seat
        if c==lower:
            max_seat-= seat_range//2+1
        if c== upper:
            min_seat+= seat_range//2+1

    if min_seat==max_seat:
        return min_seat
    else:
        raise ValueError('Could not find the right seat')

with open('input/05.txt') as f:
    data = f.read().splitlines()

id_list = []
for line in data:
    row = find_seat(line[:-3], 'F', 'B')
    column = find_seat(line[-3:], 'L', 'R', max_seat=7)
    id_list.append(row*8+column)
print('A1:', max(id_list))

id_list = sorted(id_list)
for i in range(min(id_list), max(id_list)):
    if i in id_list:
        pass
    else:
        print('A2:', i)
        break
