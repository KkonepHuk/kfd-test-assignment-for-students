from datetime import date, timedelta


class BorrowingRecord:
    def __init__(self, user, book, borrow_date = date.today(), returned = False):
        self.user = user
        self.book = book
        self.borrow_date = borrow_date
        self.returned = returned

    def mark_returned(self):
        self.returned = True
    
    def is_overdue(self):
        return date.today() > self.borrow_date + timedelta(days=self.user.get_borrow_days())
    
    def __str__(self):
        s = f'[User: {self.user}, Book: {self.book}, Borrow Date: {self.borrow_date}]'
        return s
