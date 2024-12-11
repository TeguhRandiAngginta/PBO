# Superclass
class Book:
    def __init__(self, title):
        self.title = title

    def read(self):
        return f"Reading '{self.title}' from a physical book."

# Subclass yang mewarisi dari Book
class EBook(Book):
    def read(self):
        return f"Reading '{self.title}' from an e-book."

# Pengujian
ebook = EBook("Python Basics")
print(ebook.read())  # Output: Reading 'Python Basics' from an e-book.
