from library import Library
from handlers.book_managment import handle_book_managment
from handlers.user_managment import handle_user_managment
from handlers.borrowing_operations import handle_borrowing_operations
from utils import get_input

def show_menu():
    print("\n=== Library Management ===\n")
    print("1. Book Management\n")
    print("2. User Management\n")
    print("3. Borrowing Operations\n")
    print("0. Exit\n")



if __name__ == '__main__':
    lib = Library()
    is_launched = True
    while is_launched:
        show_menu()
        choice = get_input(prompt="Enter choice: ", valid_input="0123w")

        match choice:
            case '0':
                is_launched = False
            case '1':
                handle_book_managment(lib)
            case '2':
                handle_user_managment(lib)
            case '3':
                handle_borrowing_operations(lib)
            case 'w':
                print("Users")
                lib.users.test_show()
                print("Books")
                lib.books.test_show()