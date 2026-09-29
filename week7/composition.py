class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        self._books.append(title)

    def list_books(self):
        for book in self._books:
            print(book)

    def checkout_book(self, title, member):
        print(f"{member.name} checked out '{title}'")


library = Library()
library.add_book("Dune")
library.add_book("Clean Code")

alice = Member("Alice")

library.checkout_book("Dune", alice)