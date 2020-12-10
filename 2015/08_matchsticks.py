with open('input/08.txt') as f:
    data = f.read().splitlines()

print('A1:', sum([len(line) - len(eval(line)) for line in data]))
print('A2:', sum([2+ line.count('"') + line.count('\\') for line in data]))
