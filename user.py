class User:
    def __init__(self, name, user_id, email, borrowed_books = []):
        self.name = name
        self.user_id = user_id
        self.email = email
        self.borrowed_books = borrowed_books
    