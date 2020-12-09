with open('input/01.txt') as f:
    data = f.read().splitlines()

data = data[0]

print('A1:', data.count('(')-data.count(')'))

floor = 0
for idx, c in enumerate(data):
    floor += 1 if c=='(' else -1
    if floor ==-1:
        break
print('A2:', idx)
