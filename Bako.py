import random
import string
import sys

class Book:
    def __init__(self):
        self.Series = ''.join([random.choice(string.ascii_uppercase)
                               for _ in range(4)])
        self.Number = str(random.randint(0, 3))

class ComicRack:
    class App:
        def GetLibraryBooks():
            return generate_book_list(3000)

def generate_book_list(x):
    return [Book() for _ in range(x)]

### END OF OVERRIDE ###

def gen_key(cb):
    return cb.Series + '.' + cb.Number

def BakoDuplicate(filter, a, b):
    all_books = ComicRack.App.GetLibraryBooks()
    # all_books = filter

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
        print('My dupes:')
        logging(dupes)
def logging(args):
    for arg in args:
        print(gen_key(arg), ':', arg)


#print(sys.version)
filter = generate_book_list(100)
BakoDuplicate(filter, '', '')
