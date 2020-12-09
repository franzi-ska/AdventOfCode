
import pandas as pd
import re

class check_passport():
    @classmethod
    def byr(self, byr):
        return self.in_range(byr, 1920 ,2002)

    @classmethod
    def iyr(self, iyr):
        return self.in_range(iyr, 2010, 2020)

    @classmethod
    def eyr(self, eyr):
        return self.in_range(eyr, 2020, 2030)

    @classmethod
    def hgt(self, hgt):
        unit = hgt[-2:]
        value = hgt[:-2]
        if unit=='cm':
            res = self.in_range(value, 150, 193)
        elif unit=='in':
            res = self.in_range(value, 59, 76)
        else:
            res = False
        return res

    @staticmethod
    def hcl(hcl):
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl)
        if match: return True
        else: return False

    @staticmethod
    def ecl(ecl):
        valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return ecl in valid

    @staticmethod
    def pid(pid):
        return len(pid)==9

    @staticmethod
    def in_range(value, min_value, max_value):
        value = int(value)
        return value>=min_value and value<=max_value

with open('input/04.txt') as f:
    data = f.read().splitlines()

p=0
person = {0:{}}
for idx, line in enumerate(data):
    if line =='':
        p+=1
        person[p]={}
    else:
        for pair in line.split(' '):
            [key, item] = pair.split(':')
            person[p][key]=item

persons = pd.DataFrame().from_dict(person,orient='index')

n_total = persons.shape[0]

valid_persons = persons.dropna(axis=0,
                    subset=['hgt', 'iyr', 'hcl', 'ecl', 'byr', 'eyr', 'pid'])

n_valid = valid_persons.shape[0]
print('A1:', n_valid)



all_valid = valid_persons.copy()
for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
    all_valid[key] = valid_persons[key].apply(getattr(check_passport, key))
all_valid['cid'] = True


print('A2:', all_valid.all(axis=1).value_counts()[1])
