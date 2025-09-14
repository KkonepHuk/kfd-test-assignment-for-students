from data_structures.hash_map import HashMap
from data_structures.singly_linked_list import SinglyLinkedList


class UsersMap(HashMap):
    def __init__(self, size=1000):
        super().__init__(size)

    #Хэш-функция
    def hash_func(self, user_id):
        return sum(ord(c) for c in user_id) % self.size