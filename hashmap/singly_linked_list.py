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
    def add_to_start(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1