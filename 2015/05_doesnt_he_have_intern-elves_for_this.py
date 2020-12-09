import re
with open('input/05.txt') as f:
    data = f.read().splitlines()

regex = {
            1: re.compile(r'[aeiou]'),
            2: re.compile(r'([a-z])\1'),
            3: re.compile(r'(ab|cd|pq|xy)'),
            4: re.compile(r'([a-z][a-z])[a-z]*\1'),
            5: re.compile(r'([a-z])[a-z]\1'),
        }

nice_count_1 = 0
nice_count_2 = 0
for line in data:
    if len(regex[1].findall(line))>= 3:
        if regex[2].search(line):
            if not regex[3].search(line):
                nice_count_1 += 1
    if regex[4].search(line):
        if regex[5].search(line):
            nice_count_2 += 1
print('A1:', nice_count_1)
print('A2:', nice_count_2)
