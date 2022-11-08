# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=end=head
        while end.next:
            end=end.next
        ith=0
        remove=head
        while ith!=n and remove:
            ith+=1
            remove=remove.next
        if not remove:
            return head.next
        while remove:
            if remove==end:
                node.next=node.next.next
            node=node.next
            remove=remove.next
        return head
            
        