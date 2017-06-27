#!/usr/bin/python

import sys

input_set = sys.argv[1:]

def get_combinations(prefix, char_set):
#    print "gc", prefix, char_set
    if len(char_set) == 1:
        print prefix + char_set[0]
    for char in char_set:
        subset = char_set[:]
        subset.remove(char)
        subprefix = prefix + char
#        print char_set, subprefix, subset
        get_combinations(subprefix, subset)

print input_set
print get_combinations("",input_set)


