from hashmap.hash_map import HashMap
from hashmap.singly_linked_list import SinglyLinkedList


class UsersMap(HashMap):
    def __init__(self, size=10):
        super().__init__(size)

    #Хэш-функция
    def hash_func(self, user_id):
        return sum(ord(c) for c in user_id) % self.size

    #Добавление пользователя
    @HashMap.expansion
    def add(self, user):
        ind = self.hash_func(user.user_id)
        if self.table[ind] == None:
            sll = SinglyLinkedList()
            sll.add_to_start(user, user.user_id)
            self.table[ind] = sll
        else:
            self.table[ind].add_to_start(user, user.user_id)
        self.incr_occupation()
    
    #Удаление пользователя по "user_id"
    def remove(self, user_id):
        ind = self.hash_func(user_id)
        if self.table[ind] == None:
            return -1
        elif self.table[ind].length > 1:
            self.table[ind].remove(user_id)
        else:
            self.table[ind] = None
        self.decr_occupation()
    
    #Получение пользователя по "user_id"
    def get(self, user_id):
        ind = self.hash_func(user_id)
        if self.table[ind] == None:
            return -1
        else:
            return self.table[ind].find(user_id)