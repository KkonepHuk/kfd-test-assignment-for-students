class User:
    def __init__(self, name, user_id, email, borrowed_books = None):
        self.name = name
        self.user_id = user_id
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
    
    def get_max_books(self):
        pass

    def get_borrow_days(self):
        pass

    def get_fine_per_day(self):
        pass
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def can_borrow(self):
        return len(self.borrowed_books) < self.get_max_books()
    
    def __str__(self):
        s = f'[user_id: {self.user_id}, Name: {self.name}, Email: {self.email}, Borrowed Books: {self.borrowed_books}'
        return s
    
    def show(self):
        return self.__str__()
    


