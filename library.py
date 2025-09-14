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


    ##### Операции с Книгами #####

    def add_book(self, title, author, isbn, genre):
        book = Book(title, author, isbn, genre)
        self.books.add(book)
    
    def remove_book(self, isbn):
        if self.books.remove(isbn) == -1:
            return False
        return True

    def find_book(self, isbn):
        book = self.books.get(isbn)
        if book != -1:
            return book
        return False
    
    def search_books(self, query: str):
        result = []
        query = query.lower()

        for book in self.books.hash_map_to_arr():
            if (query in book[0].lower() or
                query in book[1].lower() or
                query in book[2].lower() or
                query in book[3].lower()):
                result.append(book)
        return result
    
    ##### Операции с Пользователями #####

    def register_user(self, name, user_id, email, type: str):
        match type.lower():
            case 'student':
                user = Student(name, user_id, email)
            case 'guest':
                user = Guest(name, user_id, email)
            case 'faculty':
                user = Faculty(name, user_id, email)
            case _:
                return -1 #Поменять на нормальный вывод
        
        self.users.add(user)
    
    def find_user(self, user_id):
        user = self.users.get(user_id)
        if user != -1:
            return user
        return 'No specific user'


    ##### Заемные операции #####

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
    
    def return_book(self, user_id, isbn):
        user = self.users.get(user_id)
        book = self.books.get(isbn)

        if user == -1 or book == -1: #Существуют ли книга и пользователь
            return False
        if isbn not in user.borrowed_books:
            return False
        
        for record in self.borrowing_history:
            if record.user.user_id == user_id and record.book.isbn == isbn and not record.returned:
                record.mark_returned()
        book.set_available(True)
        user.get_borrowed_books().remove(isbn)

        return True
    
    def get_overdue_books(self):
        result = []
        for record in self.borrowing_history:
            if record.is_overdue() and (not record.returned):
                result.append(str(record))
        return result
