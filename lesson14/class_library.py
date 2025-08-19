class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    books_list = []

    def __init__(self, book):
        self.book = book

    def add_books(self):
        Library.books_list.append(self.book)

    def get_books(self):
        return Library.books_list


book1 = Book("Me", "Jane Ostin")
book2 = Book("You", "Mike Jowl")

Library(book1).add_books()
Library(book2).add_books()

library = Library(None)
for book in library.get_books():
    print(f"Title: {book.title}, Author: {book.author}")
