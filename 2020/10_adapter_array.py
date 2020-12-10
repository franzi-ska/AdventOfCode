with open('input/10.txt') as f:
    data = [int(i) for i in f.read().splitlines()]

data.append(0) # source
data.append(max(data)+3) # my device
data.sort()
diff = [data[i+1]- data[i] for i in range(0, len(data)-1)]
# data.pop(0)
A1 = diff.count(1) * (diff.count(3))

print('A1:', A1)


def adapters_it_can_reach(p):
    return [p+j for j in [1,2,3] if p+j in data]

options = {i: 0 for i in data}
options[0]=1
for key, item in options.items():
    for next_adapter in adapters_it_can_reach(key):
        options[next_adapter]+= item

print('A2:', options[max(data)])
