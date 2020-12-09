import hashlib

input = 'iwrupvqb'

result = ''
number = 1
while not result=='00000':
    number += 1
    str2hash = input+str(number)
    result = hashlib.md5(str2hash.encode()).hexdigest()[0:5]


print('A1', number)


while not result == '000000':
    number += 1
    str2hash = input+str(number)
    result = hashlib.md5(str2hash.encode()).hexdigest()[0:6]

print('A2', number)
