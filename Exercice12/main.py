class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, title, author, year):
        self.books.append(
            Book(title, author, year)
        )
    
    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Le livre '{book_title}' a été supprimé.")
                return
            
        print(f"Le livre '{book_title}' n'a pas été trouvé.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                print(f"Le livre '{book_title}' a été emprunté.")
                return

        print(f"Le livre '{book_title}' n'a pas été trouvé dans la liste des livres disponibles.")

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                print(f"Le livre '{book_title}' a été rendu.")
                return

        print(f"Le livre '{book_title}' n'a pas été trouvé dans la liste des livres empruntés.")

    def available_books(self):
        print("\nListe des livres dans la bibliothèque")
        for book in self.books:
            print(f"{book.title} - {book.author} ({book.year})")

    def borrowed_books(self):
        print("\nListe des livres empruntés")
        for book in self.borrow_books:
            print(f"{book.title} - {book.author} ({book.year})")

library = Library()

library.add_book("1984", "George Orwell", 1949)
library.add_book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
library.add_book("Les Misérables", "Victor Hugo", 1862)
library.add_book("L'Étranger", "Albert Camus", 1942)
library.borrow_book("Le Petit Prince")
library.borrow_book("Les Misérables")
library.return_book("Le Petit Prince")
library.remove_book("L'Étranger")
library.available_books()
library.borrowed_books()

