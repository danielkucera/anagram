#!/usr/bin/python3

import sys
import sqlite3

input_set = [x.upper() for x in sys.argv[1:]]

conn = sqlite3.connect("wordlist.db")
c = conn.cursor()

words = {}

def load_char_values(filename):
    ch_vals = {}
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        ch = line[0].upper()
        val = line[1:]
        ch_vals[ch] = int(val)
    return ch_vals

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

def eval_word(word):
    val = 0
    for ch in word:
        val += char_values[ch]
    return val

def add_word(word):
    words[word] = eval_word(word)

def check_word(word):
    c.execute("SELECT * FROM words WHERE word = ?", (word,))
    if c.fetchone() != None:
        add_word(word)

def check_combinations(prefix, char_set):
    for char in char_set:
        subset = char_set[:]
        subset.remove(char)
        subprefix = prefix + char
        check_word(subprefix)
        if len(subset) > 0:
            check_combinations(subprefix, subset)

def match_word(chset, word):
    lword = list(word)
    for ch in lword:
        if ch in chset:
            chset.remove(ch)
        else:
            return False
    return True

def check_dict(input_set):
    for row in c.execute("SELECT * FROM words WHERE length(word) < ?", (len(input_set),)): #where len < dict_len
        word = row[0]
        if match_word(input_set[:], word):
            add_word(word)

char_values = load_char_values("charvalues.txt")
comb_count = get_comb_count(len(input_set))
dict_len = get_dict_len()
print("possilbe combinations:", comb_count, "dictionary size:", dict_len)

if comb_count < dict_len:
    check_combinations("",input_set)
else:
    check_dict(input_set)

sorted_words = sorted(words.items(), key=lambda word: word[1])

for word in sorted_words:
    print(word)

