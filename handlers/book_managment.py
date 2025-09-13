from library import Library
from utils import get_input


def show_book_managment_menu():
    print("\n=== Book Management ===\n")
    print("1. Add Book\n")
    print("2. Remove Book\n")
    print("3. Search a book by ISBN\n")
    print("4. Search for a book by request\n")
    print("0. Quit from this menu\n")

def add_book_to_library(lib: Library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book isbn: ")
    genre = input("Enter book genre: ")

    lib.add_book(title, author, isbn, genre)

    print("\nThe book has been added successfully!\n")

def remove_book_from_library(lib: Library):
    isbn = input("Enter the isbn of the book you want to remove: ")

    if lib.remove_book(isbn):
        print("\nThe book was successfully removed\n")
    else:
        print("\nBooks with such isbn do not exist\n")

def find_book_by_isbn(lib: Library):
    isbn = input("Enter the isbn of the book you want to find: ")
    book = lib.find_book(isbn)
    if book:
        print("\n" + str(book) + "\n")
    else:
        print("\nBooks with such isbn do not exist\n")

def search_book_by_query(lib: Library):
    query = input("Enter a query that will be used to search for books: ")
    
    books = lib.search_books(query)
    if len(books) == 0:
        print("\nNo matching books found\n")
    else:
        print('\n' + str(books) + '\n')

def handle_book_managment(lib: Library):
    is_launched = True
    while is_launched:
        show_book_managment_menu()
        choice = get_input(prompt="Enter choice: ", valid_input="01234")

        match choice:
            case '0':
                is_launched = False
            case '1':
                add_book_to_library(lib)
            case '2':
                remove_book_from_library(lib)
            case '3':
                find_book_by_isbn(lib)
            case '4':
                search_book_by_query(lib)