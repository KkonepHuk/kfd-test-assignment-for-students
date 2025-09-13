class HashMap:
    #Инициализирование Хэш-Таблицы с заданным размером size
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.occupancy = 0
