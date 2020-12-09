from ctypes import c_uint16

with open('input/07.txt') as f:
    data = f.read().splitlines()
instructions = {wire: operation for operation, wire in [line.split(' -> ') for line in data]}



def get_value(wire):
    if wire.isnumeric():
        value = int(wire)
    elif wire in known:
        value = known[wire]
    else:
        op = instructions[wire].split()

        if 'RSHIFT' in op:
            value = get_value(op[0]) >> int(op[2])
        elif 'LSHIFT' in op:
            value = get_value(op[0]) << int(op[2])
        elif 'OR' in op:
            value = get_value(op[0]) | get_value(op[2])
        elif 'AND' in op:
            value = get_value(op[0]) & get_value(op[2])
        elif 'NOT' in op:
            value = c_uint16(~ get_value(op[1])).value
        else: #SET
            value = get_value(op[0])

        known[wire] = value
    return value

known ={}
print('A1:', get_value('a'))

known = {'b': 46065}
print('A2:', get_value('a'))
