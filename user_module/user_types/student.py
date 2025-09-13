from user import User


class Student(User):
    def __init__(self, name, user_id, email, borrowed_books = []):
        super().__init__(name, user_id, email, borrowed_books)
    
    def get_max_books(self):
        return 3

    def get_borrow_days(self):
        return 14

    def get_fine_per_day(self):
        return 0.50
