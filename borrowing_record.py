from datetime import date


class BorrowingRecord:
    def __init__(self, user, book, date = date.today):
        self.user = user
        self.book = book
        self.date = date