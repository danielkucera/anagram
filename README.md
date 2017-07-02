# anagram
This program creates anagrams from provided letters and checks if it exists in word database.

## Setup
* first you need to create file with valid words - one per line, e.g. wordlist.txt:
```
čakaŤ
písaľ
soľ
piť
pix
```
* next add them to database by running:
```
./create_db.py wordlist.txt
```
* valid anagrams are sorted by their values according to letter values in charvalues.txt. Format is obvious from following file:
```
cat charvalues.txt
```
* now you can use anagram.py

## Usage example
```
./anagram.py p o s o a k a ť č i x
possilbe combinations: 108505111 dictionary size: 9
('PIŤ', 9)
('PIX', 12)
('ČAKAŤ', 14)
```
