class Library:
    def __init__(self):
        self.book = []

    def add_book(self, title):
        self.book.append(title)

    def list_books(self):
        for book in self.book:
            print(book)

library = Library()
library.add_book("Dune")
library.add_book("Clean Code")
library.add_book("The Pragmatic Programmer")

library.list_books()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

account = BankAccount("Alex")
account.deposit(100)
account.withdraw(30)
account.withdraw(1000)