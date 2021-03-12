# patch sub_401000
sub_401000_end = 0x4135c9
sub_401000_start = 0x401009
patch_len = sub_401000_end - sub_401000_start

patches = bytes([0x90]) * patch_len
ida_bytes.patch_bytes(sub_401000_start, patches)

# patch main
target = '905058535b6061'.encode()
main_start = 0x004135E0
main_end = 0x0044A989

for i in range(main_start, main_end):
    if (ida_bytes.get_bytes(i, 7)) == target:
        ida_bytes.patch_bytes(i, bytes([0x90]) * 7)

# decrypte
with open('file', 'rb') as f:
    raw = f.read()

pt = b''
key = b'letsplaychess'

for i in range(len(raw)):
    pt += bytes([(raw[i] ^ 0xff) ^ key[i % len(key)]])
    
with open('file_ord', 'wb') as f:
    f.write(pt)