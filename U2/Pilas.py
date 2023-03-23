class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def setData(self, dato):
        self.data = dato

nodo1 = Node("Carito")
print(nodo1.data)
print(nodo1.next)
print(nodo1.getData())

nodo1.setData("Avocado")
print(nodo1.getData())
print(nodo1.data)

nodo2 = Node("José")
nodo1.next = nodo2
print(nodo1.data)