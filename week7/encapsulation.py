class Library:
    def __init__(self):
        self._book = []

    def add_book(self, title):
        self._book.append(title)

    def list_books(self):
        for book in self._book:
            print(book)

    def get_book_count(self):
        return len(self._book)

library = Library()
library.add_book("Dune")
library.add_book("Clean Code")
library.add_book("The Pragmatic Programmer")

print(library.get_book_count())
library.list_books()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance   # single underscore = "internal use, please don't touch directly"

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")


account = BankAccount("Alex", 100)
print(account.get_balance())     # 100 — accessed through a method, not directly
account.deposit(50)