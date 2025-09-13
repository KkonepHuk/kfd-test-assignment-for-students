from user_module.user_types.user import User


class Guest(User):
    def __init__(self, name, user_id, email, borrowed_books = []):
        super().__init__(name, user_id, email, borrowed_books)
    
    def get_max_books(self):
        return 1

    def get_borrow_days(self):
        return 7

    def get_fine_per_day(self):
        return 0.75
