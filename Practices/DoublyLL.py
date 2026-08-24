class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class dobleLL:
    def __init__(self,head=None):
        self.head = head

    def insertAtEnding(self,value):
        temp = Node(value)
        t = self.head
        if t == None:
            self.head = temp
            return
        while t.next is not None:
            t = t.next
        t.next = temp
        temp.prev = t

    def PrintLL(self):
        t = self.head
        while t.next is not None:
            print(t.data,end=" <--> ")
            t = t.next
        print(t.data)
    def insertAtBeg(self,value):
        temp = Node(value)
        t = self.head
        if t is None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

obj = dobleLL()
obj.insertAtEnding(10)
obj.insertAtEnding(20)
obj.insertAtEnding(30)
obj.insertAtEnding(40)
obj.insertAtBeg(5)
obj.PrintLL()