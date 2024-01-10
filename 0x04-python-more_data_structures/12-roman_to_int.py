#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    options = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [options[x] for x in roman_string] + [0]
    result = 0

    for n in range(len(values) - 1):
        if values[i] >= values[i+1]:
            result += values[i]
        else:
            result -= values[i]

    return result
