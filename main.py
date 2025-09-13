def show_menu():
    print("\n=== Library Management ===\n")
    print("1. Book Management\n")
    print("2. User Management\n")
    print("3. Borrowing Operations\n")
    print("0. Exit\n")

def get_input(prompt):
    print(prompt)
    user_input = input()
    while not check_input(user_input):
        print("Please enter a valid number.")
        user_input = input()
    return user_input

def check_input(user_input):
    return len(user_input) == 1 and user_input in "0123"


if __name__ == '__main__':
    is_launched = True
    while is_launched:
        show_menu()
        choice = get_input("Enter choice: ")

        match choice:
            case '0':
                is_launched = False
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass