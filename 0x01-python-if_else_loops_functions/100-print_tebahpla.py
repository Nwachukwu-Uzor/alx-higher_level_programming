#!/usr/bin/python3

for ch in range(ord('z'), ord('a') - 1, -1):
    if ch % 2 == 0:
        x = 0
    else:
        x = 32
    print('{}'.format(chr(ch - x)), end='')
