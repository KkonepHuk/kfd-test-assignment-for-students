def get_input(prompt, valid_input):
    print(prompt)
    user_input = input()
    while not check_input(user_input, valid_input):
        print("Please enter a valid number.")
        user_input = input()
    return user_input

def check_input(user_input, valid_input):
    return len(user_input) == 1 and user_input in valid_input