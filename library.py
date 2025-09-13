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

    def borrow_book(self, user_id, isbn):
        user = self.users.get(user_id)
        book = self.books.get(isbn)


        #Проверяем возможность взять книгу
        if user == -1 or book == -1: #Существуют ли книга и пользователь
            return False
        if not book.is_available(): #Доступна ли книга
            return False
        if not user.can_borrow(): #Может ли пользователь взять книгу
            return False
        

        book.set_available(False)
        user.get_borrowed_books().append(isbn)
        self.borrowing_history.append(BorrowingRecord(user, book))

        return True