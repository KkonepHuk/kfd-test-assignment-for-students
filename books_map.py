from hashmap.hash_map import HashMap
from hashmap.singly_linked_list import SinglyLinkedList


class BooksMap(HashMap):
    def __init__(self, size=10):
        super().__init__(size)

    #Хэш-функция
    def hash_func(self, isbn):
        clean_isbn = "".join(c for c in isbn if c.isdigit() or c == "-")
        selected = list(map(int, clean_isbn.split("-")))
        hash_value = (selected[1] << 8) + selected[2] * 31 + selected[3] % 17 + selected[4]
        return hash_value % self.size

    #Добавление книги
    @HashMap.expansion
    def add(self, book):
        ind = self.hash_func(book.isbn)
        if self.table[ind] == None:
            sll = SinglyLinkedList()
            sll.add_to_start(book, book.isbn)
            self.table[ind] = sll
        else:
            self.table[ind].add_to_start(book, book.isbn)
        self.incr_occupation()
    
    #Удаление книги по ее "ISBN"
    def remove(self, isbn):
        ind = self.hash_func(isbn)
        if self.table[ind] == None:
            return -1
        elif self.table[ind].length > 1:
            self.table[ind].remove(isbn)
        else:
            self.table[ind] = None
        self.decr_occupation()
    
    #Получение книги по ее "ISBN"
    def get(self, isbn):
        ind = self.hash_func(isbn)
        if self.table[ind] == None:
            return -1
        else:
            return self.table[ind].find(isbn)