# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        newHead=newLL=ListNode(0)
        for i in range(len(arr)):
            newHead.next=ListNode(arr[i])
            newHead=newHead.next
        return newLL.next