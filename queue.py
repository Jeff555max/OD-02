# Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out)
class Queue:
    def __init__(self): # метод инициализации, конструктор нашего класса
        self.items = []

    def is_empty(self):
        return self.items == []

    # добавление элемента в конец очереди, те. в начало списка
    def enqueue(self, item):
        self.items.insert(0, item)

    # Удалять будем первый элемент очереди, то есть последний элемент списка
    def dequeue(self):
        return self.items.pop() # возвращает то, что он удалил
    # Подсчет количество элементов находится в очереди
    def size(self):
        return len(self.items)


queue = Queue()

print(queue.is_empty())

queue.enqueue('Act1')
queue.enqueue('Act2')
queue.enqueue('Act3')

# ["Act3", "Act2", "Act1"]

print(queue.size())
print(queue.dequeue())  # возвращает то, что он удалил
print(queue.is_empty())
print(queue.size())