# Inheritance lets one class "inherit" attributes and methods from another
# so you can build a more specific class on top of a general one, without rewriting everything from scratch

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"'{self.title}' by {self.author}")


class AudioBook(Book):
    def __init__(self, title, author, duration_minutes):
        super().__init__(title, author)
        self.duration_minutes = duration_minutes

    def describe(self):   # overrides Book's describe method
            print(f"'{self.title}' by {self.author} (AudioBook, {self.duration_minutes} mins)")

book = Book("Clean Code", "Robert Martin")
audiobook = AudioBook("Dune", "Frank Herbert", 120)

book.describe()
audiobook.describe()