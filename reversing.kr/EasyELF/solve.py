_input = [0 for _ in range(6)]

_input[1] = 0x31
_input[0] = 0x34 ^ 0x78
_input[2] = 0x32 ^ 0x7c
_input[3] = 0x88 ^ 0xdd
_input[4] = 0x58
_input[5] = 0x0

print (''.join(chr(i) for i in _input))