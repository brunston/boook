## boook ##
# (c) brunston 2016 #
# GNU GPL #

import json

class DB:
    
    def __init__(self, name):
        self.file = name + ".bdb"
        self.db = {"count": 0, "books": {}}
        return None
    
    def read(self):
        with open(self.file) as f:
            self.db = json.load(f)
        return None

    def write(self):
        with open(self.file, 'w') as f:
            json.dump(self.db, f)
        return None

    def backup(self):
        """
        backs up db version that's in memory
        """
        with open(self.file + ".bak", 'w') as f:
            json.dump(self.db, f)
        return None

    def insert(self, book):
        self.db["count"] += 1
        if book_title(book) not in self.db["books"]:
            self.db["books"][book_title(book)] = book
        else:
            raise Exception("book already in database")
        return None

    def remove(self, title):
        self.db["count"] -= 1
        del self.db["books"][title]
        return None

# BOOK DATA ABSTRACTIONS (represented as a python dictionary to ease json conversion)

def book_make(title, author, details, links=[]):
    """
    creates a new book. TITLE (a string) and AUTHOR (a string) are self-explanatory.
    DETAILS (a string) includes any pertinent information:
        date of publication
        date of purchase
        a review / summary
        who loves the book
        who hates the book
        whatever
    LINKS (a list of Book objects) includes any Book in the DB
    """
    return {"title": title, "author": author, "details": details, "links": links}

def book_title(book):
    return book["title"]

def book_author(book):
    return book["author"]

def book_details(book):
    return book["details"]

def book_links(book):
    return book["links"]

def book_modify(book, attribute, newval):
    if attribute in book:
        book[attribute] = newval
    else:
        raise Exception("invalid attribute")
