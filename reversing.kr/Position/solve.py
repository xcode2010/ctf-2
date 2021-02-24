from itertools import product
serial = ['76876', '77776']

def name2serial(name, offset = [5, 1]):
    # (int((j & 2) != 0) + offset)
    _input = [ord(i) for i in name]
    _input_0 = [int(i) for i in bin(_input[0])[4:]]
    _input_1 = [int(i) for i in bin(_input[1])[4:]]
    result = str((_input_0[4] + offset[0]) + (_input_1[2] + offset[1]))
    result += str((_input_0[1] + offset[0]) + (_input_1[1] + offset[1]))
    result += str((_input_0[3] + offset[0]) + (_input_1[0] + offset[1]))
    result += str((_input_0[2] + offset[0]) + (_input_1[4] + offset[1]))
    result += str((_input_0[0] + offset[0]) + (_input_1[3] + offset[1]))
    return result

def serial2code(name, pos, serial, offset = 6):
    _name = [int(i) for i in bin(ord(name))[4:]]
    _serial = [int(i) for i in serial]
    if pos == 0:
        _serial[0] -= (_name[4] + offset)
        _serial[1] -= (_name[1] + offset)
        _serial[2] -= (_name[3] + offset)
        _serial[3] -= (_name[2] + offset)
        _serial[4] -= (_name[0] + offset)
    else:
        _serial[0] -= (_name[2] + offset)
        _serial[1] -= (_name[1] + offset)
        _serial[2] -= (_name[0] + offset)
        _serial[3] -= (_name[4] + offset)
        _serial[4] -= (_name[3] + offset)
    return str(_serial[4]) + str(_serial[1]) + str(_serial[3]) + str(_serial[2]) + str(_serial[0])

def name2code(name):
    return bin(ord(name))[4:]

def code2name(code):
    return chr(int('11' + code, 2))

ans_1 = code2name(serial2code('p', 1, serial[1])) + 'p'

pos_1 = []
i = 0x61
while i <= 0x7a:
    tmp = bin(i)
    if '0b1110' in tmp and tmp[-2] == '0':
        pos_1.append(i)
    i += 1

pos_0 = []
i = 0x61
while i <= 0x7a:
    tmp = bin(i)
    if '0b1100' in tmp and tmp[-2] == '1':
        pos_0.append(i)
    i += 1

for i, j in product(pos_0, pos_1):
    tmp = name2serial(chr(i) + chr(j))
    if tmp == serial[0]:
        print (chr(i) + chr(j) + ans_1)