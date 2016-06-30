# -*- coding: uft-8 -*-

import random
import string
import sys
import time

class Book:
    def __init__(self):
        self.Series = ''.join([random.choice(string.ascii_uppercase) for _ in range(4)])
        self.Number = str(random.randint(0, 3))

def GetLibraryBooks():
    return generate_book_list(3000)

def generate_book_list(x):
    return [Book() for _ in range(x)]

def gen_key(cb):
    return cb.Series + '.' + cb.Number

def BakoDuplicate(filter, a, b):
    all_books = GetLibraryBooks()

    books = dict()    # { key:[Book(), Book()] }
    for book in all_books:
        key = unicode(gen_key(book), encoding='UTF-8', errors='replace')
        if key not in books.keys():
            books[key] = [book]
        else:
            books[key].append(book)

    dupes = []
    for key, book in books.items():
        if len(book) > 1:
            dupes += [b for b in book]
    
    if len(dupes) == 0:
        print('No dupes !')
    else:
        print('%d dupes found !' % (len(dupes)))

        # file reset
        f = open('log.txt', 'w')
        f.close()

        my_logger("Dupes found on " + time.strftime("%c"))
        for book in set(dupes):
            key = unicode(gen_key(book), encoding='UTF-8', errors='replace')
            my_logger(key)
        my_logger("")

    return dupes

def my_logger(string):
    with open('log.txt', mode='a', encoding='UTF-8', errors='replace') as f:
        if type(string).__name__ != 'str':
            string = string.encode(encoding='UTF-8', errors='ignore')
        f.write(string + '\n')



filter = generate_book_list(100)
BakoDuplicate(filter, '', '')
