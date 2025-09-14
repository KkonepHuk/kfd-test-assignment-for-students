from data_structures.hash_map import HashMap
from data_structures.singly_linked_list import SinglyLinkedList


class BooksMap(HashMap):
    def __init__(self, size=10):
        super().__init__(size)

    #Хэш-функция
    '''Хэш-функция для реального isbn
    def hash_func(self, isbn):
        clean_isbn = "".join(c for c in isbn if c.isdigit() or c == "-")
        selected = list(map(int, clean_isbn.split("-")))
        hash_value = (selected[1] << 8) + selected[2] * 31 + selected[3] % 17 + selected[4]
        return hash_value % self.size'''
    
    '''Хэш-функция для любой строки, в качестве isbn'''
    def hash_func(self, isbn):
        hash_value = 0
        for char in isbn:
            hash_value = (hash_value * 31 + ord(char))
        return hash_value % self.size