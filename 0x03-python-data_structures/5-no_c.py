#!/usr/bin/env python3

def no_c(my_string):
    copy = my_string
    count_c = copy.count('c')
    count_C = copy.count('C')
    if count_c > 0:
        for i in range(count_c):
            copy.remove('c')
    if count_C > 0:
        for i in range(count_C):
            copy.remove('C')
    return copy
