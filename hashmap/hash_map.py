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