from book_module.book import Book
from book_module.books_map import BooksMap
from borrowing_record import BorrowingRecord
from user_module.user_types.faculty import Faculty
from user_module.user_types.guest import Guest
from user_module.user_types.student import Student
from user_module.users_map import UsersMap



class Library:
    def __init__(self):
        self.books = BooksMap()
        self.users = UsersMap()
        self.borrowing_history = []
        self.genres = set()