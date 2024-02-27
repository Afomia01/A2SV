class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None


class MyLinkedList:
    def __init__(self):
        self.head= Node()

    def get(self, index: int) -> int:
        temp= self.head
        for _ in range (index+1):
            temp= temp.next
            if temp==None:
                return -1
            
        return temp.val
      
    def addAtHead(self, val: int) -> None:
        newnode= Node(val)
        newnode.next= self.head.next
        self.head.next= newnode

    def addAtTail(self, val: int) -> None:
        newnode=Node(val)
        temp= self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
    def addAtIndex(self, index: int, val: int) -> None:
        newnode=Node(val)
        temp= self.head
        for _ in range (index):
            temp= temp.next
            if temp==None:
                return 
        newnode.next= temp.next
        temp.next=newnode

    def deleteAtIndex(self, index: int) -> None:
        temp= self.head
        for _ in range (index):
            temp= temp.next
            if temp==None:
                return
        if temp.next==None:
            return
        temp.next=temp.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)