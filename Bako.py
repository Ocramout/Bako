import random
import string


class Book:
    def __init__(self):
        self.Series = ''.join([random.choice(string.ascii_uppercase) for _ in range(3)])
        self.Number = str(random.randint(0, 5))

    def get_key(self):
        return self.Series + '.' + self.Number

class ComicRack:
    class App:
        def GetLibraryBooks():
            return generate_book_list(1000)

def generate_book_list(x):
    return [Book() for _ in range(x)]

def BakoDuplicate(array):
    books = tuple(array) + tuple(ComicRack.App.GetLibraryBooks())
    keys_list = [b.get_key() for b in books]
    keys_tup = tuple(keys_list)
    
    keys_list.sort()
    dupes = []
    curent = keys_list[0]
    for _next in keys_list[1:]:
        if curent == _next:
            dupes.append(curent)
        curent = _next
    print("My keys:")
    print(keys_list)
    print()
    print("My dupes:")
    print(dupes)

    return 1

BakoDuplicate(generate_book_list(100))
