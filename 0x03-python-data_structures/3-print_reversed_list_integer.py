#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    cp = my_list.copy()
    cp.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(cp[i]))
