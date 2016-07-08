# -*- coding: UTF-8 -*-

import random
import string
import sys
import time
from datetime import datetime

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

def get_random_unicode(length):

    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length))


    ####  END OF OVERRIDE  ####


def BakoDuplicate(filter, a, b):
    all_books = GetLibraryBooks()

    books = dict()
    dupes = set()
    for book in all_books:
        #key = gen_key(book)
        key = get_random_unicode(2)
        if key == None:
            continue
        elif key not in books.keys():
            books[key] = [book]
        else:
            books[key].append(book)
            dupes.add(key)

    dupes_obj = []
    number_of_dupes = len(dupes)
    template = "{{}} dupes found on {}".format(datetime.now())

    if number_of_dupes == 0:
        print(template.format("No"))
        return dupes_obj

    for dupe in dupes:
        dupes_obj += books[dupe]

    my_logger(template.format(number_of_dupes), dupes)


    return dupes_obj


def my_logger(template, args):
    f = open("log.txt", mode="a")

    try:
        f.write(template + '\n')
        print(template)

        for arg in args:
            string = arg.encode(encoding='utf8', errors='ignore')
            f.write(string + '\n')
            print(string)
        f.write('\n')
    finally:
        f.close()


filter = generate_book_list(100)
filter = None
BakoDuplicate(filter, '', '')
