#!/usr/bin/python

import sys
import sqlite3

input_set = sys.argv[1:]

conn = sqlite3.connect("wordlist.db")
c = conn.cursor()

def check_word(word):
#    print word
    c.execute("SELECT * FROM words WHERE word = ?", (word,))
    if c.fetchone() != None:
        print word

def get_combinations(prefix, char_set):
#    print "gc", prefix, char_set
    for char in char_set:
        subset = char_set[:]
        subset.remove(char)
        subprefix = prefix + char
        check_word(subprefix)
#        print char_set, subprefix, subset
        if len(subset) > 0:
            get_combinations(subprefix, subset)

print input_set
print get_combinations("",input_set)


