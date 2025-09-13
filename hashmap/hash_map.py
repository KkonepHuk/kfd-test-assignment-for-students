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