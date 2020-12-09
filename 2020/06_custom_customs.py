with open('input/06.txt') as f:
    data = f.read().splitlines()
data.append('') # add to mark next group


this_group = []
count = 0
for line in data:
    # print(line)
    if line=='':
        count += len(set(this_group))
        # print(len(set(this_group)))
        this_group = []

    else:
        this_group += [i for i in line]

print('A1:', count)



person_count = 0
this_group = ''
count = 0
for line in data:
    if line == '':
        # print(this_group)

        for c in set([i for i in this_group]):
            if person_count == this_group.count(c):
                count += 1

        # prepare for next group
        person_count = 0
        this_group = ''

    else:
        this_group += line
        person_count +=1

print('A2:', count)
