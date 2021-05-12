#!/usr/bin/env python3
from PIL import Image
from bitarray import bitarray
from json import dumps

bits = bitarray(endian='big')

i = Image.open(open('term_font.png', 'rb'))
for r in range(16):
    for c in range(16):
        for y in range(r*11, (r+1)*11):
            for x in range(c*8, (c+1)*8):
                bits.append(1 if i.getpixel((x, y)) != 0 else 0)

open('term_font.bin', 'wb').write(bits.tobytes())

open('term_font.h', 'w').write('const static char *term_font=' + dumps(list(bits.tobytes()))
                               .replace('[', '{').replace(']', '}').replace(' ', '') + ';')
