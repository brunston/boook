
from boook import *

mylib = DB("mylib")
print(mylib)
print("before write", mylib.db)
mylib.write()
mylib.read()
print("after read", mylib.db)

newbook = book_make("my life", "me", "i like this book because it is my life.") # no links
mylib.insert(newbook)
print("after insert", mylib.db)
mylib.write()
