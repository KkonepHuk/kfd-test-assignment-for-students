from hashmap.hash_map import HashMap
from hashmap.singly_linked_list import SinglyLinkedList


class UsersMap(HashMap):
    def __init__(self, size=10):
        super().__init__(size)

    #Хэш-функция
    def hash_func(self, user_id):
        return sum(ord(c) for c in user_id) % self.size