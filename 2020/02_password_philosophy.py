import re
def sep_string(text):
    [n_min, n_max, letter, string] = re.split('-| |: | ', text)
    n_min = int(n_min)
    n_max = int(n_max)
    return n_min, n_max, letter, string

with open('input/02.txt') as f:
    data = f.read().splitlines()

count_1 = 0
count_2 = 0
for line in data:
    n1, n2, letter, text = sep_string(line)

    n_letter = text.count(letter)
    if n1 <= n_letter <= n2:
        count_1 += 1

    if (text[n1-1]==letter) ^ (text[n2-1]==letter):
        count_2 += 1
print('A1', count_1)
print('A2', count_2)
