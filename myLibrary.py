class Book:
          def __init__(self, title, author, genre, pages):
                    self.title = title
                    self.author = author
                    self.genre = genre
                    self.pages = pages
          
class Author:
          def __init__(self, name):
                    self.name = name
          
class Genre:
          def __init__(self, genre):
                    self.genre = genre
          
class Library:
          def __init__(self, name):
                    self.name = name
                    self.books = []
          
          def add_book(self, book):
                    self.books.append(book)
          
          def remove_book(self, book):
                    self.books.remove(book)
          
          def list_books(self):
                    for book in self.books:
                              print(f'{book.title} by {book.author.name}')
          
          def search_books(self, title):
                    for book in self.books:
                              if book.title == title:
                                        print(f'{book.title} by {book.author.name}')
                                        return
                    print(f'{title} not found')
          
          def search_author(self, author):
                    for book in self.books:
                              if book.author.name == author:
                                        print(f'{book.title} by {book.author.name}')
                    print(f'{author} not found')
          
          def search_genre(self, genre):
                    for book in self.books:
                              if book.genre.genre == genre:
                                        print(f'{book.title} by {book.author.name}')
                    print(f'{genre} not found')
          
          def search_pages(self, pages):
                    for book in self.books:
                              if book.pages == pages:
                                        print(f'{book.title} by {book.author.name}')
                    print(f'{pages} not found')
          
          def search_books(self, title):
                    for book in self.books:
                              if book.title == title:
                                        print(f'{book.title} by {book.author.name}')
                                        return
                    print(f'{title} not found')
          
          def search_author(self, author):
                    for book in self.books:
                              if book.author.name == author:
                                        print(f'{book.title} by {book.author.name}')
                    print(f'{author} not found')
          
          def search_genre(self, genre):
                    for book in self.books:
                              if book.genre.genre == genre:
                                        print(f'{book.title} by {book.author.name}')
                    print(f'{genre} not found')
          
          def search_pages(self, pages):
                    for book in self.books:
                              if book.pages == pages:
                                        print(f'{book.title} by {book.author.name}')
                    print(f'{pages} not found')
                    
# Create some authors
author1 = Author('J.K. Rowling')
author2 = Author('J.R.R. Tolkien')
author3 = Author('George R.R. Martin')
author4 = Author
author5 = Author('Stephen King')
author6 = Author('Dan Brown')
author7 = Author('Agatha Christie')
author8 = Author('Arthur Conan Doyle')
author9 = Author
author10 = Author('Jules Verne')

# Create some genres
genre1 = Genre('Fantasy')
genre2 = Genre('Mystery')
genre3 = Genre('Science Fiction')
genre4 = Genre('Horror')
genre5 = Genre('Adventure')
genre6 = Genre('Historical Fiction')
genre7 = Genre('Romance')
genre8 = Genre('Non-Fiction')
genre9 = Genre('Biography')
genre10 = Genre('Autobiography')

# Create some books
book1 = Book('Harry Potter and the Philosopher\'s Stone', author1, genre1, 223)
book2 = Book('The Hobbit', author2, genre5, 310)
book3 = Book('A Game of Thrones', author3, genre1, 694)
book4 = Book('The Shining', author5, genre4, 447)
book5 = Book('The Da Vinci Code', author6, genre2, 454)

# Create a library
library = Library('My Library')

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# List all books in the library
library.list_books()

# Search for a book by title
library.search_books('The Hobbit')

# Search for a book by author
library.search_author('J.R.R. Tolkien')

# Search for a book by genre
library.search_genre('Fantasy')
