#!/usr/bin/python

import sqlite3

f = open("words.txt", "r")

conn = sqlite3.connect("wordlist.db")
c = conn.cursor()

c.execute("CREATE TABLE words (word text)")
c.execute("CREATE INDEX words_index ON words(word)")

for line in f:
    print "line",line[:-1]
    c.execute("INSERT INTO words VALUES(?)", (line.rstrip(),))

conn.commit()
conn.close()

