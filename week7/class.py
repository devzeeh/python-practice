# A class lets you bundle the data and the functions that work on it together, into one reusable "blueprint
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"{self.title}, by {self.author}")

book1 = Book("Dune", "Frank Herbert")
book2 = Book("Clean Code", "Robert Martin")

book1.describe()
book2.describe()