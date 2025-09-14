from core.library import Library
from core.utils import get_input


def show_borrowing_operations_menu():
    print("\n=== Borrowing Operations ===\n")
    print("1. Borrow Book\n")
    print("2. Return Book\n")
    print("3. Get Overdue Books\n")
    print("0. Quit from this menu\n")

def borrow_book_from_library(lib: Library):
    user_id = input("Enter the user's user_id: ")
    isbn = input("Enter the book's isbn: ")

    if lib.borrow_book(user_id, isbn):
        print("\nThe book has been borrowed successfully!\n")
    else:
        print("\nOperation impossible.\n")

def return_book_to_library(lib: Library):
    user_id = input("Enter the user's user_id: ")
    isbn = input("Enter the book's isbn: ")

    if lib.return_book(user_id, isbn):
        print("\nThe book has been returned successfully!\n")
    else:
        print("\nOperation impossible.\n")

def get_library_overdue_books(lib: Library):
    books = lib.get_overdue_books()
    if len(books) == 0:
        print("\nNo expired books\n")
    else:
        print('\n' + str(books) + '\n')



def handle_borrowing_operations(lib: Library):
    is_launched = True
    while is_launched:
        show_borrowing_operations_menu()
        choice = get_input(prompt="Enter choice: ", valid_input="0123")

        match choice:
            case '0':
                is_launched = False
            case '1':
                borrow_book_from_library(lib)
            case '2':
                return_book_to_library(lib)
            case '3':
                get_library_overdue_books(lib)