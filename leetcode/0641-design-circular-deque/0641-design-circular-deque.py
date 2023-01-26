class MyCircularDeque:

    def __init__(self, k: int):
        self.head,self.tail=ListNode(None),ListNode(None)
        self.k,self.len=k,0
        self.head.right,self.tail.left=self.tail,self.head

    def insertFront(self, value: int) -> bool:
        if self.len==self.k:
            return False
        self.len+=1
        new=ListNode(value)
        new.right=self.head
        self.head.left=new
        self.head=new
        self.head.left=ListNode(None)
        self.head.left.right=self.head
        if self.len==1:
            self.tail=new
        return True

    def insertLast(self, value: int) -> bool:
        if self.len==self.k:
            return False
        self.len+=1
        new=ListNode(value)
        new.left=self.tail
        self.tail.right=new
        self.tail=new
        self.tail.right=ListNode(None)
        self.tail.right.left=self.tail
        
        if self.len==1:
            self.head=new
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.len-=1
        self.head=self.head.right
        self.head.left=ListNode(None)
        if self.len==0:
            self.tail=self.head
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.len-=1
        self.tail=self.tail.left
        self.tail.right=ListNode(None)
        if self.len==0:
            self.head=self.tail
        return True

    def getFront(self) -> int:
        return -1 if self.head.val==None else self.head.val

    def getRear(self) -> int:
        return -1 if self.tail.val==None else self.tail.val

    def isEmpty(self) -> bool:
        if self.len==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.len==self.k:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()