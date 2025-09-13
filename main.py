from utils import get_input

def show_menu():
    print("\n=== Library Management ===\n")
    print("1. Book Management\n")
    print("2. User Management\n")
    print("3. Borrowing Operations\n")
    print("0. Exit\n")



if __name__ == '__main__':
    is_launched = True
    while is_launched:
        show_menu()
        choice = get_input(prompt="Enter choice: ", valid_input="0123")

        match choice:
            case '0':
                is_launched = False
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass