#!/usr/bin/python3

import sqlite3
import sys

f = open(sys.argv[1], "r", encoding="utf-8")

conn = sqlite3.connect("wordlist.db")
c = conn.cursor()

try:
    c.execute("CREATE TABLE words (word text)")
    c.execute("CREATE INDEX words_index ON words(word)")
except:
    pass

for line in f:
    word = line.rstrip().upper()
    print("line",word)
    c.execute("INSERT INTO words VALUES(?)", (word,))

conn.commit()
conn.close()

