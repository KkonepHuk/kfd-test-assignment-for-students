class Book:
    #Инициализирование книги
    def __init__(self, title, author, isbn, genre, status=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.status = status
    
    def __str__(self):
        s = f'[ISBN: {self.isbn}, Title: {self.title}, Autor: {self.author}, Genre: {self.genre}, Status: {self.status}]'
        return s
    
    def show(self):
        return self.__str__()