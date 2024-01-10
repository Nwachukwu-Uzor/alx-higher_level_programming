#!/usr/bin/python3
def complex_delete(my_dict, value):
    cpy = my_dict.copy()
    for entry, val in cpy.items():
        if value == val:
            my_dict.pop(entry)
    return my_dict

