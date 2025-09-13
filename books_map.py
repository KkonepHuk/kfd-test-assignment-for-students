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
            sll.add_to_start(book)
            self.table[ind] = sll
        else:
            self.table[ind].add_to_start(book)
        self.incr_occupation()