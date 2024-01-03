#!/usr/bin/python3
for i in range(100):
    if (i < 99):
        print(f"{'0' if i < 10 else ''}{i}, ", end="")
    else:
        print(f"{i}")
