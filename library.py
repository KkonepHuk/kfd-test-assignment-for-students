from book_module.books_map import BooksMap
from user_module.users_map import UsersMap
from borrowing_record import BorrowingRecord


class Library:
    def __init__(self):
        self.books = BooksMap()
        self.users = UsersMap()
        self.borrowing_history = []
        self.genres = set()
    
        
