#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) <= 0:
        return None
    return ("{:d}".format(len(sentence)), sentence[0])
