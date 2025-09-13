class Node:
    def __init__(self, item, key):
        self.key = key
        self.item = item
        self.next = None

class SinglyLinkedList:

    #Инициализация односвязного списка
    def __init__(self):
        self.head = None
        self.length = 0

    #Строковый формат
    def __str__(self):
        current = self.head
        s = ''
        while current:
            s += f'{str(current.item)}->'
            current = current.next
        return s[:-2]