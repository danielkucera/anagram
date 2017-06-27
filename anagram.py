#!/usr/bin/python

import sys

input_set = sys.argv[1:]

def get_combinations(prefix, char_set):
#    print "gc", prefix, char_set
    for char in char_set:
        subset = char_set[:]
        subset.remove(char)
        subprefix = prefix + char
        print subprefix
#        print char_set, subprefix, subset
        if len(subset) > 0:
            get_combinations(subprefix, subset)

print input_set
print get_combinations("",input_set)


