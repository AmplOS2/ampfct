#!/usr/bin/env python3
from json import dumps
from sys import argv
from bitarray import bitarray
from PIL import Image

name = argv[1]
glyph_width = int(argv[2])
glyph_height = int(argv[3])
columns = int(argv[4])
rows = int(argv[5])
offset_x = int(argv[6])
offset_y = int(argv[7])
white = 1 if argv[8] == 'b' else 0
black = 1 if white == 0 else 0
padding = (8 - glyph_width % 8) % 8
bpg = int((glyph_width + 7) / 8) * glyph_height

bits = bitarray(endian='big')

i = Image.open(open('%s.png' % name, 'rb'))
for r in range(rows):
    for c in range(columns):
        for y in range(r*glyph_height+offset_y, (r+1)*glyph_height+offset_y):
            for x in range(c*glyph_width+offset_x, (c+1)*glyph_width+offset_x):
                bits.append(white if i.getpixel((x, y)) != 0 else black)
            for _ in range(padding):
                bits.append(0)

open('%s.h' % name, 'w').write('const static unsigned char %s[]=' % name + dumps(list(bits.tobytes()))
                               .replace('[', '{').replace(']', '}').replace(' ', '') + ';' +
                               'const static unsigned %s_glyph_width=%d;' % (name, glyph_width) +
                               'const static unsigned %s_glyph_height=%d;' % (name, glyph_height) +
                               'const static unsigned %s_glyphs=%d;\n' % (name, rows*columns) +
                               'const static unsigned %s_bytes_per_glyph=%d;\n' % (name, bpg))
