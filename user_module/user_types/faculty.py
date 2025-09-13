from user import User

class Faculty(User):
    def __init__(self, name, user_id, email, borrowed_books = []):
        super().__init__(name, user_id, email, borrowed_books)

    def get_max_books(self):
        pass

    def get_borrow_days(self):
        pass

    def get_fine_per_day(self):
        pass

    def can_borrow(self):
        pass