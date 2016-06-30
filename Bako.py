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
    series = cb.Series
    number = cb.Number

    series_type = type(series).__name__
    number_type = type(number).__name__

    # decode la string seulement si elle est encodee
    # le type 'str' est un format d
    # decode() retourne une string de type unicode
    if series_type != 'str':
        series = series.decode(encoding=series_type)
    if number_type != 'str':
        number = number.decode(encoding=number_type)
    
    return series + '.' + number

def BakoDuplicate(filter, a, b):
    all_books = GetLibraryBooks()

    books = dict()    # { key:[Book(), Book()] }
    for book in all_books:
        key = gen_key(book)
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
            my_logger(gen_key(book))
        my_logger("")

    return dupes

def my_logger(string):
    with open('log.txt', 'a') as f:
        if type(string).__name__ != 'str':
            string = string.encode(encoding='UTF-8', errors='ignore')
        f.write(string + '\n')



filter = generate_book_list(100)
BakoDuplicate(filter, '', '')
