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
    
        #Добавление в начало списка
    def add_to_start(self, item, key):
        new_node = Node(item, key)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
        #Удаление узла
    def remove(self, key):
        current = self.head
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    #Удаление головы
                    self.head = current.next
                else:
                    prev.next = current.next

                self.length -= 1
                return
            prev = current
            current = current.next

    
    #Удаление узла из начала
    def remove_from_start(self):
        if self.head:
            removed = self.head
            self.head = self.head.next
            self.length -= 1
            return removed
    
    #Поиск в списке значения по ключу
    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.item
            current = current.next
        return -1