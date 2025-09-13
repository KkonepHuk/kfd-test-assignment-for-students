from datetime import date


class BorrowingRecord:
    def __init__(self, user, book, borrow_date = date.today()):
        self.user = user
        self.book = book
        self.borrow_date = borrow_date
    
    def is_overdue(self):
        return date.today() > self.borrow_date
