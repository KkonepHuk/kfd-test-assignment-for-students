from hashmap.singly_linked_list import SinglyLinkedList


class HashMap:
    #Инициализирование Хэш-Таблицы с заданным размером size
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.occupancy = 0

    #Увеличение на 1 счётчика заполненных ячеек Хэш-Таблицы
    def incr_occupation(self):
        self.occupancy += 1
    
    #Уменьшение на 1 счётчика заполненных ячеек Хэш-Таблицы
    def decr_occupation(self):
        self.occupancy -= 1
    
    #Вычисление коэффициента заполнения таблицы
    def occupancy_rate(self):
        return self.occupancy / self.size if self.size > 0 else 0
    
    @staticmethod
    def expansion(add_func):
        def wrapper(self, *args):
            if self.occupancy_rate() >= 2 / 3:
                new_size = self.size + int(self.size * 2 / 3)
                new_library_system = HashMap(new_size)
                for sll in self.table:
                    while sll and sll.head:
                        node = sll.remove_from_start()
                        item = node.item
                        new_library_system.add(item)
                self.size = new_library_system.size
                self.table = new_library_system.table
                self.occupancy = new_library_system.occupancy

            return add_func(self, *args)
        return wrapper
    
        #Добавление книги
    @expansion
    def add(self, item, key):
        ind = self.hash_func(key)
        if self.table[ind] == None:
            sll = SinglyLinkedList()
            sll.add_to_start(item, key)
            self.table[ind] = sll
        else:
            self.table[ind].add_to_start(item, key)
        self.incr_occupation()
    
    def remove(self, key):
        ind = self.hash_func(key)
        if self.table[ind] == None:
            return -1
        elif self.table[ind].length > 1:
            self.table[ind].remove(key)
        else:
            self.table[ind] = None
        self.decr_occupation()
    
        #Получение книги по ее "ISBN"
    def get(self, key):
        ind = self.hash_func(key)
        if self.table[ind] == None:
            return -1
        else:
            return self.table[ind].find(key)
    
    #Вывод всей Хэш-Таблицы для тестов
    def test_show(self):
        for i in range(self.size):
            if self.table[i] == None:
                print(f'{i} : {self.table[i]}')
            else:
                print(f'{i} : {self.table[i].show()}')
    
    #Вывод всех элементв в Хэш-Таблице
    def show(self):
        for i in range(self.size):
            if self.table[i] != None:
                print(f'{self.table[i].show()}')

    #Преобразует Хэш-Таблицу в двумернай массив
    def hash_map_to_arr(self):
        data = []
        for i in range(self.size):
            if self.table[i] != None:
                data.extend(self.table[i].list_to_arr())
        return data