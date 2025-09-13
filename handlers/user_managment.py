from library import Library
from utils import get_input

def show_user_managment_menu():
    print("\n=== User Management ===\n")
    print("1. Register User\n")
    print("2. Find User\n")
    print("0. Quit from this menu\n")

def register_user_to_library(lib: Library):
    name = input("Enter user name: ")
    user_id = input("Enter user user_id: ")
    email = input("Enter user email: ")
    type = input("Enter user type (Student, Faculty, Guest): ")

    if lib.register_user(name, user_id, email, type) == -1:
        print("\nInvalid user type. Try again.\n")
    else:
        print("\nThe user has been added successfully!\n")

def find_user_by_user_id(lib: Library):
    user_id = input("Enter the user_id of the user you want to find: ")
    user = lib.find_user(user_id)
    if user:
        print("\n" + str(user) + "\n")
    else:
        print("\nUser with such user_id do not exist\n")


def handle_user_managment(lib: Library):
    is_launched = True
    while is_launched:
        show_user_managment_menu()
        choice = get_input(prompt="Enter choice: ", valid_input="012")

        match choice:
            case '0':
                is_launched = False
            case '1':
                register_user_to_library(lib)
            case '2':
                find_user_by_user_id(lib)