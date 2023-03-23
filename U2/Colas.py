class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
    
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if not self.head else False
    
    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            old = self.head
            self.size -= 1
            if self.size == 1:
                self.tail = None
            data = self.head.data
            self.head = self.head.next
            del old
            return data
    
    #def exist(self):

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
#print (q.getSize())

for i in range (4):
        print (q.dequeue())


