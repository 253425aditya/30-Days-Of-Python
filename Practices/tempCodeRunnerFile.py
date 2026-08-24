class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self,head=None):
        self.head = head

    def insertList(self,value):
        temp = Node(value)
        if self.head != None:
            t1 = self.head
            while(t1 != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printList(self):
        t1 = self.head()
        while(t1 != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = linkedlist()
obj.insertList(10)
obj.insertList(20)
obj.insertList(30)

        