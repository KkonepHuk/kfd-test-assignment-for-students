class User:
    def __init__(self, name, user_id, email, borrowed_books = []):
        self.name = name
        self.user_id = user_id
        self.email = email
        self.borrowed_books = borrowed_books
    
    def __str__(self):
        s = f'[user_id: {self.user_id}, Name: {self.name}, Email: {self.email}, Borrowed Books: {self.borrowed_books}'
        return s
    
    def show(self):
        return self.__str__()
    
class Student(User):
    def __init__(self, name, user_id, email, borrowed_books = []):
        super().__init__(name, user_id, email, borrowed_books)


class Faculty(User):
    def __init__(self, name, user_id, email, borrowed_books = []):
        super().__init__(name, user_id, email, borrowed_books)

class Guest(User):
    def __init__(self, name, user_id, email, borrowed_books = []):
        super().__init__(name, user_id, email, borrowed_books)
