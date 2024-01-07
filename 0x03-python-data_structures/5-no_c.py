#!/usr/bin/env python3

def no_c(my_string):
    copy = list(my_string)
    count_c = copy.count('c')
    count_C = copy.count('C')
    if count_c > 0:
        for i in range(count_c):
            pos = copy.index('c')
            copy[pos] = ''
    if count_C > 0:
        for i in range(count_C):
            pos = copy.index('C')
            copy[pos] = ''
    return ''.join(copy)
