class Book:
    #Инициализирование книги
    def __init__(self, title, author, isbn, genre, status=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.status = status