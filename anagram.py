#!/usr/bin/python

import sys
import sqlite3

input_set = sys.argv[1:]

conn = sqlite3.connect("wordlist.db")
c = conn.cursor()

def get_comb_count(n):
    count = 0
    last = 1
    for i in range(0, n):
        last *= n-i
        count += last
    return count

def get_dict_len():
    c.execute("SELECT COUNT(*) AS count FROM words")
    return c.fetchone()[0]

def check_word(word):
#    print word
    c.execute("SELECT * FROM words WHERE word = ?", (word,))
    if c.fetchone() != None:
        print word

def check_combinations(prefix, char_set):
#    print "gc", prefix, char_set
    for char in char_set:
        subset = char_set[:]
        subset.remove(char)
        subprefix = prefix + char
        check_word(subprefix)
#        print char_set, subprefix, subset
        if len(subset) > 0:
            check_combinations(subprefix, subset)

comb_count = get_comb_count(len(input_set))
dict_len = get_dict_len()
print comb_count, dict_len

if comb_count < dict_len:
    check_combinations("",input_set)

