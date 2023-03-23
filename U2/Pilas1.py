class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

class Stack:
    def __init__ (self):
        self.head = None
        self.size = 0

    def getSize (self):
        return self.size
    
    def IsEmpty (self):
        return True if self.size == 0 else False
        return True if not self.size else False
        return True if self.head else False
    
    def push(self, data):
        new_Node = Node (data)
        new_Node.next = self.head
        self.head = new_Node
        self.size += 1

    def pop(self):
        dato = None
        if not self.IsEmpty():
            dato = self.head.data
            self.head = self.head.next
            self.size -= 1
        return dato

    def peak(self):
        dato = None
        if not self.IsEmpty():
            dato = self.head.data
        return dato

    def print(self):
        if not self.IsEmpty():
            aux = self.head
            while aux:
                print(aux.data)
                aux = aux.next
        return (None)
    
    def exist (self, data):
        if not self.IsEmpty():
            aux = self.head
            while aux:
                if aux.data == data:
                    return True
                aux = aux.next
        return False
    

    
    

pila = Stack()

pila.push("Jesús")
pila.push("María")
pila.push("José")


print(pila.exist("Jesús"))
print(pila.exist("Jorge"))




'''
print(pila.peak())

print(pila.print())


print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
'''

