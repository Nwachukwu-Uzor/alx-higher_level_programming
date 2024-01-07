#!/usr/bin/env python3

def no_c(my_string):
      copy = my_string
      return copy.translate({ord('c'): None}).translate({ord('C'): None})
