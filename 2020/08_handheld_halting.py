def infinit_loop(input):
    idx = 0
    old_idx = []
    acc = 0
    while not idx in old_idx:
        old_idx.append(idx)
        inst, val = input[idx]
        if 'acc'==inst:
            print
            acc += val
            idx += 1
        elif 'jmp'==inst:
            idx += val
        elif 'nop'==inst:
            idx += 1
        else:
            print('hä')

        if idx == len(input):
            return True, acc
    return False, acc

with open('input/08.txt') as f:
    data = f.read().splitlines()
data = [i.split(' ') for i in data]
data = [[i, int(j)] for i,j in data]


print('A1:', infinit_loop(data)[1])

for j, (instruction, value) in enumerate(data):
    if instruction=='acc':
        pass
    else:
        old = instruction
        new = ('nop' if instruction == 'jmp' else 'jmp')
        data[j][0]=new
        works, acc = infinit_loop(data)
        if works:
            print('A2:', acc)
            break
        else:
            data[j][0]=old
