class Book:
    #Инициализирование книги
    def __init__(self, title, author, isbn, genre, status=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.status = status

    def is_available(self):
        return self.status
    
    def set_available(self, status: bool):
        self.status = status

    def not_bool_status(self):
        if self.status:
            st = 'Available'
        else:
            st = 'Not Available'
        
        return st
    def book_to_arr(self):
        st = self.not_bool_status()

        return [self.isbn, self.title, self.author, self.genre, st]
    
    def __str__(self):
        st = self.not_bool_status()

        s = f'[ISBN: {self.isbn}, Title: {self.title}, Autor: {self.author}, Genre: {self.genre}, Status: {st}]'
        return s
    
    def show(self):
        return self.__str__()