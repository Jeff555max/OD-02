# Стек (Stack) — это структура данных, работающая по принципу "последний пришел, первый ушел" (Last In, First Out, LIFO).
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == [] # проверяет пустой ли наш список

    def push(self, item):
        self.items.append(item) # добавляет элемент

    def pop(self):
        return self.items.pop() # удаляет последний элемент

    def peek(self):
        return self.items[-1] # возвращает первый элемент с конца списка (элемент добавленный последним)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty()) # проверяем пустой список или нет
print(stack.peek()) # проверяем какой элемент добавлен последним

stack.pop() # удаляем последний элемент

print(stack.peek()) # # проверяем какой элемент последний